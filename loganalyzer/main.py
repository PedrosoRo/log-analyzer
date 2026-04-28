import argparse
from loganalyzer.analyzer import analyze_logs
from loganalyzer.utils import save_report


def main():
    print("""
==============================
   LOG ANALYZER v0.1
==============================
""")

    parser = argparse.ArgumentParser(
        description="Ferramenta para detecção de atividades suspeitas em logs"
    )

    parser.add_argument(
        "file",
        help="Caminho do arquivo de log"
    )

    parser.add_argument(
        "--output",
        action="store_true",
        help="Salvar relatório em arquivo TXT"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="Exportar resultado em JSON"
    )

    parser.add_argument(
        "--threshold",
        type=int,
        default=3,
        help="Número mínimo de tentativas para gerar alerta (default: 3)"
    )

    args = parser.parse_args()

    result = analyze_logs(
        args.file,
        threshold=args.threshold,
        export_json=args.json
    )

    if args.output:
        save_report(result)
    else:
        print(result)


if __name__ == "__main__":
    main()