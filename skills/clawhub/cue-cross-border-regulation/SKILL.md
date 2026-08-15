---
name: cue-cross-border-regulation
slug: cue-cross-border-regulation
displayName: 跨境法规调研
version: 1.0.0
description: >
  跨境法规调研 — 定向检索目标司法辖区法律法规原文与核心条款，提炼立法背景与适用边界，每个结论附原始出处可逐条回查。
  Triggers: 跨境法规、境外法规、外国法律、海外法规调研、欧盟法规、美国法律、GDPR、DMA、SEC规则、CFIUS、跨境合规、cross-border regulation、foreign law
license: MIT
metadata:
  source: cuecue.cn/playbook
  scene: "涉外法律"
  buddy: "跨境法规调研"
---

# 跨境法规调研

> 定向检索目标司法辖区法律法规原文与核心条款，提炼立法背景与适用边界，每个结论附原始出处可逐条回查。覆盖美国、欧盟、新加坡等主要法域。

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
| 出海产品合规 | 目标市场对产品（AI/电商/金融/医疗）的准入法规要求 |
| 数据隐私合规 | GDPR、CCPA、PDPA 等各国数据保护法的具体要求 |
| 出口管制研判 | EAR、ITAR、欧盟两用物项条例等管制法规的适用边界 |
| 外商投资审查 | CFIUS、FIRRMA、欧盟FDI审查机制的具体规定 |
| 跨境税务与转让定价 | 各国税法和转让定价规则的合规要点 |
| 劳动与雇佣合规 | 海外用工的劳动法、签证、社保要求 |

## 核心能力

1. **多法域法规检索** — 美国（USC/CFR）、欧盟（EUR-Lex）、新加坡（Singapore Statutes）
2. **核心条款解读** — 关键条款原文摘录 + 中文摘要
3. **立法背景梳理** — 法案出台背景、修订历史、配套指南
4. **适用边界研判** — 谁受管辖、什么行为触发、豁免条件
5. **逐条可溯源** — 每个结论附官方公报或法律数据库链接

## 试试这样问

- "欧盟 AI 法案的最新适用范围和合规要求"
- "美国对华半导体出口管制的现行法规梳理"
- "GDPR 对数据跨境传输的最新规定"
- "CFIUS 强制申报的触发条件和范围"
- "新加坡个人数据保护法（PDPA）的核心条款"
- "欧盟碳边境调节机制（CBAM）的法规框架"

## 输出形式

结构化报告：目标法域 → 适用法规列表 → 核心条款解读 → 立法背景 → 适用边界 → 合规要点 → 来源链接。中文报告，关键法条名和编号保留原文。

## 数据覆盖

美国USC/CFR、欧盟EUR-Lex、新加坡Singapore Statutes Online、各法域官方公报、监管机构发布指南。以公开数据为限。

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

Agent 会自动匹配「涉外法律」场景下的「跨境法规调研」搭子。固定写法：

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "<用户问题原话>" \
  --template-id <运行时的搭子 template_id> \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-cross-border-regulation.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 用户原话，不要改写 |
| `--template-id` | 从 `/api/playbook` 拉取当前可用的搭子 ID |
| `--output` | 落盘路径，格式 `~/cue-reports/日期-cross-border-regulation.md` |

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
你的 Agent ──→ Cue API（cuecue.cn）──→ EUR-Lex / USC / CFR / Singapore Statutes 等
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='涉外法律' for b in s.get('buddies',[]) if b.get('title')=='跨境法规调研'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| `RESULT empty` | 公开源无匹配 | 缩小范围（法域/领域），换关键词 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 缩窄关键词 → 单法域 → 确认该主题有公开法规
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
| [EUR-Lex](https://eur-lex.europa.eu) | 欧盟法规 | 免费 |
| [USC](https://uscode.house.gov) | 美国法典 | 免费 |
| [eCFR](https://www.ecfr.gov) | 美国联邦法规 | 免费 |
| [Singapore Statutes](https://sso.agc.gov.sg) | 新加坡法规 | 免费 |
| [国会官网](https://www.congress.gov) | 美国联邦立法动态 | 免费 |
| [各法域监管机构官网](https://www.usa.gov/federal-agencies) | 监管指南 | 免费 |

---

## FAQ

**Q: 和 Cue 网页端有什么区别？**
A: 在 Claude Code 里直接用自然语言触发，Agent 自动匹配搭子、确认、取报告，不用切网页。

**Q: 能查国内法规吗？**
A: 不能。本 Skill 专注境外法域，国内法规有另外的搭子（国内法规调研）。

**Q: 报告语言？**
A: 中文报告，法条名/编号保留原文附摘要。

**Q: 积分不够？**
A: 每天登录送 10 积分，单次约 3-8 积分。也可升级账号。

**Q: 查不到怎么办？**
A: 先跑健康检查。三个环节任一断了都会失败——见上方「自救指引」。

**Q: 结果可靠吗？**
A: 结论带来源链接可回查。注意：覆盖以美国/欧盟/新加坡等主要法域为主；非英语法域、地方性法规、未公开的监管口径覆盖不全；不构成法律意见。

---

> 本 Skill 基于 Cue 平台（cuecue.cn）「跨境法规调研」搭子。搭子模板由服务端动态维护。Skill 本身 MIT 开源。
