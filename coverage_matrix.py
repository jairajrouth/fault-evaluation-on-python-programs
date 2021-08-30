from bs4 import BeautifulSoup
import pandas as pd
from openpyxl import load_workbook


# def generate_line_coverage():
#     with open("buggy_coverage/black_py.html", "r") as f:
#         statement_coverage_list = []
#         for line in f.readlines():
#             soup = BeautifulSoup(line, 'html.parser')
#             if soup.find_all("p", attrs={"class": "run"}):
#                 # print("0")
#                 # print(soup)
#                 statement_coverage_list.append(0)
#             elif soup.find_all("p", attrs={"class": "mis show_mis"}):
#                 # print("1")
#                 # print(soup)
#                 statement_coverage_list.append(1)
#             elif soup.find_all("p", attrs={"class": "pln"}):
#                 # print("0")
#                 # print(soup)
#                 statement_coverage_list.append(1)
#
#         statement_coverage_df = pd.DataFrame(statement_coverage_list)
#         print(statement_coverage_df)
#         file_path = '/home/jai/fault-evaluation-on-python-programs/buggy_coverage/statement_coverage_file.xlsx'
#         book = load_workbook(file_path)
#         writer = pd.ExcelWriter(file_path, engine='openpyxl')
#         writer.book = book
#         writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
#         statement_coverage_df.to_excel(writer, sheet_name="Sheet1", index=None, header=None, startcol=0, startrow=0)
#         writer.save()


def get_tests_result():
    # Run py.test tests\test_black.py --excelreport=testreport2.xls --verbose
    # for generating xlsx file.
    data = pd.ExcelFile("buggy_coverage/buggy_test_report.xlsx").parse("Sheet1")
    test_results_df = pd.DataFrame(data, columns=['RESULT'])
    test_results_df = test_results_df.rename(columns={'RESULT': 'TEST_RESULT'})
    test_results_df = test_results_df.T
    test_results_df.to_excel("buggy_coverage/buggy_test_report_result_col.xlsx", startrow=0, startcol=0)


def to_run_tests():
    result_from_tests = pd.ExcelFile("fixed_test_reportm1.xlsx").parse("Sheet1")
    tests_name = pd.DataFrame(result_from_tests, columns=['SUITE NAME', 'TEST NAME'])
    number_of_tests = len(tests_name.index)
    # print(">>>>>>>>>>>>>>", tests_name)
    for num in range(number_of_tests):
        print("<<<<<<<<<<<", tests_name.iloc[num])
        if tests_name.iloc[num, 0] == "BlackTestCase":
            cov = Coverage()
            cov.start()
            print("Running the Pytest...")
            pytest.main(["-x", "tests/test_black.py::BlackTestCase::" + tests_name.iloc[num, 1]])
            cov.stop()
            cov.save()
            cov.report()
            print("Generating Coverage report...")
            cov.html_report(directory='covhtml')
            cov.erase()
        else:
            cov = Coverage()
            cov.start()
            print("Running the Pytest...")
            pytest.main(["-x", "tests/test_black.py::BlackDTestCase::" + tests_name.iloc[num, 1]])
            cov.stop()
            cov.save()
            cov.report()
            print("Generating Coverage Report...")
            cov.html_report(directory='covhtml')
            cov.erase()

            # # print("tests_name.iloc[52]", tests_name.iloc[52, 0])


if __name__ == '__main__':
    # generate_line_coverage()
    get_tests_result()
    to_run_tests()


