---
name: hsciq-mcp
description: HS Code Lookup for Chinese Products. Query customs codes, tariff rates, declaration elements, and regulatory requirements via HSCIQ MCP API. Create classification consultation requests with image upload for expert review.
license: MIT
tags:
  - HS Code Lookup for Chinese Products
  - Tariff Classification
  - Customs
  - Trade
  - China
  - MCP
env:
  HSCIQ_API_KEY:
    description: "HSCIQ API key for accessing the customs code lookup service"
    required: true
  HSCIQ_BASE_URL:
    description: "HSCIQ API base URL (default: https://www.hsciq.com)"
    required: false
    default: "https://www.hsciq.com"
credentials:
  - name: HSCIQ API Key
    description: "Free API key from https://www.hsciq.com"
    required: true
    url: https://www.hsciq.com
---

# ⚠️ 使用前必读：需要 API 密钥

**本技能需要 HSCIQ API 密钥才能正常工作。**

## 获取 API 密钥

1. 访问 [https://www.hsciq.com](https://www.hsciq.com)
2. 注册账号并登录
3. 在控制台申请 API 密钥
4. 将密钥配置到本地（见下方"配置"章节）

**没有 API 密钥将无法查询海关编码。**

---



# HSCIQ MCP - 海关编码查询服务

专业的中国商品海关编码查询与归类服务，基于 HSCIQ MCP API。

## 功能

- **search_code** - 按关键词搜索海关编码（支持中国/日本/美国）
- **get_code_detail** - 获取海关编码详情（税率、申报要素、监管条件等）。code 需为完整申报编码（纯数字）：CN 10 位、US 10 位 HTS、JP 9 位，可带点分隔符（如 8471.30.0000）；位数不足/超长会返回带引导的错误消息；不确定完整编码时先用 search_code 按名称检索确认
- **search_instance** - 按商品名称检索归类实例（输入具体商品名如"自行车"、"手机壳"，非描述性短语）
- **search_unified** - 统一搜索（CIQ 项目/危化品/港口信息）
- **create_guilei_form** - 创建 HS 归类咨询单（需上传至少 1 张产品图片，提交给平台专业归类师人工审核，可选 categoryId 指定行业分类）
- **get_guilei_form** - 获取归类咨询单详情（含字段对话、归类结论、修改历史）
- **list_my_guilei_forms** - 获取当前用户的归类咨询单分页列表
- **add_guilei_dialog_message** - 在归类单字段上创建新讨论或回复已有讨论
- **list_guilei_categories** - 获取可用的行业分类列表（用于创建归类咨询单时选择 categoryId）

## 触发条件

用户提到以下关键词时自动触发：
- "海关编码"、"HS 编码"、"税号"、"商品编码"
- "查询税率"、"申报要素"、"监管条件"
- "CIQ"、"危化品"、"港口代码"
- "归类实例"、"商品归类"
- "归类咨询"、"人工复核"、"提交审核"、"专家确认"、"帮我提交归类"
- "我的咨询单"、"咨询详情"、"咨询回复"、"归类结果"
- "行业分类"、"分类列表"、"categoryId"、"归类分类"

## 编码调用规则（重要）

- 调用 get_code_detail 前先核对编码位数：CN 10 位、US 10 位、JP 9 位（纯数字，点/空格会被自动去除）。
- 用户提供的编码位数不全时，**不要直接调用 get_code_detail**，应先 search_code 检索拿到完整编码。
- 编码超长（如 CN 13 位 CIQ 码）时截取前 10 位再调用；服务端错误消息会直接给出可重试的截取结果，按提示重试即可。

## 配置

配置文件位于 `~/.openclaw/workspace/hsciq-mcp-config.json`：
```json
{
  "baseUrl": "https://www.hsciq.com",
  "apiKey": "your_api_key",
  "authHeader": "X-API-Key"
}
```

**注意**：API Key 也可以通过环境变量设置：
```bash
export HSCIQ_API_KEY=your_api_key
export HSCIQ_BASE_URL=https://www.hsciq.com
```

## 命令

```bash
# 搜索海关编码
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js search-code --keywords "塑料软管" --country CN

# 获取编码详情
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js get-detail --code "3926909090" --country CN

# 搜索归类实例
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js search-instance --keywords "自行车" --country CN

# 统一搜索（CIQ/危化品/港口）
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js search-unified --keywords "食品" --type ciq

# 创建归类咨询单（AI 自动提交人工复核）
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js create-guilei-form \
  --productNameCn "智能手机壳" \
  --uses "手机保护" \
  --ingredients "硅胶" \
  --images ./front.jpg ./back.jpg

# 获取归类咨询单详情
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js get-guilei-form --formId "abc123..."

# 查看我的归类咨询单列表
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js list-my-guilei-forms --pageIndex 1 --pageSize 20

# 在归类单上发起讨论或回复
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js add-guilei-dialog-message \
  --formId "abc123..." \
  --fieldKey "ProductNameCn" \
  --content "请问这个产品的材质是什么？"

# 获取行业分类列表（用于创建归类咨询单时选择 categoryId）
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js list-guilei-categories

# 创建归类咨询单并指定行业分类
node ~/.openclaw/skills/hsciq-mcp/hsciq-client.js create-guilei-form \
  --productNameCn "智能手机壳" \
  --categoryId 5 \
  --uses "手机保护" \
  --images ./front.jpg
```

## 使用示例

### 示例 1: 查询商品的海关编码
```
用户：帮我查一下"塑料软管"的海关编码
→ 调用 search_code，返回编码列表和税率信息
```

### 示例 2: 获取编码详情
```
用户：3926909090 这个编码的税率是多少
→ 调用 get_code_detail，返回完整税率、申报要素、监管条件
```

### 示例 3: 搜索归类实例
```
用户：看看别人是怎么归类"蓝牙耳机"的
→ 调用 search_instance，输入商品名称关键词"蓝牙耳机"（非短语），返回历史归类案例
```

### 示例 4: AI 拿不准时提交人工复核
```
用户：帮我查一下这个产品的 HS 编码，我不太确定 AI 给的结果对不对
→ AI 在用 search_code 查询后，如果用户对结果有疑问
→ 调用 create_guilei_form，自动提交产品信息与图片，生成归类咨询单
→ 平台专业归类师审核后给出权威结论
```

### 示例 5: 查看归类咨询单结果
```
用户：我之前提交的归类咨询有结果了吗？
→ 调用 list_my_guilei_forms 获取用户的归类咨询单列表
→ 找到目标单后调用 get_guilei_form 获取详情（含归类结论、字段对话）
```

### 示例 6: 在归类单上追问
```
用户：之前在归类单上问过的问题，我想补充信息
→ 调用 add_guilei_dialog_message
→ 传入 formId + fieldKey + content，在指定字段上发起新讨论或回复已有讨论
```

## API 端点说明

本技能使用**标准 MCP 协议**（JSON-RPC over Stateless Streamable HTTP），统一端点：

| 端点 | 说明 |
|------|------|
| `POST https://www.hsciq.com/mcp/rpc` | 标准 MCP 协议端点（`initialize` / `tools/list` / `tools/call`） |

**请求要求**：
- 认证头：`X-API-Key: <key>` 或 `Authorization: Bearer <key>`
- 请求头：`Accept: application/json, text/event-stream`
- 响应为 SSE 格式（`text/event-stream`），取 `data:` 行的 JSON-RPC 结果
- Stateless 模式：每次请求独立，无需维持会话

**tools/call 调用格式**：
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "search_code",
    "arguments": {
      "keywords": "塑料软管",
      "country": "CN",
      "pageIndex": 1,
      "pageSize": 10
    }
  }
}
```

**响应格式**：成功结果在 `result.structuredContent.result`（结构化数据），`result.content[0].text` 为同数据的 JSON 字符串；业务错误时 `result.isError=true` 且 `content[0].text` 为错误描述。

### create_guilei_form 调用示例
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "create_guilei_form",
    "arguments": {
      "productNameCn": "智能手机壳",
      "productNameEn": "Smartphone Case",
      "categoryId": 5,
      "uses": "手机保护",
      "ingredients": "硅胶",
      "brand": "某品牌",
      "model": "X1",
      "images": [
        { "fileName": "front.jpg", "data": "base64编码的图片数据..." }
      ]
    }
  }
}
```

**图片要求**：**必填，至少 1 张**，最多 3 张，每张 ≤ 1MB，支持 JPG/PNG/GIF/WebP；未上传图片将创建失败。每人每天最多创建 5 次（可配置）。

**categoryId（可选）**：行业分类 ID，通过 `list_guilei_categories` 获取可用分类列表；不指定时由归类师判断。

### list_guilei_categories 调用示例
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list_guilei_categories",
    "arguments": {}
  }
}
```

返回可用的行业分类列表，如 `[{"id": 1, "name": "分类名称"}, ...]`，用于 `create_guilei_form` 的 `categoryId` 参数。

### get_guilei_form 调用示例
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "get_guilei_form",
    "arguments": { "formId": "00000000-0000-0000-0000-000000000001" }
  }
}
```

返回完整的归类咨询单详情，包含产品字段、字段对话、归类结论（如有）等信息。

### list_my_guilei_forms 调用示例
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "list_my_guilei_forms",
    "arguments": { "pageIndex": 1, "pageSize": 20 }
  }
}
```

返回当前用户的归类咨询单分页列表，包含表单状态、创建时间等摘要信息。

### add_guilei_dialog_message 调用示例
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "add_guilei_dialog_message",
    "arguments": {
      "formId": "00000000-0000-0000-0000-000000000001",
      "fieldKey": "ProductNameCn",
      "content": "这个产品的准确材质是什么？",
      "dialogId": null,
      "messageType": null
    }
  }
}
```

- `formId` / `fieldKey` / `content` 为必填
- `dialogId`：不为空时回复已有对话；为空时新建对话
- `messageType`：可选的消息类型

## API 文档

完整 API 说明：https://www.hsciq.com/MCP/Docs

## Python 客户端

也可以使用 Python 脚本直接调用：

```bash
# 搜索海关编码
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py search-code --keywords "塑料软管" --country CN

# 获取编码详情
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py get-detail --code "3926909090"

# 搜索归类实例
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py search-instance --keywords "自行车"

# 统一搜索
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py search-unified --keywords "食品" --type ciq

# 创建归类咨询单
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py create-guilei-form \
  --productNameCn "智能手机壳" --uses "手机保护" --ingredients "硅胶" \
  --images ./front.jpg ./back.jpg

# 获取归类咨询单详情
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py get-guilei-form --formId "abc123..."

# 查看归类咨询单列表
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py list-my-guilei-forms --pageIndex 1

# 归类单讨论
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py add-guilei-dialog-message \
  --formId "abc123..." --fieldKey "ProductNameCn" --content "追问内容"

# 获取行业分类列表（用于 create-guilei-form 的 categoryId）
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py list-guilei-categories

# 创建归类咨询单并指定行业分类
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py create-guilei-form \
  --productNameCn "智能手机壳" --categoryId 5 --uses "手机保护" --images ./front.jpg

# 列出可用工具
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py list-tools

# JSON 输出（便于程序处理）
python3 ~/.openclaw/skills/hsciq-mcp/hsciq_client.py search-code --keywords "软管" --json
```

### Python 代码集成

```python
from hsciq_client import HSCIQClient

client = HSCIQClient()

# 搜索编码
result = client.search_code("塑料软管", country="CN")
print(result)

# 获取详情
detail = client.get_code_detail("3926909090")
print(detail)

# 创建归类咨询（图片为文件路径，客户端自动 base64 编码）
result = client.create_guilei_form(
    productNameCn="智能手机壳",
    uses="手机保护",
    ingredients="硅胶",
    images=["./front.jpg", "./back.jpg"]
)
print(result)

# 获取归类咨询单详情
form = client.get_guilei_form("00000000-0000-0000-0000-000000000001")
print(form)

# 查看归类咨询单列表
forms = client.list_my_guilei_forms(pageIndex=1, pageSize=20)
print(forms)

# 在归类单上追问
reply = client.add_guilei_dialog_message(
    formId="00000000-0000-0000-0000-000000000001",
    fieldKey="ProductNameCn",
    content="请确认这个产品的材质"
)
print(reply)

# 获取行业分类列表
categories = client.list_guilei_categories()
print(categories)

# 创建归类咨询并指定行业分类
result = client.create_guilei_form(
    productNameCn="智能手机壳",
    categoryId=5,
    uses="手机保护",
    images=["./front.jpg"]
)
print(result)
```
