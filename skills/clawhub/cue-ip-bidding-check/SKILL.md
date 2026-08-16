---
name: cue-ip-bidding-check
description: 用 Cue 整合企业专利、软著、商标、资质许可、招投标与融资记录——判断公开可见的技术能力与商业落地证据，产出可复核的硬实力证据底稿。
description_zh: Cue 知识产权资质与招投标尽调：整合专利/软著/商标/资质许可/招投标/融资记录，产出硬实力证据底稿。
version: 1.0.0
author: sensedeal
tags: [cue, ip-check, bidding, due-diligence, 知识产权, 招投标, 资质尽调, 硬实力尽调]
---

# 知识产权资质与招投标尽调

> 整合专利、软著、商标、资质许可、招投标与融资记录，判断企业公开可见的技术能力与商业落地证据，产出可复核的硬实力证据底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_Sze2NG`，传入目标企业 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付底稿，来源链接不可丢失 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 投标准入核查 | 投标前核实对方声称的资质、专利与业绩是否属实 |
| 技术尽调 | 判断标的企业的技术能力是否有公开证据支撑 |
| 商业落地评估 | 从招投标和融资记录看企业的商业化兑现能力 |
| 供应商准入 | 核查供应商的资质许可和硬实力是否达标 |

## 核心能力

1. **知识产权全景** — 专利（发明/实用新型/外观）、软著、商标的完整清单与法律状态
2. **资质许可核查** — 行业资质、经营许可、认证证书的核实与有效期追踪
3. **招投标记录** — 全周期中标/落标记录，识别核心客户与渠道依赖
4. **融资记录** — 融资轮次、投资方、估值变化，判断资本市场认可度
5. **硬实力综合研判** — 技术能力 + 商业落地 + 资本市场认可，三维交叉验证

## 试试这样问

- "尽调一下科大讯飞的技术硬实力"
- "这家投标方的专利和资质是否属实？"
- "目标公司的招投标中标率和融资历史"
- "评估一下这家AI公司的商业落地证据"

## 输出形式

结构化硬实力底稿：知识产权清单 → 资质许可 → 招投标分析 → 融资记录 → 技术能力研判 → 商业落地证据 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/buddy-template-063fa4f79b2c)

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
  --query "目标企业 知识产权资质与招投标尽调：专利、软著、商标、资质许可、招投标、融资记录" \
  --template-id template_Sze2NG \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-ip-bidding-check.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标企业名称，**必填** |
| `--template-id` | 固定为 `template_Sze2NG` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='深度核查' for b in s.get('buddies',[]) if b.get('title')=='工商与知识产权核查'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [国家知识产权局](https://www.cnipa.gov.cn) | 专利、商标查询 | 免费 |
| [中国版权保护中心](https://www.ccopyright.com.cn) | 著作权登记 | 免费 |
| [中国裁判文书网](https://wenshu.court.gov.cn) | 知识产权判例 | 免费 |
| [天眼查](https://www.tianyancha.com) | 企业知识产权列表 | 部分免费 |
