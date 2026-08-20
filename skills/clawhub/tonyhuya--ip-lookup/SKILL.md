---
name: ip-lookup
description: "IP 地址归属地查询：国家/省份/城市/运营商/ASN/时区/坐标，支持本机公网 IP 与任意 IP。免费无 Key。"
homepage: https://ip.sb/
metadata:
  {
    "openclaw":
      {
        "emoji": "📍",
        "install":
          [
            {
              "id": "curl",
              "kind": "brew",
              "formula": "curl",
              "bins": ["curl"],
              "label": "Install curl",
            },
            {
              "id": "python3",
              "kind": "apt",
              "formula": "python3",
              "bins": ["python3"],
              "label": "Install python3",
            },
          ],
      },
  }
---

# ip-lookup.sh IP 归属地查询

查询 IP 地址的归属信息（国家/省份/城市/运营商/ASN/时区/坐标），
数据源为 **ip.sb**（免费、无需 Key），带 ipwho.is 备用通道。

## 用法

```bash
ip-lookup.sh                     # 查询本机公网 IP
ip-lookup.sh 114.114.114.114     # 查询指定 IP
ip-lookup.sh 8.8.8.8             # 查询 Google DNS
ip-lookup.sh 1.2.3.4 --json      # 输出原始 JSON（适合脚本）
ip-lookup.sh --help              # 帮助
```

## 输出内容

- 📍 IP 地址
- 🌍 国家/地区、🗺️ 省份、🏙️ 城市
- 🏢 运营商、🔢 ASN
- 🕐 时区、📍 坐标

## 说明

- 免费 API 有频率限制，高频查询请自备 Key 或换付费服务
- 运营商信息为粗略归属，不代表实际精确位置
