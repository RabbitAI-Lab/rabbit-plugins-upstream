---
name: cue-stock-valuation
description: 用 Cue 对个股进行全周期估值分析——融合短线资金流向与中长线估值模型，短期看情绪博弈与支撑压力，中长期看业绩兑现与安全边际。
description_zh: Cue 个股估值与股价分析：短/中/长三周期融合分析，资金面+估值模型+业绩兑现。
version: 1.0.0
author: sensedeal
tags: [cue, stock-valuation, equity-analysis, 个股估值, 股价分析, 估值模型, 财务分析]
---

# 个股估值与股价分析

> 融合短线资金流向与中长线估值模型，全周期分析——短期看情绪博弈与支撑压力，中长期看业绩兑现与安全边际。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_8qNgr5`，传入目标股票 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付，来源链接不丢失 | 禁止概括/改数字 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 个股深度分析 | 从短中长三周期评估估值水平、业绩驱动与安全边际 |
| 持仓检视 | 定期审视持仓股的估值变化与安全边际 |
| 新股研究 | 快速了解一家公司的估值水平和市场定位 |
| 行业对比 | 同业公司的估值对比分析 |

## 核心能力

1. **短期情绪与博弈分析** — 资金流向、筹码分布、支撑压力位
2. **中期业绩展望** — 盈利预测、增长驱动、催化剂事件
3. **长期估值模型** — DCF/PE/PB 等多模型交叉验证
4. **安全边际判断** — 当前价格与内在价值的差距评估

## 试试这样问

- "帮我分析一下宁德时代的估值"
- "比亚迪现在贵不贵？"
- "茅台的中长期投资价值如何？"
- "对比一下宁德时代和比亚迪的估值"

## 输出形式

结构化报告：公司概况 → 短期资金面 → 中期业绩驱动 → 长期估值模型 → 安全边际 → 风险因素 → 来源链接。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`（macOS 自带，Linux `apt install git python3 curl`）。Python 仅用标准库，无额外 pip 依赖。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。新账号送免费积分，每天再免费送 10 分。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "宁德时代 估值与股价分析：短线资金面 + 中长线估值 + 安全边际" \
  --template-id template_8qNgr5 \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-CATL-valuation.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标股票 + 关注角度，**必填** |
| `--template-id` | 固定为 `template_8qNgr5` |
| `--output` | 落盘路径 |

---

## 格式转换

Cue 输出 Markdown。安装 pandoc 后可转换为 Word 或 PDF：

```bash
# .md → .docx（Word）
pandoc report.md -o report.docx

# .md → .pdf
pandoc report.md -o report.pdf --pdf-engine=xelatex
```

输出文件与输入同目录、同名、不同后缀。

### 依赖安装

| 目标格式 | 依赖 | macOS | Ubuntu |
|----------|------|-------|--------|
| Word (.docx) | pandoc | `brew install pandoc` | `sudo apt install pandoc` |
| PDF (.pdf) | pandoc + LaTeX | `brew install --cask basictex` | `sudo apt install texlive-xetex` |

---

## 架构说明

本 Skill **不在本地执行检索**。流程是 Agent → Cue API（cuecue.cn）→ 外部数据源。解析结果的质量和时效取决于 Cue 服务端和外部数据源的状态。

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 你 | 重新生成 Key，更新 ~/.cue/config.json |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='投资研究' for b in s.get('buddies',[]) if b.get('title')=='个股估值与股价分析'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
```

| 检查 | 预期 | 异常处理 |
|------|------|---------|
| API Key | `已配置` | [cuecue.cn/api-key](https://cuecue.cn/api-key) 重新生成 |
| 服务 | `{"status":"healthy"}` | 等 5 分钟重试 |
| 搭子 | `可用:>0个` | 等 1h 或网页端手动跑 |

---

## 自救指引

### 错误速查

| 现象 | 原因 | 怎么修 |
|------|------|--------|
| 401 / Key 无效 | Key 过期或写错 | 重新生成 Key，更新 `~/.cue/config.json` |
| 超时 >30s | 服务维护/过载 | 等 5 分钟，跑诊断；当天内重试 |
| 搭子不可用 | 临时下线 | 网页端直接跑，或等 1 小时 |
| 积分不足 | 余额 < 消耗 | 每天登录送 10 积分 |
| 中途中断 | 队列满/数据源波动 | **不换 prompt**，相同命令续接 |
| `RESULT empty` | 公开源无匹配 | 缩小范围，换关键词 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 确认该主题有公开数据
```

### 调度建议

| 时段 | 建议 |
|------|------|
| 工作日 9-18 | 正常使用 |
| 夜间/周末 | 可能有维护，跑前先诊断 |
| 新 Key | 必须先诊断确认生效 |
| 连续失败 | 停 15 分钟再试，不要反复重试 |

---

## 降级方案

Cue 长时间不可达时的手动替代渠道：

| 渠道 | 覆盖 | 费用 |
|------|------|------|
| [东方财富](https://www.eastmoney.com) | A股行情、财务数据 | 免费 |
| [同花顺](https://www.10jqka.com.cn) | 个股数据、技术指标 | 免费 |
| [雪球](https://xueqiu.com) | 估值讨论、机构观点 | 免费 |
| [TradingView](https://www.tradingview.com) | 图表分析 | 免费版 |

---

## 输出示例

[查看完整报告](https://cuecue.cn/share/NMJ36JGzIwOx8SPJXB_WR)

## FAQ

**Q: 能同时分析多只股票吗？**
A: 建议每只单独跑以获得最深度分析。可在 query 中指定对比需求。

**Q: 报告含目标价吗？**
A: 报告给出估值区间和安全边际判断，不下具体买卖建议。
