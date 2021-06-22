from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook


def generate_line_coverage():
    with open("buggy_version/htmlcov/black_py.html", "r") as f:
        statement_coverage_list = []
        for line in f.readlines():
            soup = BeautifulSoup(line, 'html.parser')
            if soup.find_all("p", attrs={"class": "run"}):
                # print("0")
                # print(soup)
                statement_coverage_list.append(0)
            elif soup.find_all("p", attrs={"class": "mis show_mis"}):
                # print("1")
                # print(soup)
                statement_coverage_list.append(1)
            elif soup.find_all("p", attrs={"class": "pln"}):
                # print("0")
                # print(soup)
                statement_coverage_list.append(1)

        statement_coverage_df = pd.DataFrame(statement_coverage_list)
        # print(statement_coverage_df)
        cov_file_path = "buggy_coverage/statement_coverage_file.xlsx"
        writer = pd.ExcelWriter(cov_file_path, engine='openpyxl', mode='a')
        writer.book = load_workbook(cov_file_path)
        writer.sheets = {ws.title: ws for ws in writer.book.worksheets}
        statement_coverage_df.to_excel(writer, index=None, header=None, startcol=96)
        writer.save()


def get_tests_result():
    # Run py.test tests\test_black.py --excelreport=testreport2.xls --verbose
    # for generating xlsx file.
    data = pd.ExcelFile("buggy_coverage/test_report.xlsx").parse("Sheet1")
    test_results_df = pd.DataFrame(data, columns=['RESULT'])
    test_results_df = test_results_df.rename(columns={'RESULT': 'TEST_RESULT'})
    test_results_df = test_results_df.T
    test_results_df.to_excel("buggy_coverage/test_report_with_result_col.xlsx", startrow=0, startcol=0)


if __name__ == '__main__':
    # get_tests_result()
    generate_line_coverage()

