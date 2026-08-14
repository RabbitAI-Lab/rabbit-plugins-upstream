---
name: cue-after-market-assistant
description: 用 Cue 在 10 分钟内自动生成深度市场复盘报告——穿透涨跌逻辑与资金流向，帮你快速看懂今天市场发生了什么、自己的持仓受了什么影响、明天该盯哪些信号。
description_zh: Cue 盘后超级助理：10分钟深度复盘，看懂涨跌原因、资金动向、持仓影响、次日关注。
version: 1.0.0
author: sensedeal
tags: [cue, after-market, market-recap, 盘后复盘, 市场复盘, 收盘分析, 个人投资, 持仓检视]
---

# 盘后超级助理

> 收盘后 10 分钟，自动帮你把今天的市场复盘清楚——大盘为什么涨跌、钱在往哪流、你的持仓受了什么影响、明天该看什么。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_GlU1Hm` | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付报告 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 每日收盘复盘 | 下班路上 10 分钟搞懂今天市场发生了什么 |
| 持仓影响分析 | 今天的大盘走势对你的持仓意味着什么 |
| 资金动向追踪 | 主力资金在买什么、卖什么，跟你手里的票有没有关系 |
| 投资笔记积累 | 每天存一份复盘，形成自己的市场判断框架 |
| 明日操作准备 | 今晚该做功课的方向，明天开盘前心里有数 |

## 核心能力

1. **大盘深度复盘** — 指数表现、涨跌分布、量价关系，一张表看懂全貌
2. **资金流向穿透** — 北向/主力/游资今天在干什么，板块偏好一目了然
3. **涨跌驱动拆解** — 今天涨跌背后的真实原因（政策/事件/财报/外部冲击）
4. **板块机会与风险** — 哪些板块在走强、哪些在退潮，有没有值得跟的信号
5. **次日关注清单** — 明天开盘前要盯的数据、事件和信号

## 试试这样问

- "帮我复盘今天的市场"
- "今天为什么涨/跌？对我的持仓有什么影响？"
- "今天的资金在买什么板块？要不要跟？"
- "明天有什么需要关注的事件？"
- "最近的市场主线是什么？还能持续吗？"

## 输出形式

结构化复盘报告：大盘速览 → 涨跌真实原因 → 资金在干什么 → 板块冷热 → 持仓相关性提示 → 次日关注清单 → 来源链接。每条判断都有出处，不凭空臆测。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn) 注册获取。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "今日A股盘后复盘：大盘涨跌原因、资金流向、板块表现、个人投资者角度关注机会与风险" \
  --template-id template_GlU1Hm \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-after-market.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 可指定关注的持仓板块或个股 |
| `--template-id` | 固定为 `template_GlU1Hm` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='财富投顾' for b in s.get('buddies',[]) if b.get('title')=='盘后超级助理'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [东方财富](https://www.eastmoney.com) | A股行情、资金流向 | 免费 |
| [同花顺](https://www.10jqka.com.cn) | 盘后数据、龙虎榜 | 免费 |
| [雪球](https://xueqiu.com) | 市场情绪、个股讨论 | 免费 |

## 输出示例

[查看完整报告](https://cuecue.cn/share/e48Yoz--t14FjIHxaxxLz)

## FAQ

**Q: 和看盘软件的盘后总结有什么区别？**
A: 看盘软件给的是"今天发生了什么"，Cue 给的是"为什么发生、跟我有什么关系、明天该怎么办"。每条判断都带公开出处。

**Q: 能针对我的持仓做分析吗？**
A: 可以在 `--query` 中列出你持有的板块或个股，报告会侧重分析这些标的所受的影响。

**Q: 最佳跑的时间？**
A: 建议下午 4:00-4:30 以后跑，此时数据汇总是最全的。如果忙，晚饭后跑也够用。

**Q: 每天都跑会重复吗？**
A: 每天市场驱动不同，报告内容跟着当天实际情况走。建议养成每日复盘的习惯。
