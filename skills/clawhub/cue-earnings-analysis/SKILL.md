---
slug: cue-earnings-analysis
Name: 上市公司财报分析
description: 用 Cue 对上市公司最新财报做深度分析——从营收利润变动、业务驱动、利润含金量、产业链话语权到财务风险信号，产出一份带来源出处的业绩点评，帮个人投资者看懂一家公司的盈利情况，作为选股和股票分析的一环。
description_zh: Cue 上市公司财报分析：看懂营收利润/业务驱动/利润含金量/产业链话语权/财务风险，产出带溯源的业绩点评，选股基本面一环。
version: 1.0.0
author: sensedeal
tags: [cue, earnings-analysis, financial-analysis, equity-research, 财报分析, 业绩分析, 财报解读, 业绩点评, 上市公司, 选股, 基本面, 财务分析]
---

# 上市公司财报分析

> 围绕一家上市公司的最新财报，从营收利润变动、业务驱动、利润含金量、产业链话语权到财务风险信号，产出一份带来源出处的业绩点评，帮你看懂这家公司到底赚不赚钱、赚得实不实，作为选股和股票分析的一环。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_7qiAwz`，传入上市公司 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付业绩点评，来源链接不可丢失 | 禁止概括 |

## 适用范围与场景（先看这个，别用错了）

**可以查：**

| 维度 | 覆盖 |
|------|------|
| 市场 | A 股、港股、美股上市公司 |
| 财报类型 | 年报、半年报、季报（已披露的） |
| 分析深度 | 核心指标、业务驱动、利润含金量、产业链话语权、财务风险 |

**适用场景：**

| 场景 | 解决的问题 |
|------|-----------|
| 财报季看新财报 | 财报发布后快速看懂业绩好坏 |
| 持仓跟踪 | 定期跟踪持仓公司的财务变化 |
| 同业对比 | 对比同行业几家公司谁的财报更好 |
| 选股基本面筛查 | 作为选股流程里的一环，先看财报再决定深不深挖 |

**不能查：**

- 未上市 / 非上市公司的财报（非公开数据）
- 未到披露期的业绩预测或内幕信息
- 技术面、K 线、资金流（去「短线走势与技术面分析」）
- 实时行情和盘口数据

> 简单判断：**这家公司有公开披露的财报吗？** 有 → 用它；没有（未上市/未披露）→ 用不了。

### 快速判断：你是否需要这个 Skill？

```
你的需求是？
├─ 我想看懂某家上市公司最新财报好不好           → ✅ 用这个
├─ 我想对比两家公司谁的财务更健康               → ✅ 用这个
├─ 我想看某只票的技术面、资金流向、K线           → ❌ 用不了，去「短线走势与技术面分析」
├─ 我想看非上市公司的财务数据                   → ❌ 用不了，非公开信息
└─ 我想预测还没披露的财报数据                   → ❌ 用不了，不预测未来
```

## 核心能力

1. **核心指标变动** — 营收、净利润、毛利率、净利率、ROE 等关键数据，比去年同期增了还是减了
2. **业务驱动** — 业绩靠量升还是价涨，哪个业务线在真正赚钱
3. **利润含金量** — 账上利润是不是真金白银（现金流、应收账款质量），识别纸面利润
4. **产业链话语权** — 预收款/应收款/应付账款周转，判断对上下游的议价能力
5. **财务风险信号** — 存货异常、商誉减值、有息负债变化，提前发现暴雷隐患

## 避坑指南（新手先看这几条）

- **别只看净利润**：净利润涨但现金流不涨，可能是"纸面利润"（应收账款堆出来的）
- **警惕一次性收益**：卖资产、政府补助推高的利润不可持续，要看扣非后
- **应收账款暴增**：收入可能是"白条"，回款风险高
- **商誉/存货异常**：商誉减值、存货激增常是暴雷前兆

## 试试这样问

- "分析一下比亚迪最新一季的财报"
- "宁德时代这个季度赚的钱实不实？"
- "对比一下宁德时代和比亚迪谁的财务更健康"
- "这家公司应收账款有没有问题，会不会暴雷？"

## 输出形式

结构化业绩点评：核心指标变动 → 业务驱动 → 利润含金量 → 产业链话语权 → 财务风险信号 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/FKeQR7E8)

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

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "目标公司 上市公司财报分析：核心指标、业务驱动、利润含金量、产业链话语权" \
  --template-id template_7qiAwz \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-earnings-analysis.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 上市公司名称，**必填**；可选加财报期次或关注维度 |
| `--template-id` | 固定为 `template_7qiAwz` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='财报深读' for b in s.get('buddies',[]) if b.get('title')=='上市公司财报分析'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [巨潮资讯网](https://www.cninfo.com.cn) | A股年报/季报原文 | 免费 |
| [东方财富财报](https://data.eastmoney.com) | 财报数据、财务指标 | 免费 |
| [SEC EDGAR](https://www.sec.gov/edgar) | 美股财报 | 免费 |

## FAQ

**Q: 和东方财富/同花顺的财报数据有什么区别？**
A: 数据网站给你原始数字；这个帮你解读——数字背后的业务驱动是什么、利润实不实、有没有暴雷隐患，并给出带来源的点评。

**Q: 公司财报还没披露，能查吗？**
A: 不能。只能分析已披露的财报；还没出的会提示无最新财报，改用最近一期已披露的。

**Q: 能分析港股、美股财报吗？**
A: 可以。港股走披露易、美股走 SEC EDGAR，A 股走巨潮资讯网。

**Q: "利润含金量"是什么意思？**
A: 看账上利润是不是真金白银——现金流是否匹配、应收账款有没有暴增。利润高但现金流差，可能是"纸面利润"。
