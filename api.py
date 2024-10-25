import os
import requests
import xmltodict

# 配置参数
SITEMAP_URLS = [
    'https://darklotus.cn/sitemap.xml',  # 主 sitemap
    'https://blog.darklotus.cn/sitemap.xml',  # 其他 sitemap 示例 可继续添加
]
API_KEY = '5d3a8828f82f4137b955a7b77e3b542b'  # 替换为您的实际 API 密钥
HOST = 'darklotus.cn'  # 主机名（主域名）
KEY_LOCATION = f'https://{HOST}/{API_KEY}.txt'  # keyLocation

# 设置 User-Agent 头
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

def fetch_sitemap_urls():
    """从 sitemap 中获取 URL 列表"""
    all_urls = set()  # 使用 set 避免重复 URL
    for sitemap_url in SITEMAP_URLS:
        try:
            response = requests.get(sitemap_url, headers=HEADERS)
            response.raise_for_status()  # 检查请求是否成功
            sitemap = xmltodict.parse(response.content)
            urls = [url['loc'] for url in sitemap['urlset']['url']]
            all_urls.update(urls)  # 添加到集合中，避免重复
            print(f'SITEMAP_URL {sitemap_url} 响应状态码: {response.status_code}，获取到 {len(urls)} 个 URL.')
        except requests.RequestException as e:
            print(f'请求失败: {sitemap_url}，错误信息: {e}')
        except Exception as e:
            print(f'处理 sitemap 时出错: {sitemap_url}，错误信息: {e}')
    return list(all_urls)  # 返回唯一 URL 列表

def submit_urls(urls):
    """提交 URL 列表到 IndexNow API"""
    if not urls:
        print('没有要提交的 URL。')
        return

    payload = {
        "host": HOST,
        "key": API_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }

    print('即将提交的 URL 地址:', payload)  # 打印即将提交的 URL 地址

    try:
        response = requests.post('https://api.indexnow.org/indexnow', json=payload, headers=HEADERS)
        response.raise_for_status()  # 检查请求是否成功
        result = response.json()
        print('成功提交的 URL:', result)
    except requests.RequestException as e:
        print(f'提交失败，错误信息: {e}')
    except ValueError:
        print('返回的内容不是有效的 JSON 格式。')

    # 记录每个 URL 的状态
    for url in urls:
        print(f'提交的 URL: {url} 状态码: {response.status_code}')

def main():
    """主程序"""
    urls = fetch_sitemap_urls()
    submit_urls(urls)

if __name__ == '__main__':
    main()