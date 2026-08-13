---
name: cue-earnings-analysis
description: 用 Cue 对上市公司最新财报做深度分析——从核心数据变动、业务驱动因子、利润含金量、产业链话语权与典型财务信号，产出一份带可回查出处的业绩点评，供二级投研在财报发布后快速消化业绩。
description_zh: Cue 上市公司财报分析：穿透核心数据/业务驱动/利润含金量/产业链话语权，产出带溯源的业绩点评。
version: 1.0.0
author: sensedeal
tags: [cue, earnings-analysis, financial-analysis, equity-research, 财报分析, 业绩点评, 上市公司, 二级投研]
---

# 上市公司财报分析

> 围绕指定上市公司最新一期财报，从核心数据变动、业务驱动因子、利润含金量、产业链话语权与典型财务信号，产出一份带可回查出处的业绩点评，供二级投研在财报发布后快速消化业绩。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_7qiAwz`，传入上市公司 | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付业绩点评，来源链接不可丢失 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 财报季快速消化 | 财报发布当天快速产出业绩点评 |
| 基本面跟踪 | 定期跟踪持仓公司的财务变化 |
| 同业对比 | 多家同行业公司财报的横向比较 |
| 投研底稿 | 为深度报告提供带来源的财务分析素材 |

## 核心能力

1. **核心数据变动** — 营收/利润/毛利率/净利率/ROE 等关键指标变动拆解
2. **业务驱动因子** — 量升还是价涨、哪个业务线在拉动
3. **利润含金量分析** — 非经常性损益、应收账款质量、现金流匹配
4. **产业链话语权** — 预收款/应收款/应付账款周转，判断上下游议价能力
5. **典型财务信号** — 存货异常、商誉减值风险、有息负债变化

## 试试这样问

- "分析一下比亚迪最新一季的财报"
- "宁德时代Q3的利润含金量如何？"
- "对比一下宁德时代和比亚迪的财务健康度"
- "这家公司的应收账款质量有没有问题？"

## 输出形式

结构化业绩点评：核心指标变动 → 业务驱动拆解 → 利润含金量 → 产业链话语权 → 财务信号与风险 → 来源链接。

## 输出示例

[查看完整报告](https://cuecue.cn/share/FKeQR7E8)

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
  --query "目标公司 上市公司财报分析：核心指标、业务驱动、利润含金量、产业链话语权" \
  --template-id template_7qiAwz \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-earnings-analysis.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 上市公司名称，**必填**；可选加财报期次或关注维度 |
| `--template-id` | 固定为 `template_7qiAwz` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='财报深读' for b in s.get('buddies',[]) if b.get('title')=='上市公司财报分析'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [巨潮资讯网](https://www.cninfo.com.cn) | A股年报/季报原文 | 免费 |
| [东方财富财报](https://data.eastmoney.com) | 财报数据、财务指标 | 免费 |
| [SEC EDGAR](https://www.sec.gov/edgar) | 美股财报 | 免费 |
