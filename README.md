# sast2023 word game

## 环境配置

使用`pip3 install -r requirements.txt`来配置

## 使用设置

使用`streamlit run main.py`来运行游戏

文章使用 JSON 存储，格式如下：

```json
{
    "languge": "zh",
    "articles": [
        {
            "title": "这是标题1",
            "article": "这是文章1",
            "hints": "这是提示1"
        },
        {
            "title": "这是标题2",
            "article": "这是文章2",
            "hints": "这是提示2"
        },
        ...
    ]
}
```

## 游戏功能

本项目完成了python作业的基础功能，即

- 启动：设置了三个参数，能够完成基本要求的游戏设置
- 读取：能够解析作为题库的JSON文件
- 输入以及替换：能够向玩家展示hints、接受标准输入并替换文章的正确部分
- 显示：将替换后的文章在命令行打印

同时，本项目也完成了部分扩展功能，即

- GUI：使用第三方库`streamlit`完成了简单GUI的构建
- 鲁棒性：通过`try… except`优化了对不合法输入的处理
- 出题功能：用户能够自定义新的文章并存储到用户指定的JSON文件内