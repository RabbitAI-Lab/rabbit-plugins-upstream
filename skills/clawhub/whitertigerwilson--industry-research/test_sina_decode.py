# -*- coding: utf-8 -*-
"""测试 Sina 复权接口能否解析"""
import requests, base64

url = 'https://finance.sina.com.cn/realstock/company/sh601899/hisdata/klc_kl.js?d=2026_6_29'
hdrs = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    'Referer': 'https://finance.sina.com.cn/',
}
r = requests.get(url, headers=hdrs, timeout=10)
print('HTTP:', r.status_code, 'bytes:', len(r.content))

text = r.text
start = text.find('"') + 1
end = text.rfind('"')
b64 = text[start:end]
print('base64 length:', len(b64))

decoded = base64.b64decode(b64)
print('decoded length:', len(decoded))
# Sina 用 GBK 解码
text_decoded = decoded.decode('gbk', errors='replace')
print('decoded head 500 chars:')
print(text_decoded[:500])