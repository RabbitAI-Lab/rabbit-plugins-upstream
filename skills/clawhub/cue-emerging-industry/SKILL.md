---
name: cue-emerging-industry
description: 用 Cue 一键梳理陌生赛道的行业天花板、竞争格局与核心商业模式——面对新兴产业快速建立认知框架，同时映射 IPO/并购中常见的合规风险与法律争议点。
description_zh: Cue 新兴产业研究：一键梳理赛道天花板/竞争格局/商业模式，映射IPO/并购合规风险。
version: 1.0.0
author: sensedeal
tags: [cue, emerging-industry, industry-research, business-model, 新兴产业, 赛道研究, 商业模式, 前沿产业]
---

# 新兴产业研究

> 面对陌生赛道一键梳理行业天花板、竞争格局与核心商业模式，映射 IPO/并购中常见的合规风险与法律争议点。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_BbE7-1`，传入赛道名称 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付研报 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 赛道研判 | 面对陌生新兴产业（如低空经济/具身智能/合成生物）快速建立认知 |
| 投资前研究 | 看清行业天花板、集中度和核心玩家的商业模式 |
| IPO 辅导 | 识别新兴产业企业在上市过程中常见的合规风险 |
| 并购尽调 | 跨界并购前了解标的所在行业的竞争格局与法律争议点 |

## 核心能力

1. **行业天花板测算** — 市场规模、增速、渗透率、政策天花板
2. **竞争格局拆解** — 集中度、龙头壁垒、新进入者威胁
3. **商业模式分析** — 核心盈利模式、价值链分布、关键成功要素
4. **合规风险映射** — IPO/并购中常见的合规风险与法律争议点预警

## 试试这样问

- "低空经济的市场规模和竞争格局如何？"
- "具身智能赛道的核心玩家和商业模式"
- "合成生物学的IPO合规风险有哪些？"
- "帮我梳理一下固态电池行业"

## 输出形式

结构化研报：赛道概览 → 天花板测算 → 竞争格局 → 商业模式 → 合规风险映射 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/770a002e0d43)

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
  --query "目标赛道 新兴产业研究：行业天花板、竞争格局、商业模式、合规风险" \
  --template-id template_BbE7-1 \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-emerging-industry.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 赛道/产业名称，**必填** |
| `--template-id` | 固定为 `template_BbE7-1` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='行业研究' for b in s.get('buddies',[]) if b.get('title')=='新兴产业研究'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [中国政府网](https://www.gov.cn) | 产业政策原文 | 免费 |
| [工信部](https://www.miit.gov.cn) | 行业数据、白皮书 | 免费 |
| [艾瑞咨询](https://www.iresearch.cn) | 行业研究报告 | 部分免费 |
| [36氪研究院](https://research.36kr.com) | 新兴行业分析 | 免费 |
