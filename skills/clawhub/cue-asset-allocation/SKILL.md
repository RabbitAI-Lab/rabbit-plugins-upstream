---
name: cue-asset-allocation
description: 用 Cue 一键生成月度大类资产配置报告——整合全球 CPI、利率、国内宏观及资金流向，从宏观逻辑推导至股/债/商配置比例，产出可交付客户的配置建议书。
description_zh: Cue 大类资产配置月报：整合全球宏观数据，一键生成股/债/商月度配置建议书。
version: 1.0.0
author: sensedeal
tags: [cue, asset-allocation, macro, portfolio, 资产配置, 大类资产, 宏观, 配置月报]
---

# 大类资产配置月报

> 宏观配置外脑。整合全球 CPI、利率、国内宏观及资金流向，从宏观逻辑推导至股/债/商配置比例，一键生成月度资产配置建议书。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_fkAFJt` | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付，告知落盘路径 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 月度配置决策 | 每月初系统性地审视大类资产配置方向 |
| 客户配置建议 | 产出可直接交付高净值客户的配置建议书 |
| 投委会材料 | 为投委会提供宏观逻辑与配置比例的参考底稿 |
| 组合再平衡 | 基于宏观变化判断是否需要调整现有配置 |

## 核心能力

1. **全球宏观扫描** — CPI、PMI、利率、汇率、资金流等关键指标
2. **国内政策与流动性** — 货币政策、财政政策、信贷数据
3. **股/债/商配置推导** — 从宏观逻辑到具体配置比例的完整推导链
4. **配置建议书** — 结构化输出，含逻辑、比例、风险提示

## 试试这样问

- "帮我生成这个月的大类资产配置月报"
- "当前宏观环境下股债怎么配？"
- "最新CPI数据出来后配置需要调整吗？"
- "出一份客户用的月度配置建议"

## 输出形式

结构化月报：全球宏观环境 → 国内政策流动性 → 股/债/商配置逻辑 → 比例建议 → 风险提示 → 来源链接。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn) 注册获取，`cue login` 写入。新账号送免费积分。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "本月大类资产配置分析：全球CPI、利率、国内宏观、资金流向 → 股债商配置建议" \
  --template-id template_fkAFJt \
  --output ~/cue-reports/$(date +%Y-%m)-asset-allocation.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 可选指定月份、偏好、约束 |
| `--template-id` | 固定为 `template_fkAFJt` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='财富投顾' for b in s.get('buddies',[]) if b.get('title')=='大类资产配置月报'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [东方财富](https://www.eastmoney.com) | A股/基金/债券行情 | 免费 |
| [天天基金](https://fund.eastmoney.com) | 基金数据 | 免费 |
| [中国债券信息网](https://www.chinabond.com.cn) | 债券收益率 | 免费 |
| [TradingView](https://www.tradingview.com) | 全球资产价格 | 免费版 |

## 输出示例

[查看完整报告](https://cuecue.cn/share/JJiW9tVCEK7Yq3AW0zDnw)

## FAQ

**Q: 每月什么时候跑？**
A: 建议每月初 CPI/PMI 发布后跑，数据最新鲜。也可随时 ad-hoc 跑。

**Q: 报告含具体产品推荐吗？**
A: 报告给配置方向和比例，不推荐具体基金/产品代码。
