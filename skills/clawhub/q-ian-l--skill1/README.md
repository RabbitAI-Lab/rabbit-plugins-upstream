# File Tidy · 文件整理助手

纯本地文件整理 CLI。零第三方依赖、跨平台（Windows / macOS / Linux）、无需任何 API Key。
所有移动 / 重命名 / 删除操作**默认仅预览**，加 `--apply` 才真正执行。

## 功能

| 子命令 | 作用 |
|--------|------|
| `organize` | 按扩展名（Images/Documents/…）或修改日期归类文件 |
| `rename`   | 批量加前缀 / 后缀 / 序号、转小写、空格改连字符 |
| `clean`    | 清理空目录、删除重复文件（按 sha256，保留首个） |
| `flatten`  | 把多层嵌套目录平铺成一层（重名自动加后缀） |
| `duplicates` | 仅列出重复文件，不删除 |

## 快速开始

```bash
# 预览：按类型归类下载目录
python3 file_tidy.py organize ~/Downloads --by ext

# 确认无误后真正执行
python3 file_tidy.py organize ~/Downloads --by ext --apply

# 批量重命名（加序号 + 前缀）
python3 file_tidy.py rename ~/Photos --prefix trip --sequence --apply

# 找出并删除重复文件
python3 file_tidy.py clean ~/Downloads --dupes --apply
```

`python3 file_tidy.py --help` 查看全部参数。

## 发布到 ClawHub

```bash
npm i -g clawhub
clawhub login
cd file-tidy
clawhub skill publish . --slug file-tidy --version 1.0.0
```

> slug 不可含 `clawhub-` 前缀、需 npm-safe。若 `file-tidy` 已被占用，改个名即可。

## 安全特性

- 破坏性操作默认 dry-run，必须显式 `--apply`
- 移动 / 重命名遇到同名自动追加 `(1)`/`(2)`，不静默覆盖
- 重复文件删除始终保留路径字典序最小者
- 纯本地运行，无网络请求、无密钥、不读取文件内容

## License

MIT-0（ClawHub 发布默认许可）。
