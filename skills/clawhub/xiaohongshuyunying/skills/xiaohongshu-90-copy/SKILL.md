---
name: xiaohongshu-90-copy
agent_created: true
description: Upgrade Xiaohongshu/WeChat public-account copy drafts from "good enough" to 90-score quality by injecting real cases, personal persona, emotional hooks, and actionable tools. Use this skill when the user has a content draft (especially myopia-control / vision-care content for the "茶不二" IP) and asks to raise the score, fix low scores, or push it to 90分.
---

# 小红书/公众号 90分文案升级

## Overview

This skill turns a structurally sound draft into a 90-score piece of Xiaohongshu or public-account content.

The core formula:

> **90分文案 = 专业框架 + 真实案例 + 茶不二在场 + 强情绪钩子 + 可行动工具**

It is especially tuned for the 茶不二 IP (西安视光师 + 宝爸, 近视防控 / 翻转拍 / 儿童近视 topic) but works for any educational/authority content where the user needs to move from "informative" to "shareable and trust-building."

## When to use this skill

Invoke this skill when the user:
- Says a draft "分数太低了" or "怎么再上90分"
- Asks to "精修" a draft and explicitly wants high engagement
- Has a draft with good framework/data but feels "像科普文" or "不够打动人"
- Wants a Xiaohongshu post that drives comments, shares, and private-message inquiries

## Required inputs

- The user's draft (or a path to a draft file)
- The target platform (Xiaohongshu, WeChat public account, video script, Moments)
- The persona angle for "茶不二": 宝爸 + 视光师, 实战派, 亲自写内容亲自做策略

## Output format

Always produce a revised markdown file that includes:

1. **Title and hook** (first 3 lines must carry emotion or conflict)
2. **Body** with the 90分 formula applied
3. **10 hashtags** for Xiaohongshu (or platform-appropriate tags)
4. **Upgrade notes** explaining what was changed and why
5. **Rescore table** using the 8-dimension 炼金炉 scoring system (out of 40)

## Step-by-step workflow

### Step 1: Diagnose the draft against the 90分 formula

Read the draft and score it on the 5 components. Note which are missing:

| Component | What it means | Typical gap |
|-----------|---------------|-------------|
| 专业框架 | Clear structure, data, professional quotes, medical/technical backing | Usually already present |
| 真实案例 | A concrete patient story, clinic scene, or parent-child comparison | Most often missing |
| 茶不二在场 | A first-person "I" moment from the 茶不二 persona (clinic experience, own child, industry observation) | Often missing or only hinted |
| 强情绪钩子 | Fear, guilt, relief, surprise, or a punchy closing line that begs to be screenshotted | Often too rational |
| 可行动工具 | Self-check list, decision tree, comparison table, or comment CTA that lowers action barrier | Often weak or absent |

### Step 2: Inject a real opening case

Replace or supplement the abstract opening with one of these patterns:

- **Pattern A - 翻车现场**: "Last month a parent came in, eyes red... equipment cost 30k, 3 months later axial length +0.18mm."
- **Pattern B - 诊室对比**: "Two 8-year-old girls, both -1.00D, one year later one +25°, one +100°."
- **Pattern C - 惊人发现**: "I looked at the report for 3 seconds and knew the training direction was reversed."

Keep the case specific enough to be vivid (age, numbers, time frame) but anonymize the patient.

### Step 3: Add one concrete scenario per main section

For each major section (e.g., "5 information gaps," "3 unsuitable groups," "3 mistakes"), add:

- A one-sentence real-world scenario
- The specific data point that reveals the problem
- The consequence if ignored

Example: instead of only saying "myopia undercorrection accelerates growth," add: "She gave her child -1.50D glasses for -2.00D myopia to 'protect the eyes' — one year later, the child needed -3.00D."

### Step 4: Insert the 茶不二 persona

Add 1-2 first-person sentences from the 茶不二 identity. Choose from these angles:

- **As a dad**: "When my daughter was diagnosed, the first thing I did wasn't buy equipment..."
- **As a clinician**: "In more than 10 years of optometry, the most heartbreaking cases are..."
- **As a practitioner**: "Every time a parent brings a generic flippper they bought online, my first thought is..."
- **As an observer**: "I've seen hundreds of reports; the proportion of children with over-accommodation is far higher than parents think."

Place the persona sentence where it creates the most trust: right before a hard truth, after a case, or near the closing summary.

### Step 5: Strengthen emotional hooks and screenshot-worthy lines

Add at least one of the following:

- A bold contrast: "一年涨25度 vs 100度"
- A physical metaphor: "等于给抽筋的肌肉加杠铃"
- A reversed expectation: "以为买了设备就万事大吉"
- A guilt-inducing question: "凭什么买翻转拍就敢直接买通用款？"
- A closing call: "转发给那个只会买买买的家人"

### Step 6: Add an actionable tool

Choose one tool that matches the content type:

- **自查表** for "3 types / 5 mistakes / N items" content
- **对比表** for product-vs-product or before-vs-after content
- **决策树** for "should I choose A or B" content
- **时间轴** for "follow-up schedule" content
- **评论区诊断** for "send me your data and I'll analyze" content

The tool should be easy to screenshot and share.

### Step 7: Rewrite for Xiaohongshu mobile reading

- Split paragraphs into 1-3 sentences each
- Use bold for key numbers and takeaways
- Use emoji sparingly (🔹 for sub-points, 🚨 for warnings, 1️⃣2️⃣3️⃣ for steps)
- End with a concrete comment prompt: "评论区报数字+年龄" or "把报告发我帮你看"

### Step 8: Rescore and explain

Use the 8-dimension 炼金炉 scoring table to show before/after scores. Explain the biggest gains. If the result is not yet 36-38/40, identify what still needs to be added.

## 8-dimension 炼金炉 scoring system

Rate each dimension 1-5:

1. 情绪强度
2. 传播动机
3. 独家性
4. 身份匹配
5. 时效性
6. 传播锚点
7. 可视化
8. 参与门槛

Total: 8-40. ≥35 is considered 核弹级 (viral-level). Translate to 100-point scale: 35/40 = 87.5, 36/40 = 90, 38/40 = 95.

## Common failure modes to avoid

- **Too rational**: Draft is 80% framework, 20% emotion. Fix by adding a case and a closing emotional hook.
- **No persona**: Reads like a medical encyclopedia. Fix by inserting 茶不二's first-person observation.
- **Weak ending**: Closes with a summary instead of a CTA. Fix by adding a screenshotable final line + comment prompt.
- **No shareable asset**: Parents can't save or forward anything. Fix by adding a self-check table or comparison chart.
- **Abstract opening**: Starts with "Many parents..." Fix by opening with a specific parent/child/clinic scene.

## Platform-specific notes

- **Xiaohongshu**: Keep the first 3 lines high-emotion; use images for tables and checklists; hashtags must be included at the end.
- **WeChat public account**: Longer cases and deeper storytelling are allowed; use a strong title and a "转发给..." closing.
- **Video script**: Convert each case into a 3-5 second visual scene; prioritize the contrast hook and the closing CTA.
- **Moments**: Use one punchy paragraph + one image/table + a CTA.

## Sample 90分升级 prompts

- "This draft is good but too rational. Push it to 90分 by adding a real clinic case and a self-check table."
- "My A6 draft about 3 types of children who shouldn't use flippers is at 36/40. What would make it 38-40?"
- "Rewrite this public-account draft as a Xiaohongshu post with 茶不二's voice, a contrast case, and a screenshotable ending."

## Resources

No external scripts or assets required. The workflow relies entirely on the user's draft content and the 90分 formula above.
