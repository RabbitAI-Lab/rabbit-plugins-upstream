# Humanizer — 有品味的去 AI 味

A Clawdbot skill that removes signs of AI-generated writing from text, making it sound more natural and human. **Unlike blunt "delete every em dash" humanizers, it preserves the literary devices the author meant to keep, and switches rules by genre.**

中文说明：这是一个有"品味"的去 AI 味润色技能。多数去 AI 工具无脑删破折号、砍排比，把作者想留的风格也一起扔了；这个会先判断"这是 AI 套路还是有意表达"，保留复调意象、刻意象征、方言等文学装置，并按论文 / 简历 / 小红书 / 小说 / 公文切换"人味"标准。

## Installation

Install via ClawdHub:

```bash
clawdhub install humanizer
```

## Usage

Ask your agent to humanize text:

```
Please humanize this text: [your text]
```

Or invoke directly when editing documents. For Chinese scenes, try:

```
把这段论文去AI味，保留学术分寸
帮我润色这份简历，去掉自夸营销腔
给这篇小红书加网感，别改得太书面
```

## What Makes It Different

1. **Preserves intentional devices.** Polyphonic imagery, deliberate symbolism, dialect, irony, and white space stay. It only strips genuine AI filler — not the author's voice. When unsure, it keeps the device and flags it.
2. **Genre-aware.** Academic papers need restraint; résumés need strong verbs; social posts need realness and 网感; fiction needs maximum tolerance for voice. One rule set does not fit all.
3. **Chinese-specific.** Handles 「」 quotes, full-width em dashes, 黑话 stacking (赋能/抓手/闭环), mechanical 首先/其次/最后 layering, and emoji overuse — things English humanizers miss.

## Overview

Based on [Wikipedia's "Signs of AI writing"](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) guide, maintained by WikiProject AI Cleanup. This comprehensive guide comes from observations of thousands of instances of AI-generated text.

### Key Insight

> "LLMs use statistical algorithms to guess what should come next. The result tends toward the most statistically likely result that applies to the widest variety of cases."

## 24 Patterns Detected

### Content Patterns
1. **Significance inflation** - "marking a pivotal moment..." → specific facts
2. **Notability name-dropping** - listing sources without context
3. **Superficial -ing analyses** - "symbolizing... reflecting..."
4. **Promotional language** - "nestled within the breathtaking..."
5. **Vague attributions** - "Experts believe..."
6. **Formulaic challenges** - "Despite challenges... continues to thrive"

### Language Patterns
7. **AI vocabulary** - "Additionally... testament... landscape..."
8. **Copula avoidance** - "serves as" instead of "is"
9. **Negative parallelisms** - "It's not just X, it's Y"
10. **Rule of three** - forcing ideas into groups of three
11. **Synonym cycling** - excessive synonym substitution
12. **False ranges** - "from X to Y" on non-meaningful scales

### Style Patterns
13. **Em dash overuse**
14. **Boldface overuse**
15. **Inline-header lists**
16. **Title Case Headings**
17. **Emoji decoration**
18. **Curly quotation marks**

### Communication Patterns
19. **Chatbot artifacts** - "I hope this helps!"
20. **Cutoff disclaimers** - "While details are limited..."
21. **Sycophantic tone** - "Great question!"

### Filler and Hedging
22. **Filler phrases** - "In order to", "Due to the fact that"
23. **Excessive hedging** - "could potentially possibly"
24. **Generic conclusions** - "The future looks bright"

## Full Example

**Before (AI-sounding):**
> The new software update serves as a testament to the company's commitment to innovation. Moreover, it provides a seamless, intuitive, and powerful user experience—ensuring that users can accomplish their goals efficiently.

**After (Humanized):**
> The software update adds batch processing, keyboard shortcuts, and offline mode. Early feedback from beta testers has been positive, with most reporting faster task completion.

## References

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup)

## License

MIT
