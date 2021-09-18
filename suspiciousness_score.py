import pandas as pd
import math


def calc_metrics_parameters():
    coverage_df = pd.read_excel(r'statement_coverage_file_mut2.xlsx')
    tests_result_df = pd.read_excel(r'fixed_test_report_result_col_m2.xlsx')
    # Total statements is 4194
    total_statements_indexes = len(coverage_df.index)
    print("First Statement", coverage_df.index)
    # Total test cases is 121
    total_test_cases = len(tests_result_df.columns)
    print("First Test Case", tests_result_df.columns)
    # Parameters for metrics calculation
    # jaccard = 0
    # op2 = 0
    # ochiai = 0
    # tarantula = 0
    data = []
    data_col_name = ["Jaccard", "Op2", "Ochiai", "Tarantula", "Jac_Exam_Score", "Op2_Exam_Score", "Och_Exam_Score",
                     "T_Exam_Score"]

    for statement_index in range(total_statements_indexes):
        print("statement index", statement_index)
        fp_ef = pp_ep = nf = np = 0
        for test_index in range(total_test_cases):
            if coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] == "FAILED":
                fp_ef += 1
                print("coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index]"
                      "== FAILED>", coverage_df.iloc[statement_index, test_index], tests_result_df.iloc[0][test_index])

            elif coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] == "PASSED":
                pp_ep += 1
                print("coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] "
                      "== PASSED>", coverage_df.iloc[statement_index, test_index], tests_result_df.iloc[0][test_index])

            elif coverage_df.iloc[statement_index, test_index] == 1 and tests_result_df.iloc[0][test_index] == "FAILED":
                nf += 1
                print("coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index]"
                      "== FAILED>", coverage_df.iloc[statement_index, test_index], tests_result_df.iloc[0][test_index])

            elif coverage_df.iloc[statement_index, test_index] == 1 and tests_result_df.iloc[0][test_index] == "PASSED":
                np += 1
                print("coverage_df.iloc[statement_index, test_index] == 0 and tests_result_df.iloc[0][test_index] "
                      "== PASSED>", coverage_df.iloc[statement_index, test_index], tests_result_df.iloc[0][test_index])

        print("fp_ef, pp_ep, nf, np", fp_ef, pp_ep, nf, np)

        if fp_ef + nf + pp_ep == 0:
            jaccard = 0
            jac_exam_score = 0
        else:
            jaccard = fp_ef / (fp_ef + nf + pp_ep)
            jac_exam_score = jaccard / total_statements_indexes

        if pp_ep + np + 1 == 0:
            op2 = 0
            op2_exam_score = 0
        else:
            op2 = fp_ef - (pp_ep / (pp_ep + np + 1))
            op2_exam_score = op2 / total_statements_indexes

        if fp_ef + nf == 0 or fp_ef + pp_ep == 0:
            ochiai = 0
            och_exam_score = 0
        else:
            ochiai = fp_ef / math.sqrt((fp_ef + nf) * (fp_ef + pp_ep))
            och_exam_score = ochiai / total_statements_indexes

        # if fp_ef + nf == 0 or pp_ep + np == 0 or fp_ef + pp_ep == 0:
        if fp_ef * (pp_ep + np) == 0 or pp_ep * (fp_ef + nf) == 0:
            tarantula = 0
            t_exam_score = 0
        else:
            tarantula = (fp_ef / (fp_ef + nf)) / ((fp_ef / (fp_ef + nf)) + (pp_ep / (pp_ep + np)))
            t_exam_score = tarantula / total_statements_indexes

        data_temp = {jaccard, op2, ochiai, tarantula, jac_exam_score, op2_exam_score, och_exam_score, t_exam_score}
        data.append(data_temp)

    suspiciousness_df = pd.DataFrame(data, columns=data_col_name)
    suspiciousness_df = suspiciousness_df.fillna(0)
    print("len(data[0]", len(data[0]))
    print("dataframe", suspiciousness_df)
    print("total statements, total test cases", total_statements_indexes, total_test_cases)
    suspiciousness_df.to_excel("suspiciousness_score_mut2.xlsx")


if __name__ == '__main__':
    calc_metrics_parameters()