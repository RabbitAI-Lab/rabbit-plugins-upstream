# 3.0记录与沟通输入

## 正式记录

UTF-8 JSON是唯一正式格式。`id`是跨设备UUID，修订使用独立UUID；`parents`指向同一记录的历史修订。`kind`为entity/event/feedback/judgment/task/summary/historical/configuration/source/conflict之一。其他公共字段：

- `title`、`body`：完整表述，UTF-8。
- `entity_ids`：关联对象ID，不用Notion页面ID或旧member编号作为身份。
- `source_refs`：来源记录ID；文本可附 `start_line`、`end_line`，从1开始，闭区间。
- `claim_kind`、`verification_status`：说明证据性质及核实状态，未知保持“未标注”。AI推断不能自动确认；转述不能自动当作事实。
- `time`：未知为null；已知保留 `original` 和 `precision`（unknown/year/quarter/month/day/range）。year/quarter/month不能有伪造的精确value；day/range须有有效value。年份存疑增加uncertain及note，正文保留原话。
- `status`：active/archived/sample/pending/done/confirmed-deleted/resolved。日常查询排除archived、sample、confirmed-deleted；可显式查询历史归档。
- `attributes`：对象类型、角色、别名、旧字段、任务期限或等待状态、来源字节哈希等类型相关信息。
- `created_at`、`updated_at`：记录创建/修订时间，与事件发生时间分开。

人物、公司、部门、项目均为entity，通过attributes.entity_type区分。真实角色、别名、评价维度使用entity属性或configuration记录；通用模板不保存真实配置。任务body保留明确动作，attributes记录commitment、owner、due、priority、waiting_reason等实际已知信息；状态变化形成新修订。

## 捕获输入示例

示例不含真实个人资料，不能直接作为真实记录写入。

```json
{
  "input_id": "chat-unique-id:turn-unique-id",
  "user_text": "本轮相关团队原话第一行\n第二行",
  "items": [
    {
      "key": "event-1",
      "kind": "event",
      "title": "本轮事件标题",
      "body": "保留范围和措辞的结构化内容",
      "claim_kind": "用户陈述",
      "verification_status": "未标注",
      "entity_ids": [],
      "source_span": [1, 2]
    }
  ],
  "key_conclusions": ["本轮确有保存价值的AI建议或推断"]
}
```

先按名字/别名查询并确认对象。新增对象可先 `record put` 创建，再在capture条目关联其ID；不按同名自动合并身份。新增独立记录不要求预先分配ID，程序生成UUID。

`input_id`、条目key与 `record put --operation-id` 在重试时保持稳定；同一幂等键内容变化会拒绝，需新键或明确修订。修订条目带id及expected_revision。纯补充用新记录并关联来源，禁止用整页全文覆盖旧记录。

关键结论只存有价值的最终结论，不复制冗长推理。key_conclusions自动标为AI推断、待确认。用户判断应明确claim_kind=用户判断，capture将其分类为judgment。

冲突先用record show读取双方variants，再让用户选择。`record resolve --conflict-id <ID> --revision <所选修订ID>` 明确采用其中一方；也可用 `--take local|remote`，此处local/remote指冲突形成时保存的两方，不是当前设备。记录已有后续修订时会拒绝旧冲突覆盖，需重新核对。

## 查看与修订

```sh
python3 <skill目录>/scripts/team-memory.py record query --text <关键词> --limit 8
python3 <skill目录>/scripts/team-memory.py record show --id <记录ID>
python3 <skill目录>/scripts/team-memory.py record source --id <来源ID>
python3 <skill目录>/scripts/team-memory.py record put --input <JSON文件> --expected-revision <当前修订ID> --operation-id <本次唯一操作ID>
```

query正文最多1600字符，`body_truncated=true`时按ID读取全文。默认最多12条，最大100条；日常不使用大范围全文读取。source仅用于明确追溯，二进制来源用标准包内的objects按哈希取回原始字节。
