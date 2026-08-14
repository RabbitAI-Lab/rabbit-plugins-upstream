---
name: "project-retrospective"
description: "Reconstructs project timelines, tracks problems and solutions, extracts reusable lessons from AI-assisted projects. Invoke when user wants to review/recap a completed or ongoing project, create process documentation, extract experience, or do a project retrospective."
---

# Project Retrospective & Experience Distillation

This skill guides the creation of a structured project retrospective document for any complex AI-assisted project. It reconstructs the full journey — timeline, problems, solutions, iterations, and lessons — from scattered conversation history, memory files, and workspace artifacts.

## When to Use

**Trigger conditions (any one):**
- User says "复盘" / "回顾" / "总结过程" / "整理经验" / "retrospective" / "review the process"
- User wants to document what happened across multiple sessions
- User is about to start a new task and wants to carry over experience from a previous one
- User asks "我们之前做了什么" / "整个过程是怎样的" / "踩了哪些坑"
- A project has spanned multiple sessions and context is getting lost

**Complexity gate — only proceed with full retrospective if the project meets at least 2 of these:**
1. Project spanned more than 3 days or 5+ sessions
2. Went through 3+ iterations on any major component
3. Context was broken across sessions (new task was created)
4. Output has reusable value (code, methodology, classification system, etc.)
5. User explicitly wants to preserve lessons for future projects

If the project does NOT meet the complexity gate, do a lightweight summary instead (3-5 bullet points of key takeaways) and tell the user why a full retrospective isn't needed.

## Workflow

### Step 1: Gather Raw Material

Collect information from all available sources. Do NOT rely on memory alone.

**Sources to check (in order):**

1. **Memory files** — Read `project_memory.md` and recent `topics.md` files:
   ```
   /Users/shiyan/.trae-cn/memory/projects/<project-path>/project_memory.md
   /Users/shiyan/.trae-cn/memory/projects/<project-path>/<date>/topics.md
   ```
   Extract: hard constraints, engineering conventions, lessons learned, topic summaries with timestamps.

2. **Session memory files** — Read `session_memory_*.jsonl` files for detailed task-level history:
   ```
   /Users/shiyan/.trae-cn/memory/projects/<project-path>/<date>/session_memory_*.jsonl
   ```
   Extract: specific tasks, TODOs, related files, decisions made.

3. **Workspace files** — List and inspect key files in the workspace:
   - Scripts, configs, data files (check modification times for chronology)
   - Existing documentation or analysis reports
   - Git log if a repository exists (`git log --oneline --stat`)

4. **Conversation context** — Review the current conversation for any additional context not captured in memory.

**Output of Step 1:** A raw chronological list of events, each with:
- Approximate date/time
- What happened
- What problem was encountered (if any)
- What solution was applied (if any)
- What files were created/modified (if any)

### Step 2: Assess and Structure

Analyze the raw material and identify:

1. **Project phases** — Group events into logical phases. Typical phases:
   - Setup / Goal definition
   - Data collection / Implementation
   - Processing / Iteration
   - Analysis / Evaluation
   - Output / Delivery
   - Reflection / Open-source (if applicable)

2. **Problem chain** — Identify all problems encountered. For each problem:
   - Assign a sequential number (问题1, 问题2, ...)
   - Determine root cause
   - Document the solution applied
   - Count iterations (how many times the approach was revised before working)

3. **Key decisions** — Identify points where a significant choice was made (e.g., "switched from keyword matching to three-layer classification")

4. **Lessons learned** — Extract reusable insights, categorized by domain

### Step 3: Generate the Retrospective Document

Use the template below. Adapt section names to fit the actual project — do not force-fit if the project doesn't have certain phases.

---

## Document Template

```markdown
# [项目名称] 的完整过程记录

> 一句话概述：这个文档记录了 [用户] 从 [开始日期] 到 [结束日期]，用 [工具/AI] 完成 [项目目标] 的完整过程。重点不是结论，而是过程中踩的坑、发现的问题、迭代的方案。

---

## 一、起点：我们一开始想做什么

### 1.1 需求来源
[描述项目发起的背景和动机。谁、为什么、想解决什么问题。]

### 1.2 最初的目标
[记录最初的预期和目标。然后对比实际花费的时间和精力，突出预期与现实的差距。]

---

## 二、[阶段1名称]：[阶段摘要，如"数据不是拿下来就能用"]

### 2.1 第一次尝试
[描述第一次做了什么，用了什么方法。]

发现的问题：
[列出此阶段遇到的问题，每个问题加粗标题+详细描述]

### 2.2 后续迭代
[描述如何改进，又遇到什么新问题。]

### 2.X 阶段总结
| 问题 | 根因 | 解决方案 | 迭代次数 |
|------|------|---------|---------|
| [问题1] | [根因] | [解决方案] | [次数] |

---

## 三、[阶段2名称]：[阶段摘要]
[同上结构，每个阶段一个章节]

---

## [继续按实际阶段数量添加章节]

---

## N、整个过程的时间线

| 日期 | 阶段 | 关键事件 |
|------|------|---------|
| [日期] | [阶段] | [事件] |

---

## N+1、核心教训总结

### 关于[维度1，如"数据采集"]
1. **[教训1]**
2. **[教训2]**
3. **[教训3]**

### 关于[维度2，如"分类方法"]
1. **[教训1]**
2. **[教训2]**

### 关于[维度3，如"工具使用"]
1. **[教训1]**
2. **[教训2]**

### 关于[维度4，如"项目管理"]
1. **[教训1]**
2. **[教训2]**
```

### Step 4: Experience Conversion (Optional)

After generating the retrospective, offer to convert key lessons into reusable artifacts:

1. **Update project_memory.md** — Add new hard constraints, engineering conventions, and lessons learned extracted from this retrospective.

2. **Suggest Skill creation** — If a lesson is broadly applicable (e.g., "keyword specificity matters more than coverage in text classification"), suggest creating a Skill that encodes this knowledge for future projects.

3. **Create a checklist** — If the project type is likely to recur, generate a pre-flight checklist of things to watch for based on problems encountered.

## Writing Guidelines

### Tone
- First-person from the user's perspective ("我发现..." / "我决定...")
- Conversational but precise — avoid corporate jargon
- Honest about mistakes — the value is in the failures, not the successes
- Bold key judgments and insights as visual anchors

### Problem Documentation Rules
- Every problem gets a **sequential number** (问题1, 问题2, ...) — this makes cross-referencing easy
- Format: **问题N：[问题标题]。** followed by detailed description
- Always include: what happened, why it happened (root cause), how it was fixed
- If a problem required multiple iterations, note how many times the approach was revised

### Lesson Extraction Rules
- Each lesson must be **one sentence**, bolded, actionable
- Lessons should be **domain-categorized**, not listed randomly
- A good lesson answers: "If I did this again, what would I do differently?"
- Bad lesson: "分类很重要" (too vague)
- Good lesson: "关键词特异性比覆盖面更重要，泛化词的代价是大量误判，而误判的代价比漏判大得多"

### What NOT to Do
- Do NOT write a success story — focus on problems, iterations, and lessons
- Do NOT list every minor task — focus on decisions, problems, and turning points
- Do NOT repeat the same insight in multiple sections
- Do NOT use abstract metaphors ("时代注脚" "水位下降") — be concrete and specific
- Do NOT fabricate dates or events — if unsure, mark as "[大约X月]"
- Do NOT skip the complexity gate — if the project is simple, do a lightweight summary instead

## Output

Save the retrospective document to the user's workspace folder as:
```
[项目名称]过程记录.md
```

After saving, provide the file link to the user and offer the experience conversion options from Step 4.
