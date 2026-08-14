---
name: cue-hotspot-tracker
description: 用 Cue 实时追踪近 24 小时全球重磅资讯，拆解其对权益市场的催化逻辑与受益板块，助短线交易者紧跟市场热钱流向。
description_zh: Cue 24h热点追踪：扫描近24h全球重磅资讯，拆解催化逻辑与受益板块，识别热钱流向。
version: 1.0.0
author: sensedeal
tags: [cue, hotspot, catalyst, trading, 热点追踪, 题材挖掘, 短线, 催化剂]
---

# 24h热点与催化剂追踪

> 短线题材捕捉手。实时追踪近 24 小时内全球重磅资讯，拆解其对权益市场的催化逻辑与受益板块，助你紧跟市场热钱流向。

## Agent 执行摘要

| 顺序 | 做什么 | 禁止 |
|------|--------|------|
| 1 | 确认 Cue runner 就绪 | 禁止跳过 |
| 2 | 告知用户耗时 2-15 分钟 | 禁止中途取消 |
| 3 | 一条命令阻塞等待，`--template-id template_maVyo-` | 禁止连发多条 |
| 4 | stdout `[cue-research] RESULT ok` = 完成 | 无 RESULT = 未完成 |
| 5 | 原样交付报告 | 禁止自行概括 |

## 适用场景

| 场景 | 解决的问题 |
|------|-----------|
| 盘前热点扫描 | 开盘前快速了解今日可能爆发的题材 |
| 盘中题材追踪 | 突发新闻的实时催化逻辑拆解 |
| 短线选股参考 | 识别受益板块和个股 |
| 风险事件规避 | 识别可能冲击持仓的负面催化剂 |

## 核心能力

1. **24h 全球资讯扫描** — 覆盖政策、产业、公司、地缘等维度
2. **催化逻辑拆解** — 每条资讯 → 对 A 股的传导路径和影响程度
3. **受益板块识别** — 按催化强度排序受益行业
4. **热钱流向判断** — 结合盘面信号判断资金方向

## 试试这样问

- "今天市场有哪些热点？"
- "最近24小时有什么重大催化剂？"
- "哪些板块今天可能爆发？"
- "隔夜有什么影响A股的重磅消息？"

## 输出形式

结构化报告：热点资讯列表 → 每条催化逻辑拆解 → 受益板块排序 → 热钱流向判断 → 来源链接。

---

## 环境要求

**首次使用运行 skill 自带的一键安装脚本**（检查依赖 → 克隆 runner → 验证 Key → 测试连通性）：

```bash
```

Runner 来源：[GitHub - sensedeal/cue-skills](https://github.com/sensedeal/cue-skills)（[Gitee 镜像](https://gitee.com/sensedeal/cue-skills)）。

依赖：`git` + `python3` + `curl`。Python 仅用标准库，无额外 pip 依赖。

Cue API Key：在 [cuecue.cn](https://cuecue.cn) 获取，`cue login` 写入 `~/.cue/config.json`。新账号送免费积分。

---

## 调用说明

```bash
python3 ~/.cue/cue-skills/cue-research/scripts/research_run.py \
  --query "近24小时全球市场热点与催化剂分析" \
  --template-id template_maVyo- \
  --output ~/cue-reports/$(date +%Y-%m-%d-%H%M)-hotspot-tracker.md
```

| 参数 | 说明 |
|------|------|
| `--query` | 研究问题。可选加行业/方向限定 |
| `--template-id` | 固定为 `template_maVyo-` |
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
echo "=== 3/3 搭子 ===" && curl -sS --max-time 10 "https://cuecue.cn/api/playbook" -H "Authorization: Bearer $CUE_KEY" | python3 -c "import sys,json;scenes=json.load(sys.stdin).get('data',{}).get('scenes',[]);buddy=[b for s in scenes if s.get('secondary_category')=='投资研究' for b in s.get('buddies',[]) if b.get('title')=='24h热点与催化剂追踪'];print(f'可用:{len(buddy)}个') if buddy else print('暂不可用')"
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
| [东方财富](https://www.eastmoney.com) | A股资讯、公告 | 免费 |
| [华尔街见闻](https://wallstreetcn.com) | 全球财经快讯 | 免费 |
| [财联社](https://www.cls.cn) | 电报式财经资讯 | 免费 |
| [Reuters](https://www.reuters.com) | 国际财经新闻 | 免费 |

---

## 输出示例

[查看完整报告](https://cuecue.cn/share/IeiYoiYB1DsJ5fWc_1jF0)

## FAQ

**Q: 和投顾早盘简报有什么区别？**
A: 早盘简报面向理财师生成客户沟通素材；热点追踪面向交易员做催化剂拆解和板块映射。

**Q: 能指定关注的行业吗？**
A: 可以，在 `--query` 中说明，例如"重点关注新能源和半导体方向"。
