---
name: cue-domestic-regulation
slug: cue-domestic-regulation
displayName: 国内法规调研
version: 1.0.0
description: >
  国内法规调研 — 快速检索国内法律法规与行政令原文，梳理立法背景与合规要点，覆盖金融监管、工商登记、司法涉诉等多源公开数据。
  Triggers: 国内法规、法规调研、法律法规查询、金融监管、行政令、合规要点、立法背景、国内法规检索、domestic regulation
license: MIT
metadata:
  source: cuecue.cn/playbook
  scene: "法律合规"
  buddy: "国内法规调研"
---

# 国内法规调研

> 快速检索国内法律法规与行政令原文，梳理立法背景与合规要点，覆盖金融监管、工商登记、司法涉诉等多源公开数据。每个结论附原始出处可逐条回查。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 健康检查：Key / 服务 / 搭子三样全过再跑 | 禁止跳过 |
| 2 | 告知用户耗时 3-15 分钟 | 禁止中途取消 |
| 3 | 确认 credits，一条命令阻塞等待 | 禁止连发多条 |
| 4 | stdout `[cue-research] RESULT ok` = 完成 | 无 RESULT = 未完成 |
| 5 | 原样交付报告 + 告知落盘路径 | 禁止自行概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 新规速递 | 某领域最近出台了哪些新法规、修订了什么 |
| 合规自查 | 企业业务是否触碰某法规红线，有哪些合规要点 |
| 立法背景调研 | 某法规的立法背景、征求意见稿、配套文件 |
| 行业监管图谱 | 某行业（金融/医疗/数据/平台经济）的监管法规全貌 |
| 行政执法依据 | 某类行政处罚的法律依据、裁量标准 |

## 核心能力

1. **法规原文检索** — 法律、行政法规、部门规章、地方性法规、司法解释
2. **立法背景梳理** — 征求意见稿、修订说明、配套解读
3. **合规要点提炼** — 按行业和业务场景归纳合规义务
4. **跨文件关联** — 上位法→下位法→规范性文件→执法口径的层级关联
5. **逐条可溯源** — 每个结论附官方出处链接（全国人大、国务院、各部委官网）

## 试试这样问

- "数据出境安全评估的最新法规有哪些"
- "私募基金备案的监管要求和行政处罚依据"
- "个人信息保护法的配套规定和实施口径"
- "跨境电商零售进口的税收法规梳理"
- "医疗AI产品的注册审批法规体系"
- "平台经济反垄断的最新法规和执法动态"

## 输出形式

结构化报告：适用法规列表 → 核心条款解读 → 立法背景 → 合规要点 → 执法实践 → 来源链接。中文报告，法条名称和条款号保留原文编号。

## 数据覆盖

全国人大法律、国务院行政法规、各部委部门规章、地方性法规、司法解释、规范性文件、行政批复、监管问答。以公开数据为限。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：在 [cuecue.cn](https://cuecue.cn/api-key) 注册获取，新账号送 50 积分 + 每天 10 积分。写入 `~/.cue/config.json`：

```bash
mkdir -p ~/.cue
echo '{"api_key": "sk你的key"}' > ~/.cue/config.json
```

需要 `git` + `python3`（runner 仅用标准库，无额外依赖）。单次研究消耗约 3-8 credits。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

---

## 调用说明

Agent 会自动匹配「法律合规」场景下的「国内法规调研」搭子。固定写法：

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "<用户问题原话>" \
  --template-id <运行时的搭子 template_id> \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-domestic-regulation.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 用户原话，不要改写 |
| `--template-id` | 从 `/api/playbook` 拉取当前可用的搭子 ID |
| `--output` | 落盘路径，格式 `~/cue-reports/日期-domestic-regulation.md` |

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

本 Skill **不在本地执行检索**。流程是 Agent → Cue 服务端 → 外部数据源：

```
你的 Agent ──→ Cue API（cuecue.cn）──→ 全国人大 / 国务院 / 各部委官网等
```

| 环节 | 谁控制 | 出问题时 |
|------|--------|---------|
| API Key 鉴权 | 你 | 重新生成 Key，更新 config.json |
| Cue 服务端 | Cue 运维 | 等恢复，或走降级方案 |
| 外部数据源 | 公开网站 | Cue 用缓存兜底，标注"来源暂不可达" |

---

## 健康检查

跑研究前先验证三件事。一键诊断：

```bash
CUE_KEY=$(python3 -c "import json;print(json.load(open('$HOME/.cue/config.json'))['api_key'])" 2>/dev/null || echo "$CUE_API_KEY")
echo "=== 1/3 API Key ===" && [ -n "$CUE_KEY" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health" -H "Authorization: Bearer $CUE_KEY"
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='法律合规' for b in s.get('buddies',[]) if b.get('title')=='国内法规调研'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| `RESULT empty` | 公开源无匹配 | 缩小范围（领域/地域），换关键词 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 单领域 → 确认该主题有公开法规
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
| [国家法律法规数据库](https://flk.npc.gov.cn) | 法律、行政法规、地方性法规 | 免费 |
| [司法部](https://www.moj.gov.cn) | 行政法规、部门规章 | 免费 |
| [中国裁判文书网](https://wenshu.court.gov.cn) | 司法裁判文书 | 免费 |
| [巨潮资讯网](https://www.cninfo.com.cn) | 上市公司监管公告 | 免费 |
| [各部位官网](https://www.gov.cn) | 规范性文件、行政批复 | 免费 |

---

## FAQ

**Q: 和 Cue 网页端有什么区别？**
A: 在 Claude Code 里直接用自然语言触发，Agent 自动匹配搭子、确认、取报告，不用切网页。

**Q: 能查境外法规吗？**
A: 不能。本 Skill 专注国内法规，境外法规调研有另外的搭子（跨境法规调研）。

**Q: 报告语言？**
A: 中文报告，法条名称和编号保留原文格式。

**Q: 积分不够？**
A: 每天登录送 10 积分，单次约 3-8 积分。也可升级账号。

**Q: 查不到怎么办？**
A: 先跑健康检查。三个环节任一断了都会失败——见上方「自救指引」。

**Q: 结果可靠吗？**
A: 结论带来源链接可回查。注意：覆盖以全国性法规为主；地方性法规、内部文件、未公开的行政口径覆盖不全；不构成法律意见。

---

> 本 Skill 基于 Cue 平台（cuecue.cn）「国内法规调研」搭子。搭子模板由服务端动态维护。Skill 本身 MIT 开源。
