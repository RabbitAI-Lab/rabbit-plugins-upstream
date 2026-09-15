---
name: free-course-share
version: 1.1.5
description: Verifies and organizes free-course facts, then drafts sharing copy. Invoke only when the user explicitly requests both course curation and share-copy creation.
allowed-tools: WebSearch, WebFetch
---

# Free Course Share

## Goal

Evaluate genuinely free courses and produce an evidence-based shortlist plus accurate sharing copy.

## Trigger

Invoke only when the user explicitly asks for both:

1. organizing, screening, comparing, or curating free courses; and
2. drafting copy for sharing those courses.

Both conditions are required. If either is unclear, ask one concise clarifying question.

### Positive examples

- “筛选 5 门真正免费的 Python 入门课，并写一段分享文案。”
- “比较这些免费设计课程，选出适合零基础的 3 门，再生成社群推荐稿。”
- “核实这批公开课的免费范围和有效期，整理清单并写可发布前审核的介绍。”

### Non-trigger examples

- “推荐几门免费的数据分析课程。”（只有课程推荐）
- “这门课程现在免费吗？”（只有事实核验）
- “帮我写一段健身产品推广文案。”（主题不是免费课程）
- “替我把课程介绍发布到社交平台。”（要求执行发布）
- “比较几门付费 MBA 课程并给出建议。”（目标不是免费课程分享）

## Boundaries

- Work only with user-provided facts and publicly accessible course pages.
- Use `WebSearch` and `WebFetch` only when current public facts require verification.
- Keep all activity read-only and return reviewable text in the current conversation.

## Fact Verification

For each candidate course, verify only claims relevant to selection or sharing:

- course title and provider;
- whether access is free and what “free” includes;
- enrollment or availability status;
- important dates or expiration;
- delivery format, level, duration, and prerequisites;
- certificate, assessment, trial, audit, subscription, region, or registration requirements;
- direct destination URL when available.

Use this evidence policy:

1. Prefer official course or provider pages for current public facts.
2. Cross-check material claims when sources conflict or an offer is ambiguous.
3. Label evidence as `Verified`, `User-provided`, `Unverified`, `Conflicting`, or `Outdated`.
4. Define precisely what is free, including access scope and important conditions.
5. Record the verification date for time-sensitive claims.
6. Preserve uncertainty and include only supported details.

When reliable verification is unavailable, label the item clearly or exclude it if the user requires verified courses.

## Selection Method

1. Extract the audience, topic, level, goal, time budget, preferred format, region, and definition of “free.”
2. Ask a question only when a missing detail materially changes eligibility.
3. Normalize duplicate course entries without merging conflicting facts.
4. Rank eligible courses by the user's criteria, or by relevance, access clarity, provider credibility, and practical fit.
5. Explain decisions with concise, evidence-based reasoning.

## Output Contract

### Criteria

- Audience:
- Learning goal:
- Free-access definition:
- Constraints:
- Unknowns:

### Screened Courses

For each course include:

- Course:
- Provider:
- Free access:
- Key restrictions:
- Format / level / duration:
- Availability or important date:
- Verification status:
- Selection decision: Include / Exclude / Needs confirmation
- Reason:
- Direct URL, if available:

### Caveats

List material uncertainties and conditions that could change the user's decision.

### Share Draft

Create one ready-to-review draft that:

- accurately reflects the screened facts;
- clearly states important restrictions near the relevant claim;
- uses direct course URLs;
- includes a brief reminder that availability and terms may change when time-sensitive;
- is clearly presented as a draft for review.

## Completion Standard

- The two-part trigger is satisfied.
- Every material claim is supported or visibly labeled.
- “Free” is defined precisely.
- The shortlist and share draft are clearly separated.
- The work remains read-only and has no external side effects.
