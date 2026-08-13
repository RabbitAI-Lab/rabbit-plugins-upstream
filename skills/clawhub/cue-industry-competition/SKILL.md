---
name: cue-industry-competition
description: 用 Cue 穿透目标行业的景气周期、竞争格局与产业链地位——识别集中度、龙头壁垒与供需/政策拐点，研判当前所处周期位置与投资机会窗口，产出可支撑配置决策的行业研判底稿。
description_zh: Cue 行业景气与竞争格局研判：穿透景气周期/竞争格局/产业链地位，识别拐点与投资机会窗口。
version: 1.0.0
author: sensedeal
tags: [cue, industry-analysis, competitive-landscape, cycle-timing, 行业景气, 竞争格局, 产业链分析, 周期研判]
---

# 行业景气与竞争格局研判

> 穿透目标行业的景气周期、竞争格局与产业链地位，识别集中度、龙头壁垒与供需/政策拐点，研判当前所处周期位置与投资机会窗口，产出可支撑配置决策的行业研判底稿。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_qcPkH8`，传入目标行业 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付研判底稿 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 行业配置决策 | 判断行业当前是否值得配置、处于周期哪个位置 |
| 拐点研判 | 识别供需拐点、政策拐点、技术拐点 |
| 竞争格局评估 | 看清龙头壁垒、集中度趋势、替代威胁 |
| 产业链地位分析 | 判断目标公司在产业链中的议价能力和利润分配 |

## 核心能力

1. **景气周期定位** — 量价/库存/产能利用率/利润率等指标定位当前周期阶段
2. **竞争格局穿透** — CR5/CR10 集中度、龙头壁垒来源、份额趋势
3. **供需拐点识别** — 产能投放节奏、需求增速变化、库存周期位置
4. **政策催化研判** — 产业政策、环保约束、准入放松对格局的影响
5. **投资窗口判断** — 结合周期位置与估值分位，研判机会窗口

## 试试这样问

- "光伏行业目前处于景气周期的什么位置？"
- "半导体设备的竞争格局和投资机会"
- "新能源汽车产业链的供需拐点到了吗？"
- "医药外包行业还有配置价值吗？"

## 输出形式

结构化研判底稿：景气周期定位 → 竞争格局 → 供需分析 → 政策催化 → 产业链地位 → 投资窗口研判 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/RWtYmuF_)

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
  --query "目标行业 景气周期与竞争格局研判：景气定位、集中度、供需拐点、投资窗口" \
  --template-id template_qcPkH8 \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-industry-competition.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 目标行业，**必填**；可选加时间窗口或关注维度 |
| `--template-id` | 固定为 `template_qcPkH8` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='行业研究' for b in s.get('buddies',[]) if b.get('title')=='行业景气与竞争格局研判'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [国家统计局](https://www.stats.gov.cn) | 行业经济数据 | 免费 |
| [行业协会官网] | 行业统计、标准 | 免费 |
| [东方财富行业](https://data.eastmoney.com) | 行业板块数据 | 免费 |
| [艾瑞咨询](https://www.iresearch.cn) | 行业竞争分析 | 部分免费 |
