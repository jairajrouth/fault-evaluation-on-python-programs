import pandas as pd
import math


def calc_metrics_parameters():
    coverage_df = pd.read_excel(r'C:\Users\jaira\PycharmProjects\fault-evaluation-on-python-programs'
                                r'\buggy_coverage\statement_coverage_file.xlsx')
    tests_result_df = pd.read_excel(r'C:\Users\jaira\PycharmProjects\fault-evaluation-on-python-programs'
                                    r'\buggy_coverage\test_report_with_result_col.xlsx')
    # Total statements is 3820
    total_statements_indexes = len(coverage_df.index)
    # Total test cases is 95
    total_test_cases = len(tests_result_df.columns)
    # Parameters for metrics calculation
    jaccard = op2 = ochiai = tarantula = 0
    data = []
    data_col_name = ["Jaccard", "Op2", "Ochiai", "Tarantula"]

    for statement_index in range(total_statements_indexes):
        fp_ef = pp_ep = nf = np = 0
        for test_index in range(total_test_cases - 1):
            if coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] == "FAILED":
                fp_ef += 1

            elif coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] == "PASSED":
                pp_ep += 1

            elif coverage_df.iloc[statement_index, test_index] == 1 and tests_result_df.iloc[0][test_index] == "FAILED":
                nf += 1

            elif coverage_df.iloc[statement_index, test_index] == 1 and tests_result_df.iloc[0][test_index] == "PASSED":
                np += 1

        if fp_ef + nf + pp_ep == 0:
            jaccard = 0
        else:
            jaccard = fp_ef / (fp_ef + nf + pp_ep)

        op2 = fp_ef - (pp_ep/(pp_ep + np + 1))

        if fp_ef + nf ==0 or fp_ef + pp_ep == 0:
            ochiai = 0
        else:
            ochiai = fp_ef / math.sqrt((fp_ef + nf)*(fp_ef + pp_ep))

        if fp_ef + nf == 0 or pp_ep + np == 0 or fp_ef + pp_ep == 0:
            tarantula = 0
        else:
            tarantula = (fp_ef / (fp_ef + nf)) / ((fp_ef / (fp_ef + nf)) + (pp_ep / (pp_ep + np)))

        data_temp = {jaccard, op2, ochiai, tarantula}
        data.append(data_temp)

    suspiciousness_df = pd.DataFrame(data, columns=data_col_name)
    suspiciousness_df = suspiciousness_df.fillna(0)
    print("dataframe", suspiciousness_df)
    suspiciousness_df.to_excel("buggy_coverage/suspiciousness_score.xlsx")


if __name__ == '__main__':
    calc_metrics_parameters()
