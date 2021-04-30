from bs4 import BeautifulSoup
import pandas as pd


def generate_line_coverage():
    with open("buggy_version/htmlcov/black_py.html", "r") as f:
        coverage_file = open("buggy_coverage/coverage_file.txt", "a")
        for line in f.readlines():
            soup = BeautifulSoup(line, 'html.parser')
            if soup.find_all("p", attrs={"class": "run"}):
                # print("0")
                # print(soup)
                coverage_file.write("0")
            elif soup.find_all("p", attrs={"class": "mis show_mis"}):
                # print("1")
                # print(soup)
                coverage_file.write("1")
            elif soup.find_all("p", attrs={"class": "pln"}):
                # print("0")
                # print(soup)
                coverage_file.write("0")


def run_tests_to_add_result_to_coverage_file():
    # Run py.test tests\test_black.py --excelreport=testreport2.xls --verbose
    # for generating xlsx file.
    df = pd.ExcelFile("fixed_version/testreport.xls").parse("Sheet1")
    result_column = []
    result_column.append(df['RESULT'])

    print(type(result_column))
    # for res_col in result_column:
    #     if res_col == "PASSED":
    #         print(res_col)


if __name__ == '__main__':
    # generate_line_coverage()
    run_tests_to_add_result_to_coverage_file()

