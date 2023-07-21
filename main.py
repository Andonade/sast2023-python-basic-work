import argparse
import json
import sys
import random
import re


def parser_data():
    """
    从命令行读取用户参数
    做出如下约定：
    1. -f 为必选参数，表示输入题库文件
    2. -d 为必选参数，表示是否指定文章
    3. -t 当-d True时为必选参数，表示指定文章的标题
    """
    parser = argparse.ArgumentParser(
        prog="Word filling game",
        description="A simple game",
        allow_abbrev=True
    )
    parser.add_argument("-f", "--file", help="题库文件", required=True)
    parser.add_argument("-d", "--designate", help="是否指定文章", required=True)
    parser.add_argument("-t", "--title", help="指定文章的标题")
    args = parser.parse_args()
    return args


def read_articles(filename):
    """
    读取题库文件
    :param filename: 题库文件名
    :return: 一个字典，题库内容
    """
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.load(f)
    return data


def get_inputs(hints):
    """
    获取用户输入

    :param hints: 提示信息

    :return: 用户输入的单词
    """
    keys = []
    for hint in hints:
        print(f"请输入{hint}：")
        temp = input()
        keys.append(temp)
    return keys


def replace(article, keys):
    """
    替换文章内容
    :param article: 文章内容
    :param keys: 用户输入的单词
    :return: 替换后的文章内容
    """
    pattern = r'{{(\d+)}}'

    def regrex_replace(match):
        index = int(match.group(1)) - 1
        return keys[index]
    article = re.sub(pattern, regrex_replace, article)
    return article


if __name__ == "__main__":
    args = parser_data()
    data = read_articles(args.file)
    articles = data["articles"]
    flag = -1
    if args.designate == 'True':
        for i in range(len(articles)):
            if articles[i]["title"] == args.title:
                flag = i
                break
        if flag == -1:
            print(f"{args.title} not found")
            sys.exit()
    else:
        flag = random.choice(range(len(articles)))
        print(f"您抽中了《{articles[flag]['title']}》")
    keys = get_inputs(articles[flag]["hints"])
    print("替换结果如下")
    print(replace(articles[flag]["article"], keys))
