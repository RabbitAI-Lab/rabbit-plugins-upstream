---
name: cue-enterprise-panorama
description: 用 Cue 一键穿透企业的工商、股权、财务与经营全维基本面——评估业务模式与合作适配性，挖掘供应链金融与产业债机会，产出可用于内部决策的尽调底稿。
description_zh: Cue 企业全景画像：一键穿透工商/股权/财务/经营全维度，产出尽调底稿。
version: 1.0.0
author: sensedeal
tags: [cue, enterprise-panorama, due-diligence, 企业尽调, 企业画像, 信贷尽调, 供应链金融]
---

# 企业全景画像

> 一键穿透企业的工商、股权、财务与经营全维基本面，评估业务模式与合作适配性、挖掘供应链金融与产业债机会，产出可用于内部决策的尽调底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟，复杂主体更久 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_BWILbV`，传入目标企业 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付尽调底稿，来源链接不可丢失 | 禁止概括、禁止去掉引用 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 授信前尽调 | 快速了解借款企业全貌，识别核心风险点 |
| 客户准入 | 判断企业是否满足合作准入标准 |
| 供应链金融 | 挖掘核心企业上下游的金融机会 |
| 同业对标 | 多家企业的全维度横向比较 |

## 核心能力

1. **工商与股权穿透** — 注册资本、股东结构、实控人、对外投资
2. **经营基本面** — 主营构成、客户/供应商集中度、员工规模
3. **财务健康度** — 营收利润趋势、负债率、现金流、偿债能力
4. **司法与合规** — 被执行、失信、行政处罚、环保安全
5. **产业债与供应链金融机会** — 产业链位置、结算方式、融资需求推断

## 试试这样问

- "帮我画一下比亚迪的企业全景画像"
- "宁德时代的供应链金融机会在哪里？"
- "这家公司的经营风险主要是什么？"
- "对比一下宁德时代和比亚迪的尽调要点"

## 输出形式

结构化尽调底稿：工商股权 → 经营分析 → 财务健康 → 司法合规 → 供应链金融机会 → 风险点 → 待核实缺口 → 来源链接。每个结论带公开出处。

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
  --query "比亚迪 企业全景画像：工商、股权、财务、经营、供应链金融机会" \
  --template-id template_BWILbV \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-BYD-panorama.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标企业名称，**必填**；可选加行业或关注维度 |
| `--template-id` | 固定为 `template_BWILbV` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='信贷尽调' for b in s.get('buddies',[]) if b.get('title')=='企业全景画像'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [国家企业信用信息公示系统](https://www.gsxt.gov.cn) | 工商登记 | 免费 |
| [企查查](https://www.qcc.com) | 企业信息、关联方 | 部分免费 |
| [中国裁判文书网](https://wenshu.court.gov.cn) | 司法涉诉 | 免费 |
| [巨潮资讯网](https://www.cninfo.com.cn) | 上市公司公告 | 免费 |

## 输出示例

[查看完整报告](https://cuecue.cn/share/Phkgv0o_)

## FAQ

**Q: 和正式尽调报告有什么区别？**
A: 本报告基于公开数据，是预尽调底稿，不是替代正式尽调。私有数据（银行流水/合同/内部报表）不在覆盖范围。

**Q: 覆盖非上市公司吗？**
A: 可以跑，但非上市主体公开信息少，报告会如实标注证据缺口。
