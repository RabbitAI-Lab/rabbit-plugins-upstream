---
name: us-tech-giant-analyst
description: This skill should be used when a user asks to analyze a US-listed technology giant such as Apple, Microsoft, Nvidia, Amazon, Alphabet, Meta, or Tesla. It produces a structured investment-and-competitive analysis covering business model, market share, growth prospects, technology moat, financial reports, and stock price trend. Trigger when the user asks to analyze, evaluate, compare, or profile a big-tech company's fundamentals, earnings, competitive position, or stock performance.
---

# US Tech Giant Analyst

## Overview

This skill turns a vague request like "分析一下英伟达" or "How is Apple positioned versus Microsoft?" into a disciplined, six-part company analysis. It gathers the latest public data through web search and renders a consistent report that an investor, strategy analyst, or student can act on. The skill never fabricates numbers — every figure is traced to a fetched source, and gaps are stated explicitly.

## When to Use

Activate this skill when the user:

- Names a US tech giant and asks for an analysis, evaluation, breakdown, or profile.
- Uses trigger phrases such as "分析", "评估", "护城河", "商业模式", "市场占额", "财报", "股价走势", "前景", "analyze", "evaluate", "moat", "earnings", "stock trend", "compare A vs B".
- Wants a competitor comparison across the six dimensions below.
- Asks for a plain-language explanation of why a company is winning or losing.

Do not activate for: non-US companies (unless explicitly framed as a comparison), private startups without public filings, or pure stock-trading execution (this skill informs, it does not place orders).

## Execution Logic

Follow this workflow for every request.

### Step 1 — Scope the request

Identify the target company (ticker or name) and which of the six dimensions the user wants. If the user asks broadly ("分析一下 Nvidia"), cover all six. If they ask narrowly ("Nvidia 的股价走势"), focus but still give a one-line context for the other five.

### Step 2 — Gather fresh data

Use web search and web fetch to collect, for the current year:

- Latest quarterly and annual results: revenue, net income, gross margin, free cash flow, guidance (pull from the company's investor-relations page, SEC 10-K / 10-Q, or reputable financial outlets).
- Market share: segment-level share from industry reports (e.g., IDC, Canalys, StatCounter, Gartner) for the relevant market (cloud, chips, handsets, ads, etc.).
- Stock trend: recent price action, 52-week range, analyst consensus, and any major catalyst. Cite the date of the data.
- Moat signals: latest product / R&D / ecosystem moves, patent or supply-chain advantages, switching costs.
- Prospects: management commentary, secular tailwinds (AI, cloud, etc.), and principal risks.

Prefer primary sources (SEC filings, IR pages) over secondary. Always record the source URL and the data date next to each figure. If a number cannot be found, write "未找到公开最新数据" rather than guessing.

### Step 3 — Analyze, do not just summarize

For each dimension, state a judgment, not only facts:

- Business model: how the company makes money (revenue mix by segment), and what changed recently.
- Market share: the company's position, trajectory (gaining/losing), and the nearest competitor.
- Growth prospects: the 2-3 year thesis and the main upside/downside drivers.
- Technology moat: the durable advantage (scale, network effects, IP, integration, data) and how defensible it is.
- Financial reports: health read from margins, cash flow, balance sheet, and how results compare with consensus.
- Stock trend: direction and key levels, framed as context — never as investment advice.

### Step 4 — Render the report

Output a markdown report using the six-section template in `references/analysis-framework.md`. Lead with a one-paragraph verdict, then the six sections, then a concise risk list and a "data sources & dates" footer. Keep the tone objective; flag uncertainty.

## Output Structure

The report must contain these six headings (in this order):

1. **商业模式 (Business Model)**
2. **市场占额 (Market Share)**
3. **发展前景 (Growth Prospects)**
4. **技术壁垒 (Technology Moat)**
5. **财报表现 (Financial Reports)**
6. **股价走势 (Stock Price Trend)**

Close with **主要风险 (Key Risks)** and **数据来源与日期 (Sources & Dates)**. A worked example lives in `references/analysis-framework.md`.

## Reliability Rules

- No fabricated figures. Every quantitative claim cites a fetched source and date.
- State the data date prominently; tech and stock data go stale fast.
- Do not give personalized investment advice; frame outputs as analysis and context.
- If the request spans multiple companies, produce one section block per company, then a comparison table.

## Resources

- `references/analysis-framework.md` — the six-section report template, source checklist, and a fully worked Nvidia example.
