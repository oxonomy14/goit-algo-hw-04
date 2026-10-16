import argparse
import shutil
from pathlib import Path


def parse_argv():
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює та сортує файли за розширеннями"
    )
    parser.add_argument(
        "-s",
        "--source",
        type=Path,
        required=True,
        help="Шлях до директорії-джерела",
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=Path("dist"),
        help="Шлях до директорії призначення (за замовчуванням dist)",
    )
    return parser.parse_args()


def recursive_copy(source_dir: Path, output_dir: Path):
    try:
        for item in source_dir.iterdir():
            try:
                if item.is_dir():
                    recursive_copy(item, output_dir)

                elif item.is_file():
                    extension = item.suffix.lower().lstrip(".")

                    if not extension:
                        extension = "no_extension"

                    target_dir = output_dir / extension
                    target_dir.mkdir(parents=True, exist_ok=True)

                    shutil.copy2(item, target_dir)

                    print(f"Скопійовано: {item} -> {target_dir}")

            except OSError as e:
                print(f"Помилка обробки {item}: {e}")

    except OSError as e:
        print(f"Помилка доступу до директорії {source_dir}: {e}")


def main():
    args = parse_argv()
    source_dir = args.source
    output_dir = args.output

    if not source_dir.is_dir():
        print(f"Помилка: {source_dir} не є директорією")
        return

    try:
        output_dir.mkdir(parents=True, exist_ok=True)
        recursive_copy(source_dir, output_dir)

    except OSError as e:
        print(f"Помилка роботи з директорією призначення: {e}")


if __name__ == "__main__":
    main()