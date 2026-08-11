---
name: cue-person-background-check
description: 用 Cue 穿透人物的全生命周期工商与司法轨迹——剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的个人背调底稿。
description_zh: Cue 个人背调底稿：穿透人物工商/司法全生命周期轨迹，映射商业控制版图，产出IPO级背调底稿。
version: 1.0.0
author: sensedeal
tags: [cue, background-check, person-check, due-diligence, 个人背调, 人物核查, 高管尽调, IPO尽调]
---

# 个人背调底稿

> 穿透人物的全生命周期工商与司法轨迹，剥离当前在册与历史风险、映射其商业控制版图，产出可用于 IPO 或重大交易的背调底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_m4NxQy`，传入目标人物 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付背调底稿 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| IPO 董监高背调 | 上市前核查董监高的工商/司法/处罚记录 |
| 重大交易尽调 | 并购/投资前核查交易对手方的关键人物 |
| 合作方准入 | 核查潜在合作方的实控人和高管背景 |
| 候选人背调 | 高管候选人入职前的公开信息核查 |

## 核心能力

1. **工商轨迹穿透** — 历史任职、对外投资、关联企业网络
2. **司法风险剥离** — 区分当前在册风险与历史已解除风险
3. **商业版图映射** — 实控/参股/任职企业网络图谱
4. **行政处罚核查** — 失信、限高、被执行、行政处罚记录

## 试试这样问

- "帮我做一份张三的个人背调底稿"
- "这家公司实控人的商业版图和历史风险"
- "IPO 董监高背调需要核查哪些维度？"
- "核查一下这位候选人的公开司法记录"

## 输出形式

结构化背调底稿：个人身份核验 → 工商任职轨迹 → 对外投资版图 → 司法风险（当前/历史） → 行政处罚 → 关联企业图谱 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/UvXieGTT)

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

Cue API Key：[cuecue.cn](https://cuecue.cn) 注册获取。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "目标人物 个人背调底稿：工商任职、对外投资、司法风险、行政处罚、商业版图" \
  --template-id template_m4NxQy \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-person-check.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标人物姓名 + 已知关联企业（如有），**必填** |
| `--template-id` | 固定为 `template_m4NxQy` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='人物核查' for b in s.get('buddies',[]) if b.get('title')=='个人背调底稿'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [中国裁判文书网](https://wenshu.court.gov.cn) | 个人涉诉 | 免费 |
| [中国执行信息公开网](https://zxgk.court.gov.cn) | 失信被执行人 | 免费 |
| [国家企业信用信息公示系统](https://www.gsxt.gov.cn) | 任职企业 | 免费 |
| [证券业协会](https://www.sac.net.cn) | 从业人员资质 | 免费 |
