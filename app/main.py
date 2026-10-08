from os import remove, mkdir, rename


def move_file(command: str) -> None:
    separated = command.split(" ")
    directories = separated[2].split("/")

    if separated[0] != "mv":
        return

    if len(directories) == 1:
        rename(separated[1], separated[2])
        return

    directory = ""

    for direct in directories[0:-1]:

        directory += direct + "/"
        try:
            mkdir(directory)

        except FileExistsError:
            continue

    with (open(separated[1], "r") as file,
          open(f"{directory}{directories[-1]}", "w") as outfile):

        opened_file = file.read()

        outfile.write(opened_file)

    remove(separated[1])
