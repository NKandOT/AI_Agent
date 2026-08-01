from functions.get_file_contents import get_file_content

def main():
    cases = ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]
    for file in cases:
        test = get_file_content("calculator", file)
        print(f"{file} length: {len(test)}")
        print(f"{file} truncated: {'truncated' in test}")
        print(test)


if __name__ == "__main__":
    main()

