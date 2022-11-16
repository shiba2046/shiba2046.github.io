---
layout: default
title: Notes on Python
permalink: /python/
---

# Work with file path

Build path with `pathlib.Path`
Python 3.x的推荐方式。不要再用`os.path`

[Building Path with `pathlib`](https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f)

打开文件，并读取内容。添加下层目录文件只需要使用`/`！
```python
from pathlib import Path

data_folder = Path("source_data/text_files/")

file_to_open = data_folder / "raw_data.txt"

print(file_to_open.read_text())
```