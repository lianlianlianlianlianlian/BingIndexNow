# Sitemap URL 提交至 IndexNow

## 介绍

该 Python 脚本从网站地图中获取 URL 并将其提交到 IndexNow API 进行索引。对于希望确保其 URL 快速被搜索引擎索引的网站所有者非常有用。

因为我并不会开发插件 所以只能用GPT按照我的需求写一个相对符合我需求的脚本 然后再自己动脑子修改 这个脚本 可以随便挂到一台云服务器 计划任务执行即可实现全自动 目前必应估计是全球搜索引擎里最勤劳的服务商了 谷歌好像也有个API提交 但我还没研究 百度一天只有几个提交名额 而且还不一定收录 所以就不折腾了
这个脚本简单粗暴实现目的 真滴好用

## 功能

- 从指定的网站地图中获取 URL。
- 将 URL 提交至 IndexNow API。
- 优雅地处理 API 响应和错误。
- 记录每个提交的 URL 状态。

## 要求

- Python 3.x
- `requests` 库
- `xmltodict` 库

您可以使用 pip 安装所需的库：

```bash
pip install requests xmltodict
```

## 配置

在运行脚本之前，您需要配置以下参数：

1. **SITEMAP_URL**：您的网站地图的 URL。
2. **API_KEY**：您的 IndexNow API 密钥。
3. **HOST**：您的主域名（不带 `http://` 或 `https://`）。
4. **KEY_LOCATION**：您服务器上密钥文件的位置。

示例配置：

```python
SITEMAP_URL = 'https://blog.darklotus.cn/sitemap.xml'  # 您的网站地图 URL
API_KEY = 'your_api_key_here'  # 您的实际 API 密钥
HOST = 'darklotus.cn'  # 您的主域名
KEY_LOCATION = f'https://{HOST}/{API_KEY}.txt'  # 密钥位置
```

## 使用方法

要运行脚本，只需执行：

```bash
python your_script_name.py
```

脚本将输出网站地图获取的状态、即将提交的 URL 以及 IndexNow API 的响应。

## 示例输出

```
SITEMAP_URL 响应状态码: 200
即将提交的 URL 地址: {...}
提交的 URL 响应状态码: 200
成功提交的 URL: {...}
提交的 URL: https://example.com/page1 状态码: 200
```

## 错误处理

该脚本包含基本的错误处理机制。如果网站地图获取或 URL 提交失败，将打印状态码和错误信息。

## 许可证

该项目根据 MIT 许可证发布。有关详细信息，请参见 LICENSE 文件。

## 贡献

欢迎提交问题或拉取请求以进行改进或修复错误！您的贡献非常欢迎！

## 鸣谢

- [IndexNow] 提供了 URL 提交的 API。
- [requests] 和 [xmltodict] 处理 HTTP 请求和 XML 解析。