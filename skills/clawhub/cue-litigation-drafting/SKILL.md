---
name: cue-litigation-drafting
slug: cue-litigation-drafting
displayName: 诉讼文书起草
version: 1.0.0
description: >
  诉讼文书起草 — 根据用户提供的案件事实与当事人立场，通过 Cue 服务端生成法律文书草稿（答辩状/质证意见/律师函），逐点附法条与类案依据。本技能调用 Cue API（cuecue.cn）完成远程检索与生成，不直接访问任何数据源。
  Triggers: 起草答辩状、起草质证意见、起草律师函、起草起诉状、起草上诉状、draft litigation document
license: MIT
metadata:
  source: cuecue.cn/playbook
  scene: "法律合规"
  buddy: "诉讼文书起草"
---

# 诉讼文书起草

> 把案件事实、当事人立场和上传的对方材料，起草成规范的诉讼文书草稿（答辩状 / 质证意见 / 律师函等），逐点附法条与类案依据，律师拿来直接改定稿——省去从空白页起草、逐条翻法规的时间。

## 重要声明

- **草稿非终稿**：输出为文书草稿，法条和类案参考已附，但须由执业律师审核、调整后定稿。不构成正式法律意见。
- **仅限公开信息**：法条和类案检索基于公开数据库，不涉及非公开案件信息。

## 使用流程

用户提供案件信息和文书需求后，本技能通过 Cue 搭子「诉讼文书起草」生成文书草稿。典型流程：确认需求和材料 → 调用 Cue 服务端 → 等待返回 → 交付草稿。预计耗时 3-15 分钟。

Agent 调用命令参见下方「调用说明」。

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 答辩状起草 | 收到起诉状，需要起草答辩意见和反驳理由 |
| 质证意见撰写 | 对对方证据的三性（真实性、合法性、关联性）逐项质证 |
| 律师函/法务函 | 向对方发送正式法律函件，主张权利或提出警告 |
| 起诉状/上诉状 | 梳理案件事实和法律依据，起草规范的起诉或上诉文书 |
| 代理词/辩护词 | 基于庭审情况和证据，起草开庭代理意见 |
| 证据清单整理 | 按证明目的分组编排证据，编制证据目录 |

## 核心能力

1. **多类型文书** — 起诉状、答辩状、上诉状、质证意见、律师函、代理词
2. **法条自动匹配** — 每个主张附现行有效法条依据（条款号 + 原文）
3. **类案支撑** — 引用类似案件的裁判规则加强论证
4. **证据编排** — 按证明目的分组，编制证据目录与证明力说明
5. **规范格式** — 符合法院或仲裁委文书格式要求

## 试试这样问

- "根据这个案件事实，起草一份答辩状"
- "帮我写一份针对对方证据的质证意见"
- "起草一份关于合同违约的律师函"
- "帮我整理这份证据清单，按证明目的分组"
- "根据仲裁申请书，写一份仲裁答辩书"
- "起草一份关于股权转让纠纷的起诉状"

## 输出形式

结构化文书草稿：文书标题 → 当事人信息 → 案件事实概述 → 主张/答辩要点（逐点附法条依据）→ 证据目录 → 类案参考 → 结论与请求。中文文书，法条引用格式符合法院要求。

## 数据覆盖

中国现行有效法律法规数据库、公开裁判文书、各法院文书格式规范。以公开数据为限。

---

## 环境要求

Runner 安装：`git clone https://github.com/sensedeal/cue-skills.git ~/.cue/cue-skills`（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：在 [cuecue.cn](https://cuecue.cn/api-key) 注册获取，新账号送 50 积分 + 每天 10 积分。写入 `~/.cue/config.json`：

```bash
mkdir -p ~/.cue
echo '{"api_key": "sk你的key"}' > ~/.cue/config.json
```

单次研究消耗约 3-8 credits。

---

## 调用说明

用户在 [cuecue.cn](https://cuecue.cn) 的「法律合规」场景下选择「诉讼文书起草」搭子即可使用。Agent 通过 Cue Skills runner 调用：

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "用户描述的案件信息和文书需求" \
  --template-id <从 /api/playbook 获取> \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-litigation-drafting.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 用户原始问题 |
| `--template-id` | 从 `/api/playbook` 获取搭子 ID |
| `--output` | 报告落盘路径 |

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

本 Skill **不在本地执行检索**。流程是 Agent → Cue 服务端 → 外部数据源：

```
你的 Agent ──→ Cue API（cuecue.cn）──→ 法规数据库 / 裁判文书网等
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
# 健康检查：验证 Key 和连接状态，不输出密钥原文
echo "=== 1/3 API Key ===" && [ -f "$HOME/.cue/config.json" ] && echo "已配置" || echo "未配置！"
echo "=== 2/3 Cue 服务 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/health"
echo "=== 3/3 搭子 ===" && echo "请 Agent 调用 /api/playbook 检查搭子可用性"
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
| `RESULT empty` | 输入信息不足以起草 | 补充案件事实、当事人立场和材料 |
| config.json 报错 | JSON 格式不对 | `{"api_key": "sk..."}` 无多余逗号 |

### 决策树

```
出问题？
├─ Key 报错 → 重新生成 → 更新 config.json → 重试
├─ 连不上 → curl /api/health 确认 → 检查 DNS/代理
├─ 搭子找不到 → curl /api/playbook → 等或用网页端
├─ 中途中断 → 相同 prompt 续接（不要删 ~/.cue/session/task）
└─ 结果空 → 补充案件细节 → 明确文书类型 → 确认有足够输入信息
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
| [中国裁判文书网](https://wenshu.court.gov.cn) | 参考文书格式和类案 | 免费 |
| [国家法律法规数据库](https://flk.npc.gov.cn) | 法条依据核实 | 免费 |
| [各法院诉讼服务网](https://ssfw.court.gov.cn) | 文书格式模板 | 免费 |
| [北大法宝](https://www.pkulaw.com) | 法规与案例检索 | 部分免费 |

---

## FAQ

**Q: 和 Cue 网页端有什么区别？**
A: 在 Claude Code 里直接用自然语言触发，Agent 自动匹配搭子、确认、取报告，不用切网页。可以上传对方材料作为输入。

**Q: 文书可以直接用吗？**
A: 文书是**草稿**，法条和类案参考已附，但需律师根据具体案情审核、调整后定稿。不构成正式法律意见。

**Q: 支持哪些文书类型？**
A: 起诉状、答辩状、上诉状、质证意见、律师函、代理词、证据目录等常见诉讼文书。

**Q: 报告语言？**
A: 中文文书，法条引用格式符合国内法院要求。

**Q: 积分不够？**
A: 每天登录送 10 积分，单次约 3-8 积分。也可升级账号。

**Q: 起草质量如何？**
A: 质量取决于输入的案件事实和材料的完整度。输入越详细，草稿越可用。法条和类案依据自动匹配但需律师核实。

---

> 本 Skill 基于 Cue 平台（cuecue.cn）「诉讼文书起草」搭子。搭子模板由服务端动态维护。Skill 本身 MIT 开源。
