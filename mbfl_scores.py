import pandas as pd
import math
from openpyxl import load_workbook


def calc_mbfl_scores():
    file_path = 'suspiciousness_score_mut1.xlsx'
    book = load_workbook(file_path)
    mbfl_df = pd.read_excel(file_path)
    total_scores_indexes = len(mbfl_df.index)
    print(total_scores_indexes)
    # print(mbfl_df.iloc[2, 2])

    mbfl_scores_list = []
    for index in range(total_scores_indexes):
        score = mbfl_df.iloc[index, 4] / total_scores_indexes
        mbfl_scores_list.append(score)
        # print(mbfl_df)

    print(mbfl_scores_list)
    exam_score_df = pd.DataFrame(mbfl_scores_list)
    writer = pd.ExcelWriter(file_path, engine='openpyxl')
    writer.book = book
    writer.sheets = dict((ws.title, ws) for ws in book.worksheets)
    exam_score_df.to_excel(writer, sheet_name="Sheet1", index=None,
                                   header=None, startcol=8, startrow=1)
    writer.save()


if __name__ == '__main__':
    calc_mbfl_scores()
