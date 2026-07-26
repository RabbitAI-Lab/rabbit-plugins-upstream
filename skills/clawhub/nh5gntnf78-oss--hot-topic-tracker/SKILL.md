---
name: hot-topic-tracker
description: 【2026增强版】自动抓取抖音/小红书/知乎/B站/微博热点榜单，使用当前可用最强模型进行智能分析，生成选题库并保存到腾讯文档。支持多模态热点识别、趋势预测、竞品对比。当用户说"今天有什么热点"、"生成选题库"、"抓取热点榜单"、"帮我看看最近什么火"、"分析热门趋势"、"热点选题"时触发此技能。
---

# 热点追踪器 (Hot Topic Tracker) - 2026增强版

## 概述

本技能自动抓取多个平台的热点榜单，使用当前可用的最强AI模型进行深度分析，生成内容选题建议，并自动保存到腾讯文档。

> 💡 模型选择策略：优先使用session当前模型（由model route自动选择最优），无需硬编码特定模型名。

### 2026年新特性
- **多模态热点识别**：不仅抓取文本内容，还能识别视频封面、图片热点
- **AI趋势预测**：基于历史数据预测话题热度走向
- **竞品内容分析**：自动分析竞品爆款内容的结构和技巧
- **多平台一键分发**：生成内容后可自动适配不同平台格式

## 使用场景

- 内容创作者需要每日选题灵感
- 自媒体运营需要追踪热点趋势
- 营销团队需要实时监控热门话题
- 企业需要竞品内容分析和差异化策略

## 完整工作流

### 1. 抓取热点（2026增强版）

使用以下方式抓取热点：

**核心方式（按优先级）**：

1. **web_search工具**（首选）
   - 搜索各平台"热点榜单"获取最新数据
   - 支持freshness参数限定时间范围

2. **xbrowser技能**（进阶方案）
   - 使用真实登录态抓取抖音/小红书真实数据
   - 配置profile="user"复用用户浏览器
   - 适合需要登录态才能查看的内容

3. **multi-search-engine技能**（批量搜索）
   - 同时搜索多个平台，一次性获取
   - 适合快速概览

**各平台搜索关键词**：
| 平台 | 搜索关键词 | 备注 |
|------|-----------|------|
| 抖音 | "抖音热点榜单 今日" | 热点榜、飙升榜 |
| 小红书 | "小红书热门话题" | 热门笔记、话题榜 |
| 知乎 | "知乎热榜" | 科学榜、数码榜 |
| B站 | "B站热门视频" | 全站榜、分区榜 |
| 微博 | "微博热搜榜" | 实时热搜、话题榜 |
| 微信 | "微信热点" / "微信AI Agent" | 搜一搜热词 |
| AI Agent | "Claude Fable 5" / "Mythos 5" / "AI Agent 2026" | AI模型动态 |
| AI视频 | "可灵AI" / "即梦AI" / "Seedance" / "AI视频生成" | 视频工具格局 |
| 科技 | "GPT-5" / "DeepSeek" / "大模型" / "AI编程" | 大模型动态 |

**数据获取技巧**：
- 优先使用web_search，关键词加时间限定如 `site:weibo.com`
- 需要登录数据时使用xbrowser profile=user
- 批量抓取用multi-search-engine并发搜索

**2026增强能力**：
- 多模态识别：分析图片/视频封面的视觉元素
- 情感分析：抓取评论分析用户反馈
- 趋势预测：基于历史数据预测热度走向
- **AI Agent赛道追踪**：追踪 Claude Fable 5/Mythos 5 等发布动态对内容创作的影响
- **微信AI生态**：微信AI Agent内测动态、A2A协议协作
- **AI视频格局**：可灵3.0/Seedance 2.0/即梦AI格局变化

### 2. 数据分析（AI增强）

使用 **当前平台模型** 对抓取的热点进行深度分析：

1. **智能热度排序**：
   - 不仅按播放量/点赞数排序，还计算"互动率"（评论+转发/点赞）
   - 识别"黑马话题"（低粉丝高互动的内容）
   
2. **AI自动标签**：
   - 使用多模态AI自动识别内容主题（不仅限于预设标签）
   - 生成"话题聚类"，发现潜在关联话题
   
3. **趋势预测**：
   - 基于历史数据预测未来24-48小时的热度走向
   - 标记"稍纵即逝"的快闪话题 vs "持续发酵"的长效话题
   
4. **竞品内容拆解**（2026新增）：
   - 自动分析爆款内容的结构（开头hook、转折点、结尾call-to-action）
   - 提取高频词汇和情感倾向
   - 生成"爆款公式"参考

### 3. 生成选题建议（AI辅助创作）

基于热点和竞品分析，使用当前平台的强推理模型生成内容选题：

每个选题包含：

- **标题变体**（3个）：
  - 吸引眼球的标题（悬念式/数字式/反问式）
  - SEO优化标题（包含高频搜索词）
  - 平台定制化标题（适配不同平台的标题风格）
  
- **内容角度**：
  - 痛点切入：解决用户什么问题？
  - 干货分享：提供什么实用价值？
  - 情感共鸣：触发什么情绪？
  - 争议讨论：有什么对立观点？
  
- **平台适配**：
  - 抖音：15-60秒短视频脚本大纲
  - 小红书：图文笔记结构 + 封面文案
  - 知乎：回答框架 + 参考资料
  - B站：中长视频分镜脚本
  
- **AI热度预测**：
  - 高/中/低热度概率（基于历史数据训练）
  - 最佳发布时间建议
  - 标签和话题推荐
  
- **竞品参考**：
  - 同类爆款内容链接
  - "差异化角度"建议（如何做得比竞品更好）

### 4. 保存到腾讯文档（智能排版）

使用 `tencent-docs` 技能将选题库保存到腾讯文档：

**文档结构**：
1. **封面页**：
   - 标题："热点选题库 - YYYY-MM-DD"
   - 今日概览：共追踪X个平台，发现Y个高潜力选题
   - 热度趋势图（使用腾讯文档的智能图表）
   
2. **热点总览表**：
   - 表格形式展示所有抓取的热点
   - 列：排名 | 标题 | 平台 | 热度值 | 24h变化 | AI标签 | 操作按钮（点击跳转原文）
   
3. **选题建议详情**（按平台分类）：
   - 每个选题一个卡片式段落
   - 包含：标题变体、角度分析、脚本大纲、竞品参考、发布建议
   
4. **趋势预测页**（2026新增）：
   - AI预测的未来24小时热点演化
   - "值得提前布局"的长效话题列表
   
**自动化命名规则**：
- 每日版："热点选题库 - 2026-06-13"
- 每周精选版："本周热点精选 - 2026-W24"
- 月度报告版："6月热点趋势报告"

## 示例代码

### Python 脚本：热点数据清洗与趋势分析

如果需要处理大量热点数据，可以创建 `scripts/analyze_hot_topics.py`：

```python
import json
from datetime import datetime, timedelta
from collections import defaultdict

def analyze_trend(historical_data):
    """分析热点趋势，预测未来热度"""
    # 按话题分组
    topics = defaultdict(list)
    for item in historical_data:
        topic_key = item.get('title')[:20]  # 用标题前20字作为key
        topics[topic_key].append({
            'timestamp': datetime.fromisoformat(item.get('timestamp')),
            'heat': item.get('heat', 0)
        })
    
    # 计算趋势
    predictions = []
    for topic, data_points in topics.items():
        if len(data_points) < 3:
            continue
            
        # 简单线性回归预测
        data_points.sort(key=lambda x: x['timestamp'])
        hours = [(dp['timestamp'] - data_points[0]['timestamp']).total_seconds() / 3600 for dp in data_points]
        heats = [dp['heat'] for dp in data_points]
        
        # 计算斜率（每小时热度变化）
        if len(hours) >= 2:
            slope = (heats[-1] - heats[0]) / (hours[-1] - hours[0])
            predictions.append({
                'topic': topic,
                'current_heat': heats[-1],
                'slope': slope,
                'predicted_heat_24h': heats[-1] + slope * 24
            })
    
    return sorted(predictions, key=lambda x: x['predicted_heat_24h'], reverse=True)

if __name__ == '__main__':
    # 示例用法
    with open('hot_topics_history.json', 'r', encoding='utf-8') as f:
        historical_data = json.load(f)
    
    predictions = analyze_trend(historical_data)
    
    print("🔮 未来24小时热度预测TOP10：")
    for i, pred in enumerate(predictions[:10], 1):
        print(f"{i}. {pred['topic']} - 预测热度: {pred['predicted_heat_24h']:.0f}")
```

## 定时自动化（2026增强）

配合 `qclaw-cron-skill` 实现智能化自动追踪：

### 方案A：每日早报（基础版）

使用 `qclaw-cron-skill` 创建定时任务（请先读取该Skill了解最新格式）：

**建议配置**：
- 名称：每日热点追踪早报
- 时间：每天 9:00（cron: `0 9 * * *`，tz: Asia/Shanghai）
- 消息：使用 hot-topic-tracker 技能，抓取今日热点并生成选题库。重点关注科技、职场、生活技巧。生成后保存到腾讯文档。
- 推送：可根据可用渠道配置

### 方案B：实时监控（进阶版）

**建议配置**：
- 名称：热点实时监控
- 时间：每小时（cron: `0 * * * *`，tz: Asia/Shanghai）
- 消息：检查过去1小时内是否有新热点涌现（热度增长>50%）。如有则推送预警。
- ⚠️ 每小时执行成本较高，建议仅在工作时间启用（如 8-22点）

### 方案C：周报自动生成

**建议配置**：
- 名称：每周热点精选
- 时间：每周日 20:00（cron: `0 20 * * 0`，tz: Asia/Shanghai）
- 消息：汇总本周热点，生成精选报告（TOP10热点+爆款分析+下周趋势预测）。保存到腾讯文档。

> ⚠️ 实际创建cron任务前，请先读取 qclaw-cron-skill 的 SKILL.md 获取最新API格式

## 资源文件

### scripts/

如果需要复杂的数据处理，可以在此目录放置 Python 脚本：
- `analyze_hot_topics.py`：热点趋势分析和预测
- `clean_hot_topics.py`：热点数据清洗
- `generate_topics.py`：选题生成
- `competitor_analysis.py`：竞品内容分析

### references/

可以参考的文件：
- `platform_api.md`：各平台热点 API 文档
- `title_formulas.md`：爆款标题公式库
- `case_studies.md`：历史爆款案例分析
- `ai_models_guide.md`：AI模型使用指南（由 model route 自动选择最优模型）

### assets/

可以包含的模板文件：
- `topic_template.md`：选题库文档模板
- `report_template.docx`：热点分析报告模板
- `platform_adaptation_guide.md`：各平台内容适配指南

---

## 💰 付费增值服务

想要更省事？我还提供：

| 服务 | 价格 | 内容 |
|------|------|------|
| 🚗 代安装调试 | ¥68/次 | 帮你安装配置，解决环境问题 |
| 🛠️ 定制技能开发 | ¥200起 | 根据需求开发专属技能 |
| 🚀 视频自动化陪跑 | ¥999/月 | 从0到1搭建完整视频自动化 |
| 📦 技能全家桶 | ¥199 | 11个AI技能永久用 + 代安装 |

**微信咨询**：[微信号待填写]

---

**提示**：初次使用可以先不创建脚本和参考文档，直接让我按照工作流程执行即可。熟悉后可以根据需要逐步添加资源文件。

**实用建议**：
1. 使用当前session模型进行所有AI分析（model route自动选最优）
2. 大批量数据分析可指定低成本模型（如DeepSeek）
3. 长篇选题建议使用强推理模型
4. 配合 xbrowser 技能实现真实登录态抓取（profile=user）
5. 定时任务务必参考 qclaw-cron-skill 最新格式
6. **热点赛道新增**：AI Agent（Fable 5/Mythos 5）、微信AI生态、AI视频生成工具格局
7. 每周关注OpenAI/Anthropic/Google模型发布动态
