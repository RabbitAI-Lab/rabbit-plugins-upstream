# 黄金追踪 — 智能体操作手册

零第三方依赖的黄金价格追踪与分析技能。本文档是唯一操作真相源；违反「铁律」或「输出 schema」的分析会被 `analyze_check.py` 以非零退出码拒绝。

## 铁律（违反即拒绝）

1. 每个数据点 MUST 有来源 URL，不输出裸结论。
2. 每个判断 MUST 有因果链（"因为 X → 所以 Y → 对金价影响 Z"），并引用 ≥1 条真实抓取过的 URL。
3. 无数据 MUST 写 `no_data`，绝不编造、不补全。

## 安装

```bash
cp config.example.yaml config.yaml      # 生成配置（数据源/阈值/通知器全在此文件）
python3 scripts/verify.py init          # 初始化目录与 state.json
python3 scripts/verify.py check         # 一键自检，出现 [✗] 先修复
```

## 一次分析周期

1. 数据：`python3 scripts/fetch.py`（抓金价/汇率，自动校验/缓存/降级）
2. 准备（脚本接管，省 token）：`sh examples/analyze_prep.sh` = 采集可信新闻 + 生成分析骨架
3. 填 `key_factors`：读 `.cache/news_snippets.json`，在骨架里填 reasoning/impact/sources
4. 校验：`python3 scripts/analyze_check.py`（必须 exit 0）
5. 收尾（脚本接管）：`sh examples/analyze_finish.sh` = 校验 + 简报 + 通知

## 标准化输出 schema（logs/YYYY-MM-DD.yaml）

模板（与 `analyze_scaffold.py` 生成骨架一致，同日多次运行以 `---` 分隔多文档）：

```yaml
---
run_id: "20260723-1430"
timestamp: "2026-07-23T14:30+08:00"
price_data:
  gold:
    price_usd: 4090.09
    price_cny: 893.45
  fx:
    usd_cny: 6.78
    source: open.er-api.com
summary:
  focus: "一句话核心判断"
key_factors:
  - factor: "FOMC 即将召开会议"
    impact: "利空"
    reasoning: "因为 X → 所以 Y → 对金价影响 Z"
    sources:
      - "https://www.reuters.com/..."
sources:
  - "https://www.reuters.com/..."
  - "https://www.gold.org/..."
```

硬约束（违反则 `analyze_check.py` 拒绝）：
- 顶层字段 `run_id / timestamp / price_data / summary.focus / key_factors / sources` 齐全。
- `key_factors` 2–6 条，每条 `factor / impact / reasoning / sources` 四字段齐全。
- `impact` ∈ {利多, 利空, 偏多, 偏空, 中性, 多空交织}。
- `sources` ≥2 条、覆盖 ≥2 独立域名，且每条都已在 `fetch_log`（web_fetch 后立即 `python3 scripts/log_fetch.py <url> "<标题>"`）。
- `reasoning` / `summary.focus` 不含禁词（见 config `output.constraints.forbidden_phrases`）；无数据字段填 `no_data`。

## 提醒 / 通知 / 归档 / 调度

```bash
python3 scripts/alert_manager.py detect|list|pending|status|auto_resolve|cleanup|threshold
python3 scripts/notify.py send alerts|summary|retry|status|test [--dry-run]
python3 scripts/archive.py archive|find|history|cleanup|rebuild|summary|normalize
sh examples/run_cycle.sh                  # 一个周期：抓取 → 检测 → 发送
```

- 调度：不绑定调度器，周期跑 `run_cycle.sh`（见 examples/crontab.example、gold-tracker.service/.timer）。市场分析（第 2–4 步）不放进高频调度，由 Agent 关键时段触发。
- 提醒状态机 `pending → sent → acknowledged → resolved/dismissed`；通知失败保留 pending 自动重试；内容指纹去重。
- 所有写操作原子化（临时文件 + rename）。

## 排障

| 症状 | 处理 |
|---|---|
| fetch 失败 | 数据源不可用，自动降级缓存/上次状态 |
| analyze_check 报 source 未在 fetch_log | `log_fetch.py` 补记，或从 sources 删除 |
| analyze_check 报域名不足 / 禁用措辞 | 补抓不同域名 / 改写为因果链 |
| verify 报「提醒检测未运行」 | 按 examples/ 配置 cron/systemd 调度 |
| 归档索引损坏 / 状态损坏 | `archive.py rebuild` / `verify.py init` |
