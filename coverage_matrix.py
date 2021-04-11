from bs4 import BeautifulSoup
import re


def read_lines():
    with open("buggy_version/htmlcov/black_py.html", "r") as f:
        coverage_file = open("coverage_file.txt", "a")
        for line in f.readlines()[1:125]:
            soup = BeautifulSoup(line, 'html.parser')
             #code_lines = re.findall("^t.", line)
             #if soup.string.find_all("p", attrs={"class": "mis show_mis"}):
            code_lines = soup.find_all("p", attrs={"id": re.findall("^t.", str(soup))})
            myps = str(code_lines).find("mis show_mis")
            # print("soup", soup)
            # print("code_lines", code_lines)
            print("myps", myps)
                # coverage_file.write("1")
                # print("1")
            # else:
                # coverage_file.write("0")
            # print(line)


def regex_example():
    texts = ["t256", "g5489", "t1245"]
    for text in texts:
        # regex = 't[0-9]+'
        if re.findall("^t.", text):
            print(text)


if __name__ == '__main__':
    read_lines()
    # regex_example()
