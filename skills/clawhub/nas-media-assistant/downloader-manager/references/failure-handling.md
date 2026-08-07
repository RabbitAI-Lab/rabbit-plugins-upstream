# downloader-manager/references/failure-handling.md · 失败码与处置策略

> **受众**：编排器 / Agent / 开发者。本文件承载 `download_failed` 事件的所有 `failure.code` 与建议动作。
> 完整技术方案见 `downloader-manager/references/design.md`。

---

## 一、失败码表

| code | 含义 | 建议动作 | 说明 |
| --- | --- | --- | --- |
| `DL_DEAD` | 死链（0 seeders / 卡死 / 慢速） | **换链** | 链接本身有问题,换一个重试 |
| `DL_AUTH` | 鉴权失败 | 检查凭据,不换链 | 配置问题,需人工介入 |
| `DL_DISK` | 空间不足 | 清理空间,不换链 | 配置问题,需人工介入 |
| `DL_BLOCKED` | 被屏蔽/封禁 | **换链 + 换客户端** | 链接被封,需换下载器 |
| `DL_HASH` | 哈希校验失败 | **换链** | 文件损坏,需换源 |
| `DL_NET` | 网络错误 | 重试同链（≤ 2 次） | 网络波动,同链可能恢复 |
| `DL_UNKNOWN` | 未知错误 | 回报用户 | 配置/环境问题,需人工介入 |

## 二、失败事件结构

```json
{
  "event": "download_failed",
  "job_id": "dl_20260731_abc123",
  "metadata": [{"media_type":"movie","title":"电影名","year":"2024","source":"tmdb"}],
  "failure": {"code": "DL_DEAD", "msg": "任务停滞 10 分钟无进度", "suggested_action": "switch_link"}
}
```

> - 失败事件同样回传 `metadata`：换链重试时可复用同一元数据（无需重查 media-lookup）
> - 终止条件：成功 / `retry_count >= 3` / 用户主动停止（不碰下载目录源文件）

## 三、换链闭环设计

采用**事件驱动**架构，downloader-manager 只输出结构化事件，不关心下游如何消费：

```
add(url, name)
  │
  ├─ monitor -> completed -> download_completed 事件（含 file_path + metadata）
  │                                       └─→ Agent 调 media-organizer 整理
  │
  └─ monitor -> failed   -> download_failed 事件（含 code + suggested_action）
                                       └─→ Agent 按 suggested_action 决策:
                                            switch_link: 回 media-search 取下一候选
                                            retry:       重试同链（≤ 2 次）
                                            report_user: 回报用户
```

## 四、失败类型分类

| 类别 | codes | Agent 动作 |
|---|---|---|
| **换链类** | `DL_DEAD` / `DL_HASH` / `DL_BLOCKED` | 回 `media-search` 取下一候选（最多 3 次） |
| **重试类** | `DL_NET` | 同链重试（≤ 2 次） |
| **人工类** | `DL_AUTH` / `DL_DISK` / `DL_UNKNOWN` | 回报用户,不换链 |
