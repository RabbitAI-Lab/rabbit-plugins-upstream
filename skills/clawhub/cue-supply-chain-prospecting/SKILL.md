---
name: cue-supply-chain-prospecting
description: 用 Cue 沿核心企业客户/供应商/招投标关系链，挖掘产业链上下游可拓展名单——给出每家切入点和可能的金融需求，助力对公客户经理精准拓客。
description_zh: Cue 产业链上下游拓客：沿客户/供应商/招投标关系链挖掘拓客名单，输出切入点和金融需求。
version: 1.0.0
author: sensedeal
tags: [cue, supply-chain, prospecting, business-development, 产业链, 拓客, 对公营销, 供应链金融]
---

# 产业链上下游拓客

> 从一家核心企业出发，顺着客户、供应商与招投标关系，挖出上下游可拓展名单，给出每家切入点和可能的金融需求。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_AKRtET`，传入核心企业 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付拓客清单 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 对公拓客 | 从一家核心客户出发，找到上下游可营销的企业名单 |
| 供应链金融 | 识别链上企业的融资需求和金融切入点 |
| 客户经理展业 | 拿着名单出门拜访，每家有具体的切入角度 |
| 产业链地图 | 画出一家企业的客户-供应商关系网 |

## 核心能力

1. **客户关系挖掘** — 从招投标、购销数据中提取客户名单
2. **供应商关系挖掘** — 从采购公告、工商数据中提取供应商名单
3. **切入点分析** — 每家企业的金融需求推断（开户/结算/授信/发债等）
4. **分层拓客清单** — 按切入优先级排列，每家有具体业务角度

## 试试这样问

- "以比亚迪为核心，挖掘它的上下游拓客名单"
- "这家龙头企业的供应商有哪些值得拓展？"
- "产业链上有哪些企业有授信需求？"
- "帮我找一下这个行业的上游供应商"

## 输出形式

结构化拓客清单：核心企业关系网 → 上下游企业名单 → 每家切入点 → 金融需求推断 → 分层优先级 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/Ml8DOQg5)

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

依赖：`git` + `python3` + `curl`（macOS 自带，Linux `apt install git python3 curl`）。Python 仅用标准库，无额外 pip 依赖。

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

Cue API Key：[cuecue.cn](https://cuecue.cn/hub/api-key) 注册获取。新账号送免费积分，每天再免费送 10 分。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "核心企业 产业链上下游拓客：客户关系、供应商关系、招投标关联、拓客切入点" \
  --template-id template_AKRtET \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-supply-chain-prospecting.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 核心企业名称，**必填**；可选加行业或区域限定 |
| `--template-id` | 固定为 `template_AKRtET` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='商机挖掘' for b in s.get('buddies',[]) if b.get('title')=='产业链上下游拓客'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [企查查](https://www.qcc.com) | 企业供应链、客户信息 | 部分免费 |
| [天眼查](https://www.tianyancha.com) | 企业关联关系 | 部分免费 |
| [东方财富行业](https://data.eastmoney.com) | 产业链上市公司 | 免费 |
| [各行业招投标平台] | 采购中标公告 | 免费 |
