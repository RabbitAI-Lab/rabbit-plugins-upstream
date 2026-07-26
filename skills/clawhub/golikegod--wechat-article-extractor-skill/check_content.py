"""测试用 Python 通过代理抓取微信文章"""
import urllib.request
import ssl
import socket
import os

# 禁用 SSL 验证（如必要）
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://mp.weixin.qq.com/s/VSCJD-1ACSP7NWoV_CI2_Q'
out = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html'

# 模拟真实浏览器请求
req = urllib.request.Request(url, headers={
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Accept-Encoding': 'identity',  # 不压缩，避免 gzip 问题
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
})

# 设置默认超时
socket.setdefaulttimeout(45)

try:
    with urllib.request.urlopen(req, context=ctx, timeout=45) as r:
        data = r.read()
        print(f"Status: {r.status}")
        print(f"Length: {len(data)}")
        print(f"Headers: {dict(r.headers)}")
        
        # 写到文件
        with open(out, 'wb') as f:
            f.write(data)
        print(f"Saved to: {out}")
        
        # 简单搜索 js_content
        try:
            text = data.decode('utf-8', errors='replace')
            idx = text.find('js_content')
            if idx >= 0:
                print(f"js_content found at offset {idx}")
                print("---SAMPLE---")
                print(text[max(0,idx-50):idx+2000])
        except Exception as e:
            print(f"Decode error: {e}")
except Exception as e:
    print(f"ERROR: {type(e).__name__}: {e}")
