---
name: mineru-extract
description: 当用户想要使用 MinerU 从 PDF 或图片文件中提取关键信息时触发。适用于"使用 MinerU"、"从 PDF 提取文本"、"文档关键信息提取"、"解析 PDF"、"解析图像"、"上传文件到 MinerU"等请求。
sources: https://mineru.net/apiManage/docs
---

# MinerU API 技能

MinerU 提供两种 API 用于文档关键信息提取。

## 安装

首次使用时，安装依赖：

```bash
pip3 install --break-system-packages requests python-dotenv
```

## 快速使用

总是输出在在用户当前的工作目录下

```bash
# 本地文件（自动选择可用 API）
python run_mineru.py document.pdf

# 自定义超时
python run_mineru.py document.pdf --timeout 600
```

## API 认证

在项目目录创建 `.env` 文件：

```bash
# .env
MINERU_API_KEY="your-api-key-here"
```

**不要将 .env 提交到版本控制！**

```bash
# .gitignore
.env
```

## 两种 API 模式

| 功能 | Precision Parse API | Agent 轻量解析 API |
|------|---------------------|-------------------|
| 认证 | Bearer Token (有效期90天) | 无需认证（IP 限频） |
| 文件大小 | ≤ 200MB | ≤ 10MB |
| 页数 | ≤ 200页 | ≤ 20页 |
| 支持格式 | PDF、图片、Doc、Docx、Ppt、PPTx、Xls、Xlsx、HTML | PDF、图片、Docx、PPTx、Xlsx |
| 输出格式 | ZIP 包（多格式） | 仅 Markdown |

**推荐**：优先使用 Agent 轻量解析 API 模式, 当文件大小、页数、格式不符合限制时，切换到 Precision Parse API 模式（功能更强）。当 API Key 无效或过期时，提示用户 。

## Precision Parse API v4

| 功能 | 方法 | 端点 |
|------|------|------|
| 批量文件上传链接申请 | POST | `https://mineru.net/api/v4/file-urls/batch` |
| 批量获取任务结果 | GET | `https://mineru.net/api/v4/extract-results/batch/{batch_id}` |

### 认证方式

```http
Authorization: Bearer {token}
```

### 文件限制

| 限制项 | 限制值 |
|--------|--------|
| 文件大小 | ≤ 200MB |
| 页数 | ≤ 200页 |
| 支持类型 | PDF、图片、Doc、Docx、Ppt、PPTx、Xls、Xlsx、HTML |



### Precision Parse API 错误码

| 错误码 | 说明                          | 解决建议                                                     |
| :----- | :---------------------------- | :----------------------------------------------------------- |
| A0202  | Token 错误                    | 检查 Token 是否正确，请检查是否有Bearer前缀 或者更换新 Token |
| A0211  | Token 过期                    | 更换新 Token                                                 |
| -500   | 传参错误                      | 请确保参数类型及Content-Type正确                             |
| -10001 | 服务异常                      | 请稍后再试                                                   |
| -10002 | 请求参数错误                  | 检查请求参数格式                                             |
| -60001 | 生成上传 URL 失败，请稍后再试 | 请稍后再试                                                   |
| -60002 | 获取匹配的文件格式失败        | 检测文件类型失败，请求的文件名及链接中带有正确的后缀名，且文件为 pdf,doc,docx,ppt,pptx,xls,xlsx,png,jp(e)g 中的一种 |
| -60003 | 文件读取失败                  | 请检查文件是否损坏并重新上传                                 |
| -60004 | 空文件                        | 请上传有效文件                                               |
| -60005 | 文件大小超出限制              | 检查文件大小，最大支持 200MB                                 |
| -60006 | 文件页数超过限制              | 请拆分文件后重试                                             |
| -60007 | 模型服务暂时不可用            | 请稍后重试或联系技术支持                                     |
| -60008 | 文件读取超时                  | 检查 URL 可访问                                              |
| -60009 | 任务提交队列已满              | 请稍后再试                                                   |
| -60010 | 解析失败                      | 请稍后再试                                                   |
| -60011 | 获取有效文件失败              | 请确保文件已上传                                             |
| -60012 | 找不到任务                    | 请确保task_id有效且未删除                                    |
| -60013 | 没有权限访问该任务            | 只能访问自己提交的任务                                       |
| -60014 | 删除运行中的任务              | 运行中的任务暂不支持删除                                     |
| -60015 | 文件转换失败                  | 可以手动转为pdf再上传                                        |
| -60016 | 文件转换失败                  | 文件转换为指定格式失败，可以尝试其他格式导出或重试           |
| -60017 | 重试次数达到上限              | 等后续模型升级后重试                                         |
| -60018 | 每日解析任务数量已达上限      | 明日再来                                                     |
| -60019 | html文件解析额度不足          | 明日再来                                                     |
| -60020 | 文件拆分失败                  | 请稍后重试                                                   |
| -60021 | 读取文件页数失败              | 请稍后重试                                                   |
| -60022 | 网页读取失败                  | 可能因网络问题或者限频导致读取失败，请稍后重试               |

### 输出

Precision Parse API 的输出是一个zip包，解压出多个文件，用户需要的是 `full.md`


## Agent 轻量解析 API

| 功能 | 方法 | 端点 |
|------|------|------|
| 文件上传解析 | POST | `https://mineru.net/api/v1/agent/parse/file` |
| URL 解析 | POST | `https://mineru.net/api/v1/agent/parse/url` |
| 查询结果 | GET | `https://mineru.net/api/v1/agent/parse/{task_id}` |

### 认证方式

无需认证，采用 IP 限频防滥用。超出限制返回 HTTP 429。

### 文件限制

| 限制项 | 限制值 |
|--------|--------|
| 文件大小 | ≤ 10MB |
| 页数 | ≤ 20页 |
| 支持格式 | PDF、图片、Docx、PPTx、Xlsx |

### 状态值

| 状态 | 说明 |
|------|------|
| waiting-file | 等待文件上传 |
| uploading | 文件上传中 |
| pending | 排队中 |
| running | 解析中 |
| done | 完成 |
| failed | 失败 |

### Agent 专属错误码
| 错误码 | 说明                             | Agent 应对策略                   |
| :----- | :------------------------------- | :------------------------------- |
| -30001 | 文件大小超出轻量接口限制（10MB） | 请使用标准 API 或拆分文件        |
| -30002 | 轻量接口不支持该文件类型         | 请上传 PDF/图片/Doc/PPT/Excel    |
| -30003 | 文件页数超出轻量接口限制         | 请使用标准 API 或指定 page_range |
| -30004 | 请求参数错误                     | 检查必填参数是否缺失             |



## 工作流程

**Precision Parse API：**
1. 申请上传链接 → `POST /api/v4/file-urls/batch`
2. PUT 上传文件到 OSS
3. 轮询结果 → `GET /api/v4/extract-results/batch/{batch_id}`
4. 将每个解析结果的`full.md`整合到一个 md 文件里，作为最终输出，用 markdown divider 分割结果。

**Agent 轻量解析 API：**
1. 获取上传 URL → `POST /api/v1/agent/parse/file`
2. PUT 上传文件到 OSS
3. 轮询结果 → `GET /api/v1/agent/parse/{task_id}`

## run_mineru.py 参数说明

```
用法: python run_mineru.py <file_path> [options]

位置参数:
  file_path              本地文件路径

选项:
  --timeout <秒>         超时时间（默认: 300）
```