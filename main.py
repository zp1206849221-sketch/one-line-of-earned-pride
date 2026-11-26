import os

LINE = "The night before her seventh driving test, after six failures, Rosa, 44, eased between the cones in the empty lot without touching one, then sat with her hands still on the wheel, smiling at no one."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
