---
name: cue-insurance-policy-check
description: 用 Cue 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失——与同类产品客观对比，产出一份可向客户如实说明的条款理解底稿。
description_zh: Cue 保险产品条款核查：逐条核验保障/免责/等待期/费率/退保条款，产出可如实说明的理解底稿。
version: 1.0.0
author: sensedeal
tags: [cue, insurance, policy-check, product-analysis, 保险, 条款核查, 产品对比, 合规营销]
---

# 保险产品条款核查

> 逐条核验保险产品的保障责任、责任免除、等待期、费率与退保损失，并与同类产品客观对比，产出一份可向客户如实说明的条款理解底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_-P8x-f`，传入保险产品 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付条款理解底稿 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 产品上架核查 | 新产品上线前逐条核验条款是否存在歧义或销售风险 |
| 客户如实说明 | 对照条款整理可向客户如实陈述的要点与禁区 |
| 竞品对比 | 横向比对同类产品在保障/免责/费率上的差异 |
| 合规销售支撑 | 区分"可如实说明"与"不可承诺"的边界 |

## 核心能力

1. **保障责任核验** — 保什么、不保什么、具体触发条件
2. **责任免除逐条解读** — 免责条款的适用边界与常见误解
3. **费率与退保分析** — 现金价值、退保损失、费率对比
4. **同类产品客观对比** — 不带销售导向的横向比较
5. **合规边界标注** — 标注"可如实说明"和"不可承诺"的表述边界

## 试试这样问

- "核查一下这款重疾险的条款"
- "这两款医疗险的保障范围和免责条款对比"
- "这款产品的退保损失有多大？"
- "条款里有没有容易引起客户误解的地方？"

## 输出形式

结构化条款理解底稿：保障责任概览 → 免责条款逐条解读 → 费率与退保分析 → 同类产品对比 → 合规表述边界 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/1c3d67d8bc4c)

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：[cuecue.cn](https://cuecue.cn) 注册获取。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "目标保险产品 条款核查：保障责任、责任免除、等待期、费率、退保损失、同类对比" \
  --template-id template_-P8x-f \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-insurance-policy-check.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 保险产品名称，**必填**；可选加对比产品 |
| `--template-id` | 固定为 `template_-P8x-f` |
| `--output` | 落盘路径 |

---

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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='保险营销' for b in s.get('buddies',[]) if b.get('title')=='保险产品条款核查'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [银保监会](https://www.cbirc.gov.cn) | 保险监管规定 | 免费 |
| [中国保险行业协会](https://www.iachina.cn) | 保险条款范本 | 免费 |
| [各保险公司官网] | 产品条款原文 | 免费 |
