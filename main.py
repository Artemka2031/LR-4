from user_interface import main_menu
from file_operations import create_data_directory


def main():
    create_data_directory()
    main_menu()


if __name__ == "__main__":
    main()
