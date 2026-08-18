# yiigle_tracker — 中华医学期刊网 指南/共识/标准 定时追踪下载

基于 cn-med-oa 的 yiigle 逆向经验（复用 `cn_med_oa.py` 的检索/下载/节流能力），独立轻量的**指南追踪工具**：
定时扫描 yiigle 最新指南/共识/标准，**快照 diff 只报告新增**，儿科文献优先，best-effort 下载 PDF，有新增时推送飞书。

## 核心能力

| 能力 | 说明 |
|---|---|
| 关键词追踪 | `--keywords "指南,共识,标准"` 逐词扫描最新文献（docType 或标题含指南/共识/标准/规范/建议） |
| 期刊过滤 | `--journals "中华儿科杂志,中华小儿外科杂志"` 在关键词结果中按刊名过滤（⚠️ yiigle 的 JN: 查询语义是"关于该期刊的文章"，不可用于追踪该刊文献，故用结果过滤） |
| 快照 diff | 状态文件记录已见文献 ID，**首次运行只建基线，之后只报告新增**（幂等，可每日 cron） |
| 儿科优先 🧒 | 标题含 儿童/小儿/新生儿/婴幼儿/患儿/青少年/母乳/疫苗接种 等关键词 → 置顶 + 🧒 标记 |
| best-effort 下载 | 复用 yiigle_try_download；登录墙/验证码门槛**不硬闯** → artUrl 浏览器下载兜底 |
| 飞书通知 | `--notify`：有新增时推送到 hermes 飞书频道（复用 feishu-send 通道，凭证在 .82 `~/.hermes/.env`，无需配置） |
| 控频合规 | 检索/下载间隔 ≥3s（复用 cn_med_oa `_throttle`），不碰付费/登录墙 |

## 用法

```bash
# 首次运行：建立基线（不报告新增）
python scripts/yiigle_tracker.py --keywords "指南,共识,标准" --out-dir ./tracker_out

# 期刊追踪（儿科期刊示例）+ 每日 cron 增量报告
python scripts/yiigle_tracker.py --keywords "指南,共识,标准" \
    --journals "中华儿科杂志,中华小儿外科杂志,中华实用儿科临床杂志" \
    --max 20 --out-dir ./tracker_out --notify

# 只追踪不下载 PDF
python scripts/yiigle_tracker.py --keywords "共识" --no-download --out-dir ./tracker_out
```

### 定时任务（cron，每天 08:00）

```cron
0 8 * * * cd /path/to/cn-med-oa && python3 scripts/yiigle_tracker.py \
    --keywords "指南,共识,标准" \
    --journals "中华儿科杂志,中华小儿外科杂志,中华实用儿科临床杂志" \
    --max 20 --out-dir ./tracker_out --notify >> ./tracker_out/cron.log 2>&1
```

Windows 可用任务计划程序（schtasks）配置同命令。

## 输出

- `tracker_report.md`：每次运行的全量报告（新增清单 + 元数据 + 阅读链接 + 下载状态）
- `tracker_state.json`：追踪状态（已见文献 ID），**不要删除**，否则下次全量误报新增
- PDF 文件：best-effort 下载成功时落入 out-dir

## 覆盖边界（诚实声明）

- ✅ 覆盖：yiigle 检索可见的指南/共识/标准/规范/建议（CMA 系期刊 + 指南解读），含完整元数据 + artUrl 免费阅读
- 🔗 下载：PDF 有验证码/登录门槛时给 artUrl 浏览器下载（不硬闯）
- ⚠️ 新增检测依赖 yiigle 搜索结果集（每词最多翻 5 页 100 条），极早期未入索引的文献可能延迟 1 次扫描发现
- ⚠️ 期刊过滤基于结果刊名匹配，极少数刊名变体（如"中华炎性肠病杂志（中英文）"）需用全名或包含匹配

## 依赖

- `cn_med_oa.py`（同目录，复用 yiigle 检索/下载/节流）
- 飞书推送可选：需要 192.168.3.82 可达（hermes 飞书应用），失败不影响本地报告