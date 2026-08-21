# 验收标准

## 功能验收

| 验收项 | 验证方法 | 预期结果 |
|--------|---------|---------|
| 能力清单 | `capability-list --mock` | 输出 10 项能力，退出码 0 |
| 标量检索 | `scalar-search --bucket demo-assets --mock` | 输出 5 个对象，退出码 0 |
| 标量检索（名称过滤） | `scalar-search --bucket demo-assets --name-filter .png --mock` | 仅返回含 .png 的对象 |
| 标量检索（大小过滤） | `scalar-search --bucket demo-assets --min-size 1KB --mock` | 仅返回 ≥1KB 的对象 |
| 标量检索（类型过滤） | `scalar-search --bucket demo-assets --type image --mock` | 仅返回 image 类型对象 |
| 语义检索 | `semantic-search --bucket demo-assets --query landscape --mock` | 返回匹配对象 + 分数 |
| AI 开通 | `enable-ai --bucket demo-assets --ai-type image --mock` | status=enabled |
| AI 查询 | `ai-status --bucket demo-assets --mock` | 输出 image/video 状态 |
| AI 关闭 | `disable-ai --bucket demo-assets --mock` | status=disabled |
| 桶统计 | `bucket-stats --bucket demo-assets --mock` | 输出对象数/总大小/存储类别 |
| 桶列表 | `list-buckets --mock` | 输出 3 个桶 |
| Markdown 输出 | `scalar-search --bucket demo-assets --format md --mock` | Markdown 表格 |
| JSON 格式合法 | `capability-list --mock \| python3 -m json.tool` | 无错误 |
| 缺少子命令 | `python3 hcs-obs-metaquery.py` | 退出码 2 |
| 缺少 AK/SK | 非 mock 模式无 AK/SK | 退出码 3 |

## 代码风格验收

| 验收项 | 预期 |
|--------|------|
| _load_credentials | 动态扫描 AK/SK（不依赖固定变量名） |
| _build_obs_client | 使用 ObsCredentials（非 BasicCredentials） |
| _attr 兼容函数 | 兼容 dict + SDK 对象 |
| MOCK_DATA | 含桶/对象/AI标签/AI配置 |
| capability_list | 列出 10 项能力 |
| 退出码 | 0/2/3/4 对应成功/参数错误/缺少认证/API 失败 |
| 子命令 | 10 个子命令（scalar-search / semantic-search / enable-ai / ai-status / disable-ai / create-bucket / upload-object / bucket-stats / list-buckets / capability-list） |
