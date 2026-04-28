from collections import defaultdict
from datetime import datetime
from colorama import Fore, Style, init
import json

init(autoreset=True)


def analyze_logs(file_path, threshold=3, export_json=False):
    failed_attempts = defaultdict(int)
    success_after_fail = []

    logs = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                parts = line.strip().split()

                timestamp = parts[0] + " " + parts[1]
                action = parts[2]
                user = parts[3].split("=")[1]
                ip = parts[4].split("=")[1]

                logs.append({
                    "timestamp": timestamp,
                    "action": action,
                    "user": user,
                    "ip": ip
                })

                if action == "LOGIN_FAILED":
                    failed_attempts[ip] += 1

    except FileNotFoundError:
        return "❌ Erro: arquivo de log não encontrado."
    except Exception as e:
        return f"❌ Erro inesperado: {str(e)}"

    # 🔎 Detectar falha → sucesso
    for i in range(1, len(logs)):
        prev = logs[i - 1]
        curr = logs[i]

        if (
            prev["action"] == "LOGIN_FAILED"
            and curr["action"] == "LOGIN_SUCCESS"
            and prev["ip"] == curr["ip"]
        ):
            success_after_fail.append(curr)

    # 📊 Montar relatório
    report = "\n🔎 RELATÓRIO DE ANÁLISE\n"
    report += "-" * 40 + "\n"

    json_output = {
        "failed_attempts": dict(failed_attempts),
        "alerts": [],
        "successful_after_fail": success_after_fail
    }

    for ip, count in failed_attempts.items():
        report += f"IP: {ip} → {count} tentativas\n"

        if count >= threshold:
            alert_msg = f"Possível brute force em {ip}"
            report += Fore.RED + f"⚠️ ALERTA: {alert_msg}\n"
            json_output["alerts"].append({"ip": ip, "reason": alert_msg})

    if success_after_fail:
        report += Fore.YELLOW + "\n⚠️ POSSÍVEL INVASÃO DETECTADA:\n"
        for event in success_after_fail:
            msg = f"{event['ip']} logou com sucesso após falhas ({event['timestamp']})"
            report += Fore.YELLOW + f"→ {msg}\n"
            json_output["alerts"].append({"ip": event["ip"], "reason": msg})

    # 📁 Export JSON
    if export_json:
        filename = datetime.now().strftime("reports/report_%Y%m%d_%H%M%S.json")
        with open(filename, "w") as f:
            json.dump(json_output, f, indent=4)

        report += f"\n📁 JSON salvo em: {filename}\n"

    return report