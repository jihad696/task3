modes = ("r", "w", "a", "r+")


def read(filepath, option="all"):
    try:
        with open(filepath, modes[0]) as file:
            if not file.readable():
                return "File is not readable"

            if option == "all":
                content = file.read()
            elif isinstance(option, int):
                content = file.read(option)
            elif option == "line":
                content = file.readline()
            elif option == "lines":
                content = file.readlines()
            else:
                content = "Invalid option"
        return content
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"


# =========================


def write(filepath, content, option="normal"):
    try:
        with open(filepath, modes[1]) as file:
            if option == "normal":
                file.write(content)
            elif option == "line":
                file.write(content + "\n")
            elif option == "lines":
                if isinstance(content, list):
                    file.writelines(content)
                else:
                    return "Invalid content type for lines. Must be a list."
            else:
                return "Invalid option"
        return "Write successful"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"


# =====================================================
def append(filepath, content, seek=None):
    try:
        with open(filepath, modes[2]) as file:
            if seek is not None:
                file.seek(seek)

            file.write(content)
        return "Append successful"
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"An error occurred: {e}"


write("asd.txt", "Hello, world!", "normal")
append("asd.txt", "\nThis is a new line.", None)
print(read("asd.txt", "all"))
print(read("asd.txt", 5))
print(read("asd.txt", "line"))
print(read("asd.txt", "lines"))
