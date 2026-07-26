# Phase 2 Reference — 案例采集与风格指纹

## TOC

- §1 与 Phase 1 并行执行
- §2 提取风格特征
- §3 Style Fingerprint 结构
- §4 失败兜底

---

## §1 与 Phase 1 并行执行

Phase 2 复用 Phase 1 的 `SearchTimeline` 响应，不额外发起搜索。

- Phase 1 的 `tmp/tweets.json` 已包含 Top 20 推文及其 metrics
- Phase 2 从中取 Top 3（按 score 倒序），分析写作风格而非选题价值

---

## §2 提取风格特征

对 Top 3 推文，分析以下维度：

| 维度 | 提取方式 |
|------|----------|
| 开篇钩子类型 | 自定义分类：问句 / 数字 / 反直觉断言 / 引用 / 故事开头 |
| 段落节奏 | 计算：空行次数、最长段落字符数、平均段落字符数 |
| 表情符号密度 | 正文中 emoji 数 / 总字符数（Unicode 范围粗略判定） |
| Hashtag 数量与风格 | 计数 + 是否通用词（`#AI`）vs 长尾（`#browserautomation`） |
| 链接插入位置 | 开头 / 中间 / 末尾 / 无 |
| CTA 类型 | 转推 / 关注 / 评论讨论 / 访问链接 / 无 CTA |
| 带媒体类型 | image / video / gif / none |

这些特征由 Agent 从 `full_text` 语义分析得出，不要求精确量化——模型输出的 JSON 就能直接用。

---

## §3 Style Fingerprint 结构

写入 `workspaces/x-posting/<date>/style_fingerprint.json`：

```json
{
  "source_keyword": "browser automation",
  "analyzed_tweets": [
    "2045568934254960835",
    "2052697237856088114",
    "2053112233445566778"
  ],
  "fingerprint": {
    "hook_style": "反直觉断言 + 数字支撑（例：'48 hours after X posted, this appeared on GitHub'）",
    "paragraph_rhythm": "短段落多，平均 40-60 字符，段间空行分隔",
    "emoji_density": "低（0-2 个 emoji / 推文，多用于强调）",
    "hashtag_usage": "0-1 个长尾 hashtag，避免通用词",
    "link_position": "末尾附上 t.co 短链",
    "cta_type": "提问引导评论 / 暗示下篇更新",
    "media_preference": "video demo 比 static image 互动更高",
    "tone": "technical but with conversational hooks"
  },
  "example_hooks": [
    "Terminal automation + e2e testing solved",
    "Do you understand what {X} just open-sourced???"
  ]
}
```

`example_hooks` 保留最典型的 2-3 个开篇句，Phase 4 写作时作为语感参考。

---

## §4 失败兜底

- Phase 1 的 `tmp/tweets.json` 不存在（Phase 1 失败或被跳过） → 跳过 Phase 2，Phase 4 用户无风格指纹时使用默认"中性技术向"风格
- Top 3 均为 reply（噪音） → 从 `tweets.json` 取 Top 10 中的 3 条非 reply 长推文（full_text 长度 > 80 字符）
- 结构化提取出错（emoji 检测库不可用等） → 降级为 "tone + hook_style" 两个关键特征，其他置 null
