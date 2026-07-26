---
name: "xhs-research"
description: "小红书深度研究：话题搜索+总结/趋势分析/多模态报告/每日简报，支持发布回小红书"
user-invocable: true
metadata:
  openclaw:
    emoji: "🔬"
    tags: ["xiaohongshu", "research", "analysis", "trends", "report"]
---

# XHS Research v2.0

## 定位
分析研究层。数据→`xhs-data`，运营→`xhs-ops`。

---

## 研究流程
1. 关键词扩展(主词+3-4长尾)
2. 调用 `xhs-data` 搜索+去重，Top 20-50
3. 爆款分析(登录态获取详情和评论)
4. AI 多模态报告生成

---

## 爆款分析指标

| 指标 | 公式 | 判断 |
|------|------|------|
| 赞藏比 | 点赞÷收藏 | <1实用, >3情绪 |
| 评论比 | 评论÷点赞 | >0.1高互动 |
| 入池差 | 平均互动-当前互动 | 判断是否入推荐池 |

---

## 报告模板

```markdown
# {主题} 小红书研究

## 📱 速览(可转发)
{2-3段口语化总结}

## 📊 数据概览 | N篇/{likes}赞/{collects}藏

## 🔝 Top 10
1. **标题** @作者 | 👍{} 📁{} | [查看](link)

## 🔍 深度分析
{按主题归并，不逐帖罗列}

## 💡 趋势洞察
## 📎 原始数据路径
```

### 写作风格
速览像朋友聊天，正文简洁，不用官腔。

---

## 每日简报工作流
1. 前置：`mcporter` + `xiaohongshu-mcp` 配置
2. 编辑 `config/topics.json`
3. `python scripts/run_daily.py --topic <topic> --dry-run`
4. 检查草稿 → 满意后 `--publish`

---

## 限制
- 未登录可能获取不到详情
- 搜索频率须保守
- 不要自动全量发布
