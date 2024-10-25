import requests
import xmltodict

# 配置参数
SITEMAP_URL = 'https://blog.darklotus.cn/sitemap.xml'# 替换为您要获取的sitemap地址
API_KEY = '5d3a8828f82f4137b955a7b77e3b542b'  # 替换为您的实际 API 密钥
HOST = 'darklotus.cn'  # 替换为您的主机名（主域名）
KEY_LOCATION = f'https://{HOST}/{API_KEY}.txt'  # 替换为您的 keyLocation

def fetch_sitemap_urls():
    """从 sitemap 中获取 URL 列表"""
    response = requests.get(SITEMAP_URL)
    print('SITEMAP_URL 响应状态码:', response.status_code)  # 打印 SITEMAP_URL 的状态码
    response.raise_for_status()  # 检查请求是否成功
    sitemap = xmltodict.parse(response.content)
    urls = [url['loc'] for url in sitemap['urlset']['url']]
    return urls

def submit_urls(urls):
    """提交 URL 列表到 IndexNow API"""
    payload = {
        "host": HOST,
        "key": API_KEY,
        "keyLocation": KEY_LOCATION,
        "urlList": urls
    }
    
    print('即将提交的URL地址:', payload)  # 打印即将提交的URL地址

    response = requests.post('https://api.indexnow.org/indexnow', json=payload)
    
    # 打印返回内容以供调试
    print('提交的URL响应状态码:', response.status_code)
    
    if response.status_code == 200:
        try:
            result = response.json()
            print('成功提交的 URL:', result)
        except ValueError:
            pass  # 忽略 JSON 格式错误
    else:
        print('提交错误:', response.status_code, response.text)

    # 记录每个 URL 的状态
    for url in urls:
        print(f'提交的 URL: {url} 状态码: {response.status_code}')

def main():
    """主程序"""
    urls = fetch_sitemap_urls()
    submit_urls(urls)

if __name__ == '__main__':
    main()