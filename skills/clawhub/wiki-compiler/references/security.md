# 安全准则

> 任何破坏性操作前必读。任何不可逆操作必须先备份 + 用户确认 + 操作日志。

## 1. 破坏性操作清单

| 操作 | API | 风险 | 保护级别 |
|------|-----|------|:--------:|
| 删除笔记 | `delete_note` | 不可逆，内容永久丢失 | 🔴 极高 |
| 删除标签 | `tag_delete` | 所有关联自动解除 | 🔴 高 |
| 重命名标签 | `tag_rename` | 新名重复会**自动合并** | 🔴 高 |
| 移动文件 | `move_knowledge` | 标签数组可能清空 | 🟡 中 |
| 删除文件夹 | `create_folder` 反向 | 文件归属变根目录 | 🟡 中 |

## 2. 通用保护原则

1. **备份优先**：所有破坏性操作前必须先备份到本地
2. **三重确认门**：备份完成 + 内容已验证 + 用户显式确认
3. **操作日志**：每次破坏性操作后必须记录到 `/sandbox/workspace/logs/note_operations.log`
4. **优先用可逆方案**：`tag_remove` 优于 `tag_delete`，创建新笔记优于删除旧笔记
5. **影响范围可见**：执行前必须告诉用户"将影响 X 个文件/标签"

## 3. 删除笔记（`delete_note`）安全流程

> ⚠️ **不可逆操作**。一旦执行：
> - 笔记内容永久丢失，无法恢复
> - `note_id` 被永久废弃，新笔记会获得新的 ID
> - 如果 `note_id` 错误（如拼错、复制错误），可能误删其他笔记
> - 所有外部引用该 `note_id` 的链接都会失效

### 🚫 严禁直接执行

```bash
# ❌ 千万不要直接运行！必须先完成以下所有确认门
curl -s -X POST "https://ima.qq.com/openapi/note/v1/delete_note" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "<旧note_id>"}'
```

### ✅ 安全删除流程

**步骤 1：备份原笔记内容**

```bash
# 先把旧笔记完整导出到本地，作为永久备份
curl -s -X POST "https://ima.qq.com/openapi/note/v1/export_note" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id":"<旧note_id>","target_content_format":1}' | \
python3 -c "
import sys, json, urllib.request
d = json.load(sys.stdin)
if d['code'] == 0:
    content = d['data']['content']
    backup_path = '/sandbox/workspace/backups/notes/<旧note_id>_backup.md'
    with open(backup_path, 'w') as f: f.write(content)
    print(f'已备份到: {backup_path}')
"
```

**步骤 2：三重确认门**

执行前必须依次确认以下问题，**任何一个答案为"否"或"不确定"都禁止继续**：

- [ ] 确认 1：备份文件已成功保存到本地？
- [ ] 确认 2：新内容已经创建并验证完整（与原内容比对通过）？
- [ ] 确认 3：用户已**显式**确认删除（不是隐式同意）？
- [ ] 确认 4：`note_id` 已核对 3 次以上，无拼写错误？

**步骤 3：删除前最后一次预览**

```bash
# 先打印要删除的笔记信息，让用户最终确认
curl -s -X POST "https://ima.qq.com/openapi/note/v1/get_note_info" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id":"<旧note_id>"}' | python3 -m json.tool

# 用户必须明确回复"确认删除"才能继续
```

**步骤 4：执行删除（仅在所有确认门通过后）**

```bash
# 此时方可执行删除——但强烈建议先告知用户：
# "即将删除 note_id=XXX 的笔记'XXX'，是否继续？"
# 等待用户再次确认后再运行：

curl -s -X POST "https://ima.qq.com/openapi/note/v1/delete_note" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "<旧note_id>"}' | python3 -m json.tool

# 立即记录到操作日志
echo "$(date -Iseconds) | 删除笔记: <旧note_id> | 备份路径: <备份路径>" >> /sandbox/workspace/logs/note_operations.log
```

### 💡 推荐替代方案：保留旧笔记 + 创建新笔记

> **强烈推荐**：对绝大多数场景，**不要删除旧笔记**，而是：
> 1. 创建内容完全的新笔记（获得新的 `note_id`）
> 2. 在新笔记中标注"替代旧版 v1.X（`note_id=XXX`）"
> 3. 旧笔记保留作为历史版本，用户可自行在 IMA 客户端手动决定是否删除

这样：
- 避免误删风险
- 保留版本历史
- 用户拥有最终决定权

## 4. 删除标签（`tag_delete`）保护

> ⚠️ 删除后所有关联自动解除，不可恢复。

调用前必须：
1. 用 `tag_list(keyword=新名)` 检查新名是否存在
2. 用 `get_knowledge_list(tags=[标签])` 列出受影响文件数
3. 告知用户所有关联自动解除且不可恢复
4. **用户显式确认**

```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/tag_delete" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"knowledge_base_id": "<kb_id>", "tag_name": "<标签名>"}'
```

## 5. 重命名标签（`tag_rename`）保护

> ⚠️ 新名重复会**自动合并**到旧名——所有文件可能被打上意外标签。

调用前必须：
1. 用 `tag_list(keyword=新名)` 检查新名是否存在
2. 若存在，告知用户会"自动合并"并显式确认
3. 用 `get_knowledge_list` 列出受影响文件数
4. **用户显式确认**

```bash
curl -s -X POST "https://ima.qq.com/openapi/wiki/v1/tag_rename" \
  -H "ima-openapi-clientid: $IMA_OPENAPI_CLIENTID" \
  -H "ima-openapi-apikey: $IMA_OPENAPI_APIKEY" \
  -H "Content-Type: application/json" \
  -d '{"knowledge_base_id": "<kb_id>", "old_tag_name": "<旧名>", "new_tag_name": "<新名>"}'
```

## 6. 移动文件（`move_knowledge`）保护

详见 [folder-organization.md](folder-organization.md) 第 0.4 节。

关键保护：
- 移动前**必须备份标签**（`move` 会清空标签数组）
- 移动后**逐个重新打标**

## 7. 操作日志

所有破坏性操作后必须记录：

```bash
# 追加到操作日志
echo "$(date -Iseconds) | <操作类型>: <note_id 或 tag_name> | 标题: <标题> | 备份路径: <路径>" \
  >> /sandbox/workspace/logs/note_operations.log
```

**日志格式**：

```
时间戳 | 操作 | ID | 标题 | 备份路径
```

**目的**：建立可审计的操作记录，万一误删可追溯。
