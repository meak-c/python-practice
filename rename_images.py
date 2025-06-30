from pathlib import Path
from sys import argv, exit
from shutil import rmtree


def make_folder_and_files():
    base_dir = Path("test_dir")
    base_dir.mkdir(exist_ok=True)

    file_names = ["img001.jpg", "holiday.jpg", "trip.jpg"]
    for name in file_names:
        (base_dir / name).write_text("Dummy")


def get_extension_and_basename():
    if len(argv) != 3:
        exit("拡張子とファイル名本体のベースの合計2つを順番通りに入力してください（例: python rename_images.py jpg summer2025_）")

    extension = argv[1]
    basename = argv[2]

    return extension, basename


def rename_files(extension, basename):
    base_dir = Path("test_dir")
    index = 1
    for file in base_dir.iterdir():
        if file.is_file():
            new_name = f"{basename}{index}.{extension}"
            (base_dir / new_name).unlink(missing_ok=True)
            file.rename(base_dir / new_name)
            index += 1


def main():
    make_folder_and_files()
    extension, basename = get_extension_and_basename()
    rename_files(extension, basename)
    base_dir = Path("test_dir")
    rmtree(base_dir)


if __name__ == "__main__":
    main()
