# sast2023 word game

## 环境配置

使用 `pip3 install -r requirements.txt` 来配置

## 使用设置

使用 `streamlit run main.py` 来 运行游戏

文章使用 JSON 存储，格式如下：

```json
{
    "language": "zh",
    "articles": [
        {
            "title": "这是标题1",
            "article": "这是文章1",
            "hints": ["这是提示1", "..."]
        },
        {
            "title": "这是标题2",
            "article": "这是文章2",
            "hints": ["这是提示2", "..."]
        },
        {
            "title": "这是标题3",
            "article": "这是文章3",
            "hints": ["这是提示3", "..."]
        }
    ]
}
```

## 游戏功能

本项目完成了 Python 作业的基础功能，即

- 启动：较为不美观的参数改为由 GUI 来实现
- 读取：能够解析作为题库的 JSON 文件
- 输入以及替换：能够向玩家展示 hints 、接受标准输入并替换文章的正确部分
- 显示：将替换后的文章打印

同时，本项目也完成了部分扩展功能，如下

- GUI：使用第三方库 `streamlit` 完成了简单 GUI 的构建
- 鲁棒性：通过 `try… except` 优化了对不合法输入的处理
- 出题功能：用户能够自定义新的文章并存储到用户指定的 JSON 文件内
- 更多题目：作者在 **example.json** 添加了三道题目