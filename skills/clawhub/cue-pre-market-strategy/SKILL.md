---
name: cue-pre-market-strategy
description: 用 Cue 生成交易员级别的盘前策略内参——扫描隔夜全球突发事件与技术突破，推导其对 A 股的逻辑映射与产业链传导，在开盘前锁定今日最具爆发力的主题。
description_zh: Cue 深度盘前策略内参：扫描隔夜全球事件，推导A股逻辑映射与产业链传导，锁定爆发力主题。
version: 1.0.0
author: sensedeal
tags: [cue, pre-market, trading-strategy, 盘前策略, 盘前内参, 开盘策略, 主题挖掘]
---

# 深度盘前策略内参

> 交易员的盘前必读。扫描隔夜全球突发事件与技术突破，推导其对 A 股的逻辑映射与产业链传导，在开盘前锁定今日最具爆发力的主题。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令，`--template-id template_qsweF9` | 禁止连发多条 |
| 4 | `[cue-research] RESULT ok` = 完成 | 禁止编造 |
| 5 | 原样交付报告 | 禁止概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 每日开盘前 | 系统性地扫描隔夜事件并推导A股影响 |
| 主题投资 | 识别当日最具爆发力的交易主题 |
| 风险预警 | 隔夜利空事件的产业链传导预警 |
| 仓位调整 | 根据盘前信号决定开盘操作方向 |

## 核心能力

1. **隔夜全球事件扫描** — 美股、欧股、大宗商品、地缘、产业突破
2. **逻辑映射推导** — 每个事件 → A 股映射逻辑 → 受益/受损标的
3. **产业链传导分析** — 上游事件如何沿产业链传导到中下游
4. **爆发力主题排序** — 按逻辑强度和市场弹性排序今日主题

## 试试这样问

- "今天盘前有什么重要信号？"
- "隔夜美股对今天A股有什么影响？"
- "今天最可能爆发的主题是什么？"
- "开盘前需要关注哪些风险？"

## 输出形式

结构化内参：隔夜事件清单 → 逻辑映射 → 产业链传导 → 爆发力主题排序 → 风险提示 → 来源链接。

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
  --query "今日盘前策略：隔夜全球事件→A股映射→产业链传导→爆发力主题" \
  --template-id template_qsweF9 \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-pre-market.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 可加行业偏好或风险关注点 |
| `--template-id` | 固定为 `template_qsweF9` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='投资研究' for b in s.get('buddies',[]) if b.get('title')=='深度盘前策略内参'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [东方财富](https://www.eastmoney.com) | A股盘前资讯 | 免费 |
| [财联社](https://www.cls.cn) | 隔夜要闻 | 免费 |
| [华尔街见闻](https://wallstreetcn.com) | 全球市场动态 | 免费 |
| [新浪财经](https://finance.sina.com.cn) | 盘前公告汇总 | 免费 |

---

## 输出示例

[查看完整报告](https://cuecue.cn/share/jwhaQSVxNzzWYOvHmt-jO)

## FAQ

**Q: 和投顾早盘简报、24h热点追踪有什么区别？**
A: 早盘简报 → 理财师客户沟通素材；热点追踪 → 催化剂拆解；盘前策略 → 交易员级别深度推导，含产业链传导和爆发力排序。三者深度递增。

**Q: 最佳跑的时间？**
A: 建议 8:00-8:30 跑，隔夜信息已充分沉淀，距开盘足够决策时间。
