# API 速查

> IMA OpenAPI 完整参考。所有调用都依赖 `IMA_OPENAPI_CLIENTID` 和 `IMA_OPENAPI_APIKEY` 环境变量。

## 1. 环境变量配置

```bash
# 必需的环境变量
export IMA_OPENAPI_CLIENTID="你的ClientID"
export IMA_OPENAPI_APIKEY="你的APIKey"

# 或使用配置文件
mkdir -p ~/.config/ima
echo "你的ClientID" > ~/.config/ima/client_id
echo "你的APIKey" > ~/.config/ima/api_key
chmod 600 ~/.config/ima/*
```

## 2. 通用调用函数（Python）

```python
import urllib.request
import json

def ima_api(path, data=None):
    """IMA OpenAPI 通用调用函数"""
    headers = {
        "ima-openapi-clientid": "你的ClientID",
        "ima-openapi-apikey": "你的APIKey",
        "Content-Type": "application/json"
    }
    url = f"https://ima.qq.com/{path}"
    req = urllib.request.Request(
        url,
        data=json.dumps(data or {}).encode('utf-8'),
        headers=headers,
        method="POST"
    )
    with urllib.request.urlopen(req, timeout=15) as resp:
        return json.loads(resp.read().decode("utf-8"))
```

## 3. 常用 API 端点

| 功能 | 端点 | 关键参数 |
|------|------|---------|
| **获取知识库列表** | `openapi/wiki/v1/get_knowledge_list` | `knowledge_base_id`, `limit` |
| **搜索知识库** | `openapi/wiki/v1/search_knowledge_base` | `query`, `cursor`, `limit` |
| **获取媒体信息** | `openapi/wiki/v1/get_media_info` | `media_id`, `knowledge_base_id` |
| **导出媒体内容** | `openapi/wiki/v1/export_media_for_ima_sandbox` | `media_id` |
| **创建文件夹** | `openapi/wiki/v1/create_folder` | `knowledge_base_id`, `folder_name`, `parent_folder_id` |
| **移动文件** | `openapi/wiki/v1/move_knowledge` | `src_kb_id`, `dst_kb_id`, `dst_folder_id`, `infos` |
| **添加标签** | `openapi/wiki/v1/tag_add` | `kb_id`, `item_id`, `item_name`, `tag_name` |
| **移除标签** | `openapi/wiki/v1/tag_remove` | `kb_id`, `item_id`, `item_name`, `tag_name` |
| **列出标签** | `openapi/wiki/v1/tag_list` | `kb_id`, `cursor`, `limit` |
| **删除标签** | `openapi/wiki/v1/tag_delete` | `kb_id`, `tag_name` |
| **重命名标签** | `openapi/wiki/v1/tag_rename` | `kb_id`, `old_tag_name`, `new_tag_name` |
| **创建笔记** | `openapi/note/v1/import_doc` | `content_format`, `content`, `title` |
| **导出笔记** | `openapi/note/v1/export_note` | `note_id`, `target_content_format` |
| **删除笔记** | `openapi/note/v1/delete_note` | `note_id` |
| **列出笔记本** | `openapi/note/v1/list_notebooks` | - |
| **创建笔记本** | `openapi/note/v1/create_notebook` | `name` |
| **列出笔记** | `openapi/note/v1/list_notes` | `notebook_id`, `count` |

## 4. 错误代码参考

| code | 说明 | 解决方案 |
|------|------|---------|
| 0 | 成功 | - |
| 51 | 参数错误（如 `limit` 超出范围） | 检查参数值 |
| 220001 | 文件名称不匹配（`item_name` 未用完整标题） | 从 `get_knowledge_list` 取原标题 |
| 220004 | 无效的 `knowledge_base_id` | 检查 kb_id |
| 220030 | 无写权限（普通成员调用 `tag_add` 等写操作） | 联系知识库创建者加权限 |
| 404 | API 端点不存在 | 检查 path |

## 5. 关键 API 详解

### 5.1 `get_knowledge_list`

```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/get_knowledge_list" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"knowledge_base_id": "<kb_id>", "folder_id": "<folder_id>", "count": 50}'
```

| 参数 | 必填 | 说明 |
|------|:----:|------|
| `knowledge_base_id` | ✅ | 知识库 ID |
| `folder_id` | ❌ | 文件夹 ID（不传=根目录，返回所有项目含散落文件视图）|
| `count` / `limit` | ❌ | 返回数量（最大 50，超出需 cursor 分页）|
| `cursor` | ❌ | 分页游标 |
| `tags` | ❌ | 按标签筛选（数组）|

### 5.2 `move_knowledge`

```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/move_knowledge" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{
    "src_knowledge_base_id": "<kb_id>",
    "dst_knowledge_base_id": "<kb_id>",
    "dst_folder_id": "<target_folder_id>",
    "dst_folder_name": "<target_folder_name>",
    "infos": [{"media_id": "<file_media_id>"}]
  }'
```

| 参数 | 必填 | 说明 |
|------|:----:|------|
| `src_knowledge_base_id` | ✅ | 原知识库 ID |
| `dst_knowledge_base_id` | ✅ | 目标知识库 ID（同库移动时与 src 相同）|
| `dst_folder_id` | ❌ | 目标文件夹 ID（不传=根目录）|
| `dst_folder_name` | ❌ | 目标文件夹名称（二次校验）|
| `infos` | ✅ | 移动列表，每项含 `media_id`，**最多 10 个**|

**注意**：返回的 `data.move_results[media_id].ret_code` 表示单文件结果，需检查每个文件的 ret_code 而非顶层 code。

### 5.3 `tag_add` / `tag_remove`

**`item_name` 必须严格匹配**——使用 `get_knowledge_list` 返回的**完整标题**（含扩展名和括号内容）。简化标题会导致 `220001 文件名称不匹配` 错误。

```bash
# 添加标签
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/tag_add" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{
    "knowledge_base_id": "<kb_id>",
    "item_id": "<file_media_id>",
    "item_name": "<get_knowledge_list 返回的完整 title>",
    "tag_name": "<标签名>"
  }'

# 移除标签
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/tag_remove" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{
    "knowledge_base_id": "<kb_id>",
    "item_id": "<file_media_id>",
    "item_name": "<完整标题>",
    "tag_name": "<标签名>"
  }'
```

**特性**：
- 重复操作不报错（幂等）
- 文件夹不支持打标签（`media_type=99`）

### 5.4 `import_doc` 创建笔记

```bash
# 1. 构建请求 JSON
python3 -c "
import json
with open('guide_content.md', 'r') as f:
    content = f.read()
with open('note_request.json', 'w') as f:
    json.dump({
        'content_format': 1,
        'content': content,
        'title': '📖 主题导览：[主题名称]'
    }, f, ensure_ascii=False, indent=2)
"

# 2. 发送请求
curl -s -X POST "https://ima.qq.com/openapi/note/v1/import_doc" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d @note_request.json | python3 -m json.tool
# 返回: {"code": 0, "data": {"note_id": "xxx"}}
```

### 5.5 `export_note` 导出笔记

```bash
curl -s -X POST "https://ima.qq.com/openapi/note/v1/export_note" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id":"<note_id>","target_content_format":1}' | python3 -c "
import sys,json
d=json.load(sys.stdin)
if d['code']==0:
    print(d['data']['content'])
else:
    print(d)
"
```

### 5.6 `export_media_for_ima_sandbox` 获取永久 URL

```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/export_media_for_ima_sandbox" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"media_id": "<文件media_id>"}'
```

返回的 `data.media_content_url_info.url` 即为永久可跳转链接（仅 type 2/6 可用）。
