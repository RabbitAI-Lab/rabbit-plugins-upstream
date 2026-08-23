---
name: lanzou-downloader-0.0.5
description: 蓝奏云下载器 v0.0.5，纯本地解析零第三方服务。一键下载蓝奏云单文件与文件夹分享（自动识别文件夹短码、自动处理 JS 反爬与密码验证、文件夹列表自动翻页、--select 选择性下载、大文件断流自动重试）。当用户发送蓝奏云分享链接（lanzou* / lanzn.com 域名）并表达下载意图时触发。不适用于其他网盘平台（百度网盘/阿里云盘/微云等）。
---

# 蓝奏云下载器（lanzou-downloader）

## 概述

纯 Node.js 实现、零外部依赖、**纯本地解析（不调用任何第三方服务）** 的蓝奏云专用下载器。

## 路由决策

| URL 含 | 处理 |
|--------|------|
| `lanzou`（`lanzou*` / `lanzn.com`） | `scripts/download.js` |

## 安全与权限

本 skill 只做"下载蓝奏云"这一件事：

- **网络出访**：仅向蓝奏云域名（`lanzou*` / `lanzn.com` / `lanrar.com` / `webgetstore.com`，均为蓝奏云官方域名及 CDN）发起请求。**纯本地解析，不调用任何第三方服务**，分享链接与密码不会外发给任何第三方。
- **文件写入**：仅写入用户指定的输出路径与下载产物。不读取用户工作区其他文件，不收集 / 外发与本次下载无关的数据。
- **依赖**：零外部依赖（纯 Node.js 内置模块），无需安装任何包。

---

## 用法

```bash
node scripts/download.js <蓝奏云链接> [输出文件路径] [密码] [--select 目标1,目标2]
```

- 密码可选，不提供时脚本自动检测是否需要
- 输出路径可选，默认保存到当前目录 + 页面提取的文件名
- **文件夹分享（b 开头短码）自动识别**：输出路径视为目录，逐个下载文件夹内所有文件

### --select 选择性下载

只下载指定的文件，支持：
- 文件名精确匹配：`--select "ima.plus-skill-v1.0.8.zip"`
- 通配符：`--select "分*.zip"`、`--select "*.pdf"`
- 多个目标逗号分隔：`--select "a.zip,b.zip"`

---

## 解析流程

1. **访问分享页** → 检测 JS 反爬（`arg1=`）→ 执行反爬脚本计算 `acw_sc__v2` cookie 后重试
2. **文件夹分享**（分享页含 `filemoreajax`、短码形如 `b00XXXXXXX`）→ `filemoreajax.php` 提交密码获取文件列表（自动翻页，每页 50 个，跳过推广条目）→ 逐文件走单文件解析 → 流式下载
3. **单文件 + 密码**（页面含 `passwddiv`）→ 提取 fid/kdns/sign → POST 提交密码获取直链
4. **单文件无密码** → 提取 iframe 入口 → 请求 iframe 页（**带反爬自动重试**）→ 提取 ajaxdata/wp_sign → **ajax 接口路径从 iframe JS 动态提取** → POST 获取真实直链
5. **流式下载**（自动跟随重定向；重定向后清除 Referer 防 CDN 防盗链断流；Content-Length 完整性校验 + 断流自动重试 3 次）

### 已知机制（重要）

- **蓝奏云分享只含单层文件，不含子文件夹**（子文件夹需单独生成分享链接）；列表中的 `t==1` 条目是蓝奏云推广/广告内容，自动跳过
- 文件夹列表参数 t/k 由页面 JS 动态生成，脚本自动提取；缺失时列表会返回 `zt=4` 为空

---

## 示例

```
用户：https://wwapw.lanzouu.com/xxxxx 下这个
→ node .../scripts/download.js "https://wwapw.lanzouu.com/xxxxx"

用户：https://wwapw.lanzouu.com/xxxxx 密码:1234
→ node .../scripts/download.js "https://wwapw.lanzouu.com/xxxxx" "" "1234"

用户：https://wwapw.lanzouu.com/b00XXXXXXX（文件夹）密码:1234 下载整个目录
→ node .../scripts/download.js "https://wwapw.lanzouu.com/b00XXXXXXX" "/下载目录" "1234"
   → 自动识别文件夹 → 共 6 个文件 → 逐个下载 ✅

用户：https://wwapw.lanzouu.com/b00XXXXXXX 密码:1234 只要 分5.zip 和 分4.zip
→ node .../scripts/download.js "https://wwapw.lanzouu.com/b00XXXXXXX" "/下载目录" "1234" --select "分5.zip,分4.zip"

用户：https://wwapw.lanzouu.com/b00XXXXXXX 密码:1234 只要 ima.plus-skill-v1.0.8.zip
→ node .../scripts/download.js "https://wwapw.lanzouu.com/b00XXXXXXX" "/下载目录" "1234" --select "ima.plus-skill-v1.0.8.zip"
```

---

## 不支持的平台

本 skill 仅覆盖蓝奏云。百度网盘、阿里云盘、微云、115 等其他网盘不在范围内，告知用户无法处理。
