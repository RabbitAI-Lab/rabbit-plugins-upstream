---
name: password-gen
description: "安全密码生成器：强密码（含符号）、字母数字密码、数字 PIN、易记密码短语。纯本地生成，无网络依赖。"
homepage: ""
metadata:
  {
    "openclaw":
      {
        "emoji": "🔐",
        "install":
          [
            {
              "id": "coreutils",
              "kind": "apt",
              "formula": "coreutils",
              "bins": ["tr", "shuf"],
              "label": "Install coreutils",
            },
          ],
      },
  }
---

# password-gen.sh 安全密码生成器

本地生成高强度随机密码，**无需联网**，密码不会离开你的设备。

## 用法

```bash
password-gen.sh                    # 16位强密码（大小写+数字+符号）
password-gen.sh 20                 # 20位强密码
password-gen.sh --no-symbol 16     # 不含符号（字母+数字）
password-gen.sh --pin 6            # 6位数字 PIN
password-gen.sh --passphrase 4     # 4个单词的密码短语（易记难破）
password-gen.sh --help             # 帮助
```

## 特点

- 🔒 使用系统 `/dev/urandom` 真随机源
- 🔑 `--passphrase` 生成「dragon-apple-tiger」式密码短语，好记又安全
- 📱 `--pin` 适合手机锁屏、门禁密码
- ⚡ 纯本地生成，无网络传输，密码不外泄

## 安全提示

- 强密码建议 16 位以上
- 不同网站/账号使用不同密码
- 建议配合密码管理器使用
