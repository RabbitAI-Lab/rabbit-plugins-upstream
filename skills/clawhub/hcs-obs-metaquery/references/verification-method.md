# 验证方法

## mock 模式验证

```bash
# 能力清单
python3 scripts/hcs-obs-metaquery.py capability-list --mock

# 标量检索
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket demo-assets --mock

# 标量检索（带过滤）
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket demo-assets --name-filter .png --min-size 1KB --mock

# 标量检索（按类型）
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket demo-assets --type image --mock

# 语义检索
python3 scripts/hcs-obs-metaquery.py semantic-search --bucket demo-assets --query landscape --mock

# AI 内容感知开通
python3 scripts/hcs-obs-metaquery.py enable-ai --bucket demo-assets --ai-type image --mock
python3 scripts/hcs-obs-metaquery.py enable-ai --bucket demo-assets --ai-type video --mock

# AI 内容感知查询
python3 scripts/hcs-obs-metaquery.py ai-status --bucket demo-assets --mock

# AI 内容感知关闭
python3 scripts/hcs-obs-metaquery.py disable-ai --bucket demo-assets --mock

# 桶统计
python3 scripts/hcs-obs-metaquery.py bucket-stats --bucket demo-assets --mock

# 桶列表
python3 scripts/hcs-obs-metaquery.py list-buckets --mock

# Markdown 输出
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket demo-assets --format md --mock
python3 scripts/hcs-obs-metaquery.py capability-list --format md --mock
```

## JSON 格式校验

```bash
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket demo-assets --mock | python3 -m json.tool
python3 scripts/hcs-obs-metaquery.py semantic-search --bucket demo-assets --query landscape --mock | python3 -m json.tool
python3 scripts/hcs-obs-metaquery.py capability-list --mock | python3 -m json.tool
```

## 退出码验证

```bash
# 缺少子命令 → 退出码 2
python3 scripts/hcs-obs-metaquery.py; echo "exit=$?"

# 非 mock 模式缺少 AK/SK → 退出码 3
python3 scripts/hcs-obs-metaquery.py list-buckets --region cn-north-4; echo "exit=$?"
```

## 真实环境验证

```bash
export HWCLOUD_AK=<your_ak>
export HWCLOUD_SK=<your_sk>
python3 scripts/hcs-obs-metaquery.py list-buckets --region cn-north-4
python3 scripts/hcs-obs-metaquery.py scalar-search --bucket <your-bucket> --region cn-north-4
python3 scripts/hcs-obs-metaquery.py bucket-stats --bucket <your-bucket> --region cn-north-4
```
