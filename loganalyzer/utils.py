from datetime import datetime
import os

def save_report(content):
    if not os.path.exists("reports"):
        os.makedirs("reports")

    filename = datetime.now().strftime("reports/report_%Y%m%d_%H%M%S.txt")

    with open(filename, "w") as file:
        file.write(content)

    print(f"📁 Relatório salvo em: {filename}")