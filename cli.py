import argparse
from Zomboid.inventory import Inventory


def main():
    parser = argparse.ArgumentParser(description="Inventory CLI Tool")
    parser.add_argument("path", help="Path to data file (csv/json/xml)")
    parser.add_argument("--search", help="Search by name")
    parser.add_argument("--id", type=int, help="Search by ID")
    parser.add_argument("--page", type=int, default=1, help="Show page number")
    parser.add_argument("--size", type=int, default=10, help="Page size")

    args = parser.parse_args()

    inv = Inventory(args.path)

    if args.search:
        print(f"Результати пошуку '{args.search}':")
        for i in inv.search_by_name(args.search):
            print(i)
    elif args.id:
        print(f"Предмет з ID={args.id}:")
        print(inv.get_by_id(args.id))
    else:
        print(f"=== Сторінка {args.page} ===")
        inv.show_page(args.page, args.size)

    print("\nВідсоток стану предметів:")
    for cond, pct in inv.state_percentages().items():
        print(f"{cond}: {pct}%")


if __name__ == "__main__":
    main()
