s = "<tr><td>{}</td><td>{}</td></tr>"

with open("./books.txt", "r") as fin:
    with open("./00-books.txt", "w") as fout:
        for line in fin:
            line = line.strip()
            if line not in ["", "Miscellaneous"]:
                if "|" in line:
                    try:
                        author, title = line.split("|")
                        author = author.strip()
                        title = title.strip()
                        fout.write(s.format(author, title) + "\n")
                    except:
                        print(line)
                        break
                else:
                    fout.write(s.format("", line) + "\n")
