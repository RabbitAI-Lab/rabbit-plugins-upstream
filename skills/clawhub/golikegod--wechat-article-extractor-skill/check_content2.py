"""通过 http.client 直接抓取，禁用 keepalive 让 server 尽快断开"""
import http.client
import ssl
import socket
import os

# 禁用 SSL 验证
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

host = 'mp.weixin.qq.com'
path = '/s/VSCJD-1ACSP7NWoV_CI2_Q'
out = r'C:\Users\ZWB2016\.openclaw\workspace\skills\wechat-article-extractor-skill\raw.html'

conn = http.client.HTTPSConnection(host, 443, context=ctx, timeout=60)
try:
    conn.request('GET', path, headers={
        'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
        'Accept-Encoding': 'identity',
        'Connection': 'close',  # 不复用连接
        'Upgrade-Insecure-Requests': '1',
    })
    resp = conn.getresponse()
    print(f"Status: {resp.status} {resp.reason}")
    print(f"Headers: {dict(resp.getheaders())}")
    
    # 循环读取直到服务器关闭连接
    data = b''
    while True:
        try:
            chunk = resp.read(65536)
        except Exception as e:
            print(f"Read interrupted: {e}")
            break
        if not chunk:
            break
        data += chunk
        if len(data) > 5_000_000:  # 5MB 上限
            print(f"Hit 5MB cap, stopping")
            break
    
    print(f"Got {len(data)} bytes")
    
    with open(out, 'wb') as f:
        f.write(data)
    print(f"Saved to: {out}")
    
    text = data.decode('utf-8', errors='replace')
    idx = text.find('id="js_content"')
    print(f"id=js_content at: {idx}")
    if idx > 0:
        print("---SAMPLE 3000 chars around js_content---")
        print(text[max(0,idx-50):idx+3000])
finally:
    conn.close()
