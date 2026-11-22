# 元简题库维护工具

本目录是源码仓库维护者使用的来源更新与题库候选流水线，不进入 npm 发布包。
普通用户的元简分析、模拟面试、导出和自检均不包含网络抓取能力。

## 边界

- 只允许 `https://` 来源。
- 抓取只保存 HTTP 状态、内容长度、ETag、Last-Modified 和 SHA-256，不保存网页正文。
- 跨 host 重定向、非 2xx、超时、超限或证书失败均受控失败。
- 来源变化只生成候选，不直接修改正式 `data/`。
- 题目新增、修改或退役必须经过人工复核和完整契约校验。

## 标准流程

### 1. 抓取来源快照

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py sources fetch \
  --source-id owasp-top10-2025 \
  --out snapshots-2026-11-24
```

抓取全部 active 来源：

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py sources fetch --all --out snapshots-2026-11-24
```

可用参数：

- `--timeout`：单来源超时秒数，默认 15。
- `--max-bytes`：单来源响应上限，默认 2 MiB。
- `--today`：覆盖抓取日期，便于测试和回放。

### 2. 离线比较来源

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py sources check \
  --snapshots snapshots-2026-11-24 \
  --out source-candidate \
  --format json
```

首次内容指纹标记为 `baseline`；后续变化标记为 `updated`；仅检查日期变化标记为
`verified`。内容指纹和检查日期都未变化时不创建空候选。

### 3. 生成题库候选

创建补丁文件：

```json
{
  "add": [],
  "modify": [
    {
      "question_id": "sec-soc-knowledge-001",
      "set": {
        "prompt": "请说明告警分诊的输入、证据和停止条件。"
      }
    }
  ],
  "retire": []
}
```

生成候选：

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py bank propose \
  --source-candidate source-candidate \
  --patches question-patches.json \
  --target-version 0.2.1 \
  --out bank-candidate \
  --format json
```

`bank propose` 会重算被修改题目的 `content_hash`，但不会修改正式题库。
候选目录包含 `manifest.json`、差异、来源候选、题库候选和复核清单。

### 4. 人工复核

复核备注写入独立文本文件，然后执行：

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py bank review \
  --candidate bank-candidate \
  --reviewer local-maintainer \
  --decision approve \
  --review-notes review-notes.md \
  --confirm facts,role,level,boundary,rights \
  --format json
```

批准候选必须同时确认：

- `facts`：来源事实；
- `role`：岗位族适配；
- `level`：职级适配；
- `boundary`：答案边界和安全表述；
- `rights`：来源许可、引用方式和允许使用范围。

缺少任一项时，`bank validate` 和 `bank apply` 都会拒绝。

### 5. 校验候选

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py bank validate \
  --candidate bank-candidate \
  --format json
```

校验在临时数据目录中完成，检查 15 个契约文件、162+ active 题目、来源有效性、
角色和职级、题干唯一性、内容哈希与候选哈希。正式数据保持不变。

### 6. 应用与回滚

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py bank apply \
  --candidate bank-candidate \
  --format json
```

应用前会在 `data/history/<snapshot-id>/` 保存当前
`source-registry.json`、`source-watch-state.json` 和 `question-bank.json`。
应用后重新运行契约校验；失败时恢复应用前文件。

```bash
python tools/resume_maintenance/yotta_resume_maintenance.py bank rollback \
  --snapshot <snapshot-id> \
  --format json
```

回滚前校验历史快照的大小和 SHA-256；被篡改的快照不能恢复。回滚后再次运行契约校验，
失败时恢复回滚前状态。

`data/history/` 只保留在本机，不进入 npm 发布包。

## 退出码

- `0`：成功。
- `2`：参数或复核决策无效。
- `3`：快照、候选或备注文件不存在。
- `5`：JSON、日期、版本或候选结构无效。
- `6`：15 文件契约校验失败。
- `7`：候选隔离、人工复核、哈希、应用或回滚闸门失败。

## 恢复原则

- 不手工编辑 `data/history/` 中的 manifest 或文件。
- 不使用未登记目录覆盖正式数据。
- 不把网页正文、登录态、Cookie 或候选人资料写入快照。
- 应用或回滚异常时先保留当前目录与错误输出，再排查，不重复执行破坏性操作。
