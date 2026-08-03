from functions.write_file import write_file

def main():
    files = ["lorem.txt", "pkg/morelorem.txt", "/tmp/temp.txt"]
    contents = ["wait, this isn't lorem ipsum", "lorem ipsum dolor sit amet", "this should not be allowed"]
    tests = dict(zip(files, contents))
    for file, content in tests.items():
        test = write_file("calculator", file, content)
        print(test)


if __name__ == "__main__":
    main()