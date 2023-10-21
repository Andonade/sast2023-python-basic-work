import json
import random
import re
import streamlit as st


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
    for i in range(len(hints)):
        key = st.text_input(f'提示{i + 1}：{hints[i]}')
        keys.append(key)
    return keys


def replace(article, keys):
    """
    替换文章内容
    :param article: 文章内容
    :param keys: 用户输入的单词
    :return: 替换后的文章内容
    """
    pattern = r'{{(\d+)}}'
    article = re.sub(pattern, lambda match: keys[int(match.group(1)) - 1], article)
    return article


def get_hints(num):
    """
    获取用户输入的提示信息
    :param num: 提示的数量
    :return: 提示信息的列表
    """
    hints = []
    for i in range(num):
        hint = st.text_input(f'请输入第{i + 1}个提示')
        hints.append(hint)
    return hints


if __name__ == "__main__":
    st.title('文章填词小游戏')
    st.sidebar.header('Made by Andonade')
    st.sidebar.markdown('什么都还没有的[github](https://github.com/Andonade)')
    st.sidebar.markdown('[仓库地址](https://github.com/Andonade/sast2023-python-basic-work.git)')
    mode = st.selectbox('选择游戏模式', options=['做题模式', '出题模式'])
    if mode == '做题模式':
        file = st.text_input('请输入题库文件名', value='example.json')
        try:
            data = read_articles(file)
            if not (data.get('articles', 0) != 0 and data.get('language', 0)):
                st.text('题库文件格式有误，可自行更改或更换一个题库文件')
            elif not data['articles']:
                st.text('题库中无文章，可选择出题模式进行出题或更换一个题库文件')
            else:
                isDesignated = st.checkbox('是否指定文章', value=True)
                articles = data["articles"]
                title = ''
                flag = -1
                if isDesignated:
                    titles = []
                    for i in range(len(articles)):
                        titles.append(articles[i]['title'])
                    title = st.selectbox('请指定您想要的文章', options=titles)
                    flag = titles.index(title)
                else:
                    flag = random.choice(range(len(articles)))
                    title = articles[flag]['title']
                    st.text(f'您随机到了《{title}》这篇文章')
                article = articles[flag]['article']
                keys = get_inputs(articles[flag]['hints'])
                if st.button('完成'):
                    article = replace(article, keys)
                    st.write('替换结果：', article)
        except FileNotFoundError:
            st.text('题库文件不存在')
    else:
        file = st.text_input('请输入要保存到的题库文件名', value='example.json', help='若文件不存在则将新建')
        title = st.text_input('请输入文章标题')
        article = st.text_area('请输入文章正文', help='挖空请按照{{1}}格式，多个挖空请按照{{1}}、{{2}}、{{3}}……的顺序')
        pattern = re.compile(r'{{(\d+)}}')
        substrings = pattern.findall(article)
        if substrings:
            num = max(int(match) for match in substrings)
            st.text(f'发现了{num}个挖空')
            hints = get_hints(num)
            if st.button('完成'):
                dict_temp = {'title': title, 'article': article, 'hints': hints}
                try:
                    with open(file, "r", encoding="utf-8") as f:
                        data = json.load(f)
                    data['articles'].append(dict_temp)
                    with open(file, "w") as f:
                        json.dump(data, f, ensure_ascii=False)
                except FileNotFoundError:
                    with open(file, "x") as f:
                        articles = [dict_temp]
                        dict = {'language': 'zh', 'articles': articles}
                        json.dump(dict, f, ensure_ascii=False)
