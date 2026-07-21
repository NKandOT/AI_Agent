from functions.get_files_info import get_files_info

def main():
    lable = "Result for current directory:"
    cases = [".", "pkg", "/bin", "../"]
    for directory in cases:
        print(lable)
        print(get_files_info("calculator", directory))


if __name__ == "__main__":
    main()

