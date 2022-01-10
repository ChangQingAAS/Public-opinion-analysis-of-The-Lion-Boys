# coding=gbk
import xlrd
from pyecharts.charts import Bar
from pyecharts.charts import Pie
from pyecharts import options as opts


# ���ж�ȡexcel����ȡ�����������
def Read_Excel(table, tables):
    # �ӵ�2�п�ʼ��ȡ���ݣ���Ϊ���Excel�ļ�����ӵ����п�ʼ���ǿ�����Ϣ
    for rows in range(1, table.nrows - 1):
        dict_ = {"rid": "", "�û�����": "", "΢���ȼ�": "", "΢������": "", "΢��ת����": "", "΢��������": "",
                 "΢������": "", "����ʱ��": "", "�����ؼ���": "", "��������": "", "����������": "", "�����Ķ���": "",
                 "�������": ""}
        dict_["rid"] = table.cell_value(rows, 1)
        dict_["�û�����"] = table.cell_value(rows, 2)
        dict_["΢���ȼ�"] = table.cell_value(rows, 3)
        dict_["΢������"] = table.cell_value(rows, 4)
        dict_["΢��ת����"] = table.cell_value(rows, 5)
        dict_["΢��������"] = table.cell_value(rows, 6)
        dict_["΢������"] = table.cell_value(rows, 7)
        dict_["����ʱ��"] = table.cell_value(rows, 8)
        dict_["�����ؼ���"] = table.cell_value(rows, 9)
        dict_["��������"] = table.cell_value(rows, 10)
        dict_["����������"] = table.cell_value(rows, 11)
        dict_["�����Ķ���"] = table.cell_value(rows, 12)
        dict_["�������"] = table.cell_value(rows, 13)
        tables.append(dict_)


# ���ж�ȡexcel���ʻ�ͳ�Ʊ�������
def Read_Excel_keyword(table, tables):
    # �ӵ�2�п�ʼ��ȡ���ݣ���Ϊ���Excel�ļ�����ӵ����п�ʼ���ǿ�����Ϣ
    for rows in range(1, table.nrows - 1):
        dict_ = {"����": "", "���ִ���": ""}
        dict_["����"] = table.cell_value(rows, 1)
        dict_["���ִ���"] = table.cell_value(rows, 2)
        tables.append(dict_)


# �û���п��ӻ�����״ͼ��
def emotion_bar(tables, file_name):
    num_positive = 0
    num_negative = 0
    for i in tables:
        emotion = i["�������"]
        if emotion == "����":
            num_positive = num_positive + 1
        if emotion == "����":
            num_negative = num_negative + 1
    bar_x_data = ("����", "����")
    bar_y_data = (num_positive, num_negative)
    c = (
        Bar()
            .add_xaxis(bar_x_data)
            .add_yaxis("΢������", bar_y_data, color="#af00ff")
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "������з�����״ͼ" ))
            .render("chart_emotion/" + file_name + "������з�����״ͼ.html")
    )
    print("��з�����״ͼ�������")


# �û���п��ӻ�����״ͼ��
def emotion_pie(tables, file_name):
    num_positive = 0
    num_negative = 0
    for i in tables:
        emotion = i["�������"]
        if emotion == "����":
            num_positive = num_positive + 1
        if emotion == "����":
            num_negative = num_negative + 1
    bar_x_data = ("����", "����")
    bar_y_data = (num_positive, num_negative)
    c = (
        Pie(init_opts=opts.InitOpts(height="800px", width="1200px"))
            .add("��з�������",
                 [list(z) for z in zip(bar_x_data, bar_y_data)],
                 center=["35%", "38%"],
                 radius="40%",
                 label_opts=opts.LabelOpts(
                     formatter="{b|{b}: }{c}  {per|{d}%}  ",
                     rich={
                         "b": {"fontSize": 16, "lineHeight": 33},
                         "per": {
                             "color": "#eee",
                             "backgroundColor": "#334455",
                             "padding": [2, 4],
                             "borderRadius": 2,
                         },
                     }
                 ))
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "������з�����״ͼ"),
                             legend_opts=opts.LegendOpts(pos_left="0%", pos_top="65%"))
            .render("chart_emotion/" + file_name + "������з�����״ͼ.html")
    )
    print("��з�����״ͼ�������")


# �û����Ϳ��ӻ�����״ͼ��
def level_bar(tables, file_name):
    num_nomal_level = 0
    num_blue_v = 0
    num_yellow_v = 0
    num_gold_v = 0
    num_talent = 0
    for i in tables:
        level = i["΢���ȼ�"]
        if level == "��ͨ�û�":
            num_nomal_level = num_nomal_level + 1
        if level == "��v":
            num_blue_v = num_blue_v + 1
        if level == "��v":
            num_yellow_v = num_yellow_v + 1
        if level == "��v":
            num_gold_v = num_gold_v + 1
        if level == "΢������":
            num_talent = num_talent + 1
    bar_x_data = ("��ͨ�û�", "��v", "��v", "��v", "΢������")
    bar_y_data = (num_nomal_level, num_blue_v, num_yellow_v, num_gold_v, num_talent)
    c = (
        Bar()
            .add_xaxis(bar_x_data)
            .add_yaxis("΢������", bar_y_data, color="#af00ff")
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "�����û��ȼ���״ͼ" ))
            .render("chart_level/" + file_name + "�����û��ȼ���״ͼ.html")
    )
    print("�û��ȼ���״ͼ�������")


# �û����Ϳ��ӻ�����״ͼ��
def level_pie(tables, file_name):
    num_nomal_level = 0
    num_blue_v = 0
    num_yellow_v = 0
    num_gold_v = 0
    num_talent = 0
    for i in tables:
        level = i["΢���ȼ�"]
        if level == "��ͨ�û�":
            num_nomal_level = num_nomal_level + 1
        if level == "��v":
            num_blue_v = num_blue_v + 1
        if level == "��v":
            num_yellow_v = num_yellow_v + 1
        if level == "��v":
            num_gold_v = num_gold_v + 1
        if level == "΢������":
            num_talent = num_talent + 1
    bar_x_data = ("��ͨ�û�", "��v", "��v", "��v", "΢������")
    bar_y_data = (num_nomal_level, num_blue_v, num_yellow_v, num_gold_v, num_talent)
    c = (
        Pie(init_opts=opts.InitOpts(height="800px", width="1200px"))
            .add("�û��ȼ�����",
                 [list(z) for z in zip(bar_x_data, bar_y_data)],
                 center=["35%", "38%"],
                 radius="40%",
                 label_opts=opts.LabelOpts(
                     formatter="{b|{b}: }{c}  {per|{d}%}  ",
                     rich={
                         "b": {"fontSize": 16, "lineHeight": 33},
                         "per": {
                             "color": "#eee",
                             "backgroundColor": "#334455",
                             "padding": [2, 4],
                             "borderRadius": 2,
                         },
                     }
                 ))
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "�����û��ȼ���״ͼ" ),
                             legend_opts=opts.LegendOpts(pos_left="0%", pos_top="65%"))
            .render("chart_level/" + file_name + "�����û��ȼ���״ͼ.html")
    )
    print("�û��ȼ���״ͼ�������")


# �ʻ�ͳ�ƿ��ӻ�����״ͼ��
def keyword_bar(tables, file_name):
    keywords = []
    times = []
    for i in tables:
        keywords.append(i["����"])
        times.append(i["���ִ���"])
    bar_x_data = (keywords)
    bar_y_data = (times)
    c = (
        Bar()
            .add_xaxis(bar_x_data)
            .add_yaxis("������ִ���", bar_y_data, color="#af00ff")
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "��״ͼ" ))
            .render("chart_keyword/" + file_name + "��״ͼ.html")
    )
    print("�ʻ�ͳ����״ͼ�������")


# �ʻ�ͳ�ƿ��ӻ�����״ͼ��
def keyword_pie(tables, file_name):
    keywords = []
    times = []
    for i in tables:
        keywords.append(i["����"])
        times.append(i["���ִ���"])
    bar_x_data = (keywords)
    bar_y_data = (times)
    c = (
        Pie(init_opts=opts.InitOpts(height="800px", width="1200px"))
            .add("�ʻ�ͳ��",
                 [list(z) for z in zip(bar_x_data, bar_y_data)],
                 center=["35%", "38%"],
                 radius="40%",
                 label_opts=opts.LabelOpts(
                     formatter="{b|{b}: }{c}  {per|{d}%}  ",
                     rich={
                         "b": {"fontSize": 16, "lineHeight": 33},
                         "per": {
                             "color": "#eee",
                             "backgroundColor": "#334455",
                             "padding": [2, 4],
                             "borderRadius": 2,
                         },
                     }
                 ))
            .set_global_opts(title_opts=opts.TitleOpts(title=file_name + "��״ͼ" ),
                             legend_opts=opts.LegendOpts(pos_left="0%", pos_top="65%"))
            .render("chart_keyword/" + file_name + "��״ͼ.html")
    )
    print("�ʻ�ͳ�Ʊ�״ͼ�������")


if __name__ == '__main__':
    # ��з������û��ȼ����ӻ�
    file_name = "֪���ش�"  # �ļ���
    # ����Excel �ļ�
    data = xlrd.open_workbook("weibo/" + file_name + ".xls")
    # �����һ�����
    table = data.sheets()[0]
    tables = []
    Read_Excel(table, tables)
    emotion_bar(tables, file_name)
    emotion_pie(tables, file_name)
    level_bar(tables, file_name)
    level_pie(tables, file_name)

    # # �ʻ�ͳ�ƿ��ӻ�
    # file_name = file_name + "����΢���ʻ�ͳ��"  # �ļ���
    # # ����Excel �ļ�
    # data = xlrd.open_workbook("seg_result/" + file_name + ".xls")
    # # �����һ�����
    # table = data.sheets()[0]
    # tables = []
    # Read_Excel_keyword(table, tables)
    # keyword_bar(tables, file_name)
    # keyword_pie(tables, file_name)
