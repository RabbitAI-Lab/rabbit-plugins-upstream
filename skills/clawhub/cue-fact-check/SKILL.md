---
name: cue-fact-check
description: 用 Cue 穿透待核查资讯的表层表述——通过独立信源交叉验证与底层数据复核，精准识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。
description_zh: Cue 事实核查：多源交叉验证，识别时间错位/数据偏差/误导信息，产出原文对照与纠偏证据。
version: 1.0.0
author: sensedeal
tags: [cue, fact-check, verification, cross-validation, 事实核查, 交叉验证, 信息纠偏, 深度核查]
---

# 事实核查

> 穿透待核查资讯的表层表述，通过独立信源交叉验证与底层数据复核，精准识别时间错位、数据偏差及误导性信息，产出包含原文对照与纠偏证据的结构化事实核查报告。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_uoJDCg`，传入待核查内容 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付核查报告，纠偏证据不可丢失 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 研报数据核查 | 券商研报引用的数据是否真实、有无断章取义 |
| 新闻真实性验证 | 热点新闻中的数据、时间、主体是否准确 |
| 尽调信息复核 | 标的方提供的数据和公开数据是否一致 |
| 舆情纠偏 | 市场传言中哪些是真、哪些是误导 |

## 核心能力

1. **时间错位识别** — 旧数据当新数据、时间线前后矛盾
2. **数据偏差核查** — 引用的数字与原始来源是否一致
3. **误导性表述拆解** — 识别选择性呈现、口径变换等误导手法
4. **多源交叉验证** — 至少 2 个独立信源互相印证
5. **原文对照** — 待核查原文 vs 纠偏证据 逐条并排

## 试试这样问

- "核查一下这篇研报里的数据是否准确"
- "这条新闻里的数字是真的吗？"
- "对方提供的经营数据和公开数据对得上吗？"
- "这个市场传言有没有事实依据？"

## 输出形式

结构化核查报告：待核查原文 → 逐条核查结论（属实/偏差/无法核实） → 纠偏证据 → 独立信源对照 → 偏差分析 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/680abf29664d)

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
  --query "待核查内容 事实核查：原文对照、数据复核、多源交叉验证、时间线核实" \
  --template-id template_uoJDCg \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-fact-check.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 待核查的原文/链接/描述，**必填**；越具体越好 |
| `--template-id` | 固定为 `template_uoJDCg` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='深度核查' for b in s.get('buddies',[]) if b.get('title')=='事实核查'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [国家企业信用信息公示系统](https://www.gsxt.gov.cn) | 企业工商信息 | 免费 |
| [中国裁判文书网](https://wenshu.court.gov.cn) | 司法信息 | 免费 |
| [天眼查](https://www.tianyancha.com) | 企业信息核查 | 部分免费 |
| [百度](https://www.baidu.com) | 公开信息交叉验证 | 免费 |
