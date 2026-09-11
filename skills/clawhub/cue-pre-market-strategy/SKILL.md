---
slug: cue-pre-market-strategy
Name: 今日盘前机会
description: 每天开盘前 3 分钟，看懂今天 A 股的机会与风险——自动扫隔夜美股、政策、产业新闻，大白话讲清利好利空，排出今日最值得关注的方向清单。
description_zh: Cue 今日盘前机会：每天开盘前 3 分钟，扫隔夜大事，看懂今天 A 股机会与风险。
version: 1.0.0
author: sensedeal
tags: [cue, pre-market, trading-strategy, 今日盘前机会, 盘前机会, 盘前热点, 盘前掘金, 开盘前必看]
---

# 今日盘前机会

> 每天开盘前，花几分钟看懂隔夜发生了什么、今天 A 股哪些方向有机会、哪些要避开。不用熬夜盯盘，个人投资者也能轻松上手的盘前功课。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_qsweF9` | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付报告 | 禁止概括 |

## 适用场景

| 场景 | 帮到你什么 |
|------|-----------|
| 每天开盘前 | 几分钟看懂隔夜发生了什么，不用自己熬夜盯美股 |
| 今天关注什么方向 | 直接给你一份「今日机会清单」，哪些板块最可能有行情 |
| 提前避坑 | 隔夜利空会砸到哪些板块，提前知道，避免开盘踩雷 |
| 上班族 | 通勤路上几分钟看完，心中有数再决定今天动不动手 |

## 核心能力

1. **隔夜大事扫描** — 美股、大宗商品、政策、产业新闻，一网打尽
2. **翻译成大白话** — 每件事告诉你「对 A 股意味着什么、利好谁、利空谁」
3. **产业链顺藤摸瓜** — 上游一个消息，帮你推到中下游哪些公司受影响
4. **今日机会排序** — 按「确定性 × 爆发力」排出今天最值得看的方向

## 试试这样问

- "今天盘前有什么值得关注的？"
- "隔夜美股对今天 A 股有什么影响？"
- "今天哪些板块最可能有行情？"
- "开盘前我要避开哪些雷？"
- "帮我看看今天的盘前机会"

## 输出形式

一份「今日盘前机会清单」：隔夜大事 → 对 A 股意味着什么 → 利好/利空哪些板块 → 今日机会排序 → 风险提示 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/jwhaQSVxNzzWYOvHmt-jO)

---

## 环境要求

**三步装好（一次性，约 1 分钟）：**

```bash
# 1. 克隆 runner 到 ~/.cue/cue-skills
mkdir -p ~/.cue && git clone https://github.com/sensedeal/cue-skills ~/.cue/cue-skills
#   国内网络慢可换 Gitee 镜像：
#   git clone https://gitee.com/sensedeal/cue-skills ~/.cue/cue-skills

# 2. 写入 API Key（在 https://cuecue.cn/hub/api-key 创建后复制）
mkdir -p ~/.cue && echo '{"api_key":"sk..."}' > ~/.cue/config.json

# 3. 验证连通（返回 200 即成功）
curl -sS --max-time 10 "https://cuecue.cn/api/templates" \
  -H "Authorization: Bearer $(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])")"
```

依赖：`git` + `python3` + `curl`（macOS 自带，Linux `apt install git python3 curl`）。Python 仅用标准库，无额外 pip 依赖。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。新账号送 500 积分，每天再免费送 10 分。

- **积分赠送**：新注用户赠送 500 积分，邀请新用户再送 500 积分。
- **积分不足**：积分用完后，前往 [cuecue.cn/pay](https://cuecue.cn/pay) 页面进行订阅。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "今日盘前策略：隔夜全球事件→A股映射→产业链传导→爆发力主题" \
  --template-id template_qsweF9 \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-pre-market.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 可加行业偏好或风险关注点 |
| `--template-id` | 固定为 `template_qsweF9` |
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

**能力边界（先说清楚，别期望过高）：**

- 结果是**基于公开信息的推断**，不构成投资建议，也不保证涨跌。
- 报告质量与时效**取决于 Cue 服务端和外部数据源当天状态**——数据源波动时可能延迟或标注"来源暂不可达"。
- 不提供实时行情、资金流、买卖点；这些去券商 App。

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='短线盘面' for b in s.get('buddies',[]) if b.get('title')=='深度盘前策略内参'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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

### 输入不对时会怎样、怎么改

| 你的输入 | 结果 | 正确做法 |
|---------|------|---------|
| 空 query，或没写清时间/主题 | 结果空或跑偏 | 明确"今天/近几天的盘前"，说清关注方向 |
| 问实时行情、买卖点、K 线 | 无法回答 | 这类去券商 App；本工具只做隔夜事件→A股影响的推断 |
| 隔夜无大事，硬要"今天机会" | `RESULT empty` | 正常，说明当天无强信号，别硬凑 |
| 只写一个行业（如"半导体"） | 结果过窄 | 可直接用，也可加"及相关产业链"扩大覆盖面 |

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 确认该主题有公开数据
```

### 中断恢复与重试模型

> `research_run.py` 采用 fire-and-retrieve + replay 兜底：后台跑完自动取报告，取不到会自动回放 DB 拿完整报告（**不重复扣费**）。但**网络/鉴权类失败不会自动重试**——按上方决策树手动重试（最多 3 次）。
> 想要自动重试，可在外层包循环：
> ```bash
> for i in 1 2 3; do
>   python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
>     --query "今日盘前策略：隔夜全球事件→A股映射→产业链传导→爆发力主题" \
>     --template-id template_qsweF9 && break
>   sleep 300
> done
> ```

中断 ≠ 失败：中途超时/断网，用**相同命令**续接（Cue 从断点继续，不重复计费）；只有手动 cancel 才无法恢复。

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
| [东方财富](https://www.eastmoney.com) | A股盘前资讯 | 免费 |
| [财联社](https://www.cls.cn) | 隔夜要闻 | 免费 |
| [华尔街见闻](https://wallstreetcn.com) | 全球市场动态 | 免费 |
| [新浪财经](https://finance.sina.com.cn) | 盘前公告汇总 | 免费 |

---

## FAQ

**Q: 和投顾早盘简报、24h热点追踪有什么区别？**
A: 早盘简报是理财师发给客户的素材；热点追踪讲「发生了什么」；今日盘前机会更进一步，讲「对 A 股意味着什么、今天该关注哪些板块」，并给出机会排序。深度依次递增，这个最接近「今天该怎么看盘」。

**Q: 最佳跑的时间？**
A: 建议 8:00-8:30 跑，隔夜信息已充分沉淀，距开盘（9:30）还有充足决策时间。上班族通勤路上就能跑完。
