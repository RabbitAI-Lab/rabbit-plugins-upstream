---
name: zh-history-literature-culture
description: >
  Write, polish, and cite Chinese-language articles on Chinese history,
  literature, and culture (Five Dynasties & Ten Kingdoms, silk, Dream of the
  Red Chamber, 洛神赋, 脂砚斋, etc.). Use when the user shares their own
  outline, notes, or stream-of-thought for a 中文历史/文学/文化 article and
  wants the agent to follow that thought-flow (must), expand with web
  research, and produce a polished, well-cited draft. Covers creation,
  polishing, fact-checking, and source selection.
---

# 中文历史·文学·文化写作 (Chinese History / Literature / Culture Writing)

Write, polish, and cite Chinese articles about Chinese history, literature, and culture. The user supplies the thinking; you supply the structure-faithful expansion, web research, and citations.

This skill complements `astro-sync` (publishing). Writing happens here; publishing happens there.

## Golden rules

1. **Follow the user's thought-flow — must.** The user's outline, sequencing, analogies, claims, and conclusions are the skeleton. Preserve them. Never silently rearrange the user's structure into a generic essay template, never drop their points, and never swap in your own thesis.
2. **Keep their voice.** Polish wording and grammar, but do not flatten the user's tone into a house style. A personal, essayistic voice stays a personal, essayistic voice.
3. **Cite, don't assert.** Every historical or literary claim gets checked against at least two independent, reliable sources. Anything that cannot be verified is NOT asserted in the article; it goes into the batch corrections doc under "待核实" (see AGENTS.md → Working rules → Verify facts before publishing).
4. **Flag before replacing.** If the user's thought contains a factual error, keep their intent, propose the corrected wording, and get explicit approval before swapping it in (AGENTS.md: "Get approval before any change").
5. **Never cite a source you have not opened and checked.** A "source" that is merely indexed in search results, or that lives on a trusted domain but does not actually contain the claimed sentence, is not a source — it is a ghost citation. Every citation must be verified against the source's actual content (see Phase 2.5).

## Inputs

- `source` — the user's raw text: an outline, bullet notes, a stream of thought, or a rough draft. May be pasted directly or given as a file path.
- `mode` — what the user wants this run:
  - `create` — turn notes/thoughts into a full article.
  - `polish` — improve an existing draft (grammar, flow, clarity, style) while preserving structure and voice.
  - `cite` — add/verify citations for an existing article (may combine with polish). Default: follow whatever the user asked; ask if unclear.
- `audience` / `tone` — optional; e.g. "general readers", "academic-leaning", "blog-style". Default: general literate audience.

## Workflow

### Phase 1 — Understand the thought-flow (do not skip)

1. Read the user's input end to end.
2. Extract and restate the user's **own** structure back to them: main sections, key claims, and the connecting logic. List anything you plan to add, cut, or move.
3. Confirm with the user before writing the article, unless they asked for an immediate draft and the structure is unambiguous.

### Phase 2 — Research & source curation

For each claim that needs support (dates, events, attributions, quotations, chapter references, terminology):

4. **Search the web** for each fact independently. Prefer site-restricted queries against trusted domains, e.g. `site:zh.wikisource.org 洛神赋` or `kaogu.cn 钱山漾 年代`.
5. **Cross-check with at least two independent, reliable sources.** When the sources disagree, record the discrepancy in the corrections doc rather than silently picking a side.
6. **Prefer primary text.** For classical works (洛神赋, 红楼梦, 旧五代史, 人间词话, 诗经, 全宋词…), quote from the primary text where possible (Wikisource scans/editions, 中华书局点校本), and verify the exact wording and chapter (回目) number.
7. For literature, verify **chapter attributions against the original text**, not memory: e.g. 刘姥姥一进荣国府=第六回, 元妃省亲=第十八回, 葬花吟=第二十七回, 黛玉焚稿=第九十七回.

### Phase 2.5 — Cross-checking the source (verify the truth)

A trusted domain is not proof. The claim must be **actually present in the source's content**, not merely plausibly attributed to it. For every claim:

8. **Open each source and locate the exact passage.** Fetch the page (wikisource, kaogu.cn, cssn.cn, Wikipedia article body, etc.) and confirm the specific sentence or data point appears there verbatim or in substance. If you cannot retrieve the full content, you may not cite it — put it in 待核实.
9. **Match claim ↔ source one-to-one.** Pair every fact in the draft with the exact sentence(s) that support it in each source. If a source does not actually say what the draft claims, drop that source or fix the claim; do not keep a citation next to a claim it does not support.
10. **Check source independence.** Two sources that copy one another (e.g. an article, a WeChat re-post, and a blog all reproducing the same 维基百科 text; or a Wikipedia entry whose only references are the very claim sites) count as ONE source, not two. Look for genuinely independent origins — a primary text, an academic paper, an official institution report.
11. **Watch for ghost citations.** A citation is suspicious if: the title looks plausible but no copy exists; the quoted sentence cannot be found anywhere in the cited work; or search returns only secondary mentions. AI-generated and memory-invented citations (e.g. 爱国书社1927, 中华书局 《李煿词作赏析》) must be detected and removed — see `docs/260808-corrections-by-citation.md` for worked examples.
12. **Cross-source sentence audit.** Take each quoted sentence and search it (in full, or its distinctive clause) on the web. It must surface in the primary text or in independently-verifiable sources. A sentence that only ever appears inside your own draft is fabricated.
13. **Prefer the original over commentary.** When a fact appears in both a primary text and a secondary commentary, cite the primary text; the commentary may be wrong or derivative. If two reliable sources disagree, record the discrepancy in the corrections doc rather than silently picking a side.

### Source quality — trusted vs. untrusted

**Trusted** (meet the ≥2-sources rule):
- Primary-text archives: Wikisource (维基文库) — classical texts, 二十四史, 诗文集, 白话小说原文.
- Official academic institutions: 中国社科院考古研究所 kaogu.cn, 中国社会科学网 cssn.cn, 故宫博物院, 国家图书馆, university presses.
- Academic presses & canonical editions: 中华书局 (点校本二十四史, 《南唐二主词校订》等), 上海古籍出版社, 人民文学出版社, 商务印书馆.
- Wikipedia entries (维基百科) that carry references.
- Peer-reviewed journals / academic databases (中国知网 CNKI, ResearchGate).

**NOT trusted** (never count as evidence): 微博 / WeChat / 头条 / 抖音 / TikTok / 哔哩哔哩弹幕 / personal blogs / 百度百科 无参考文献词条 / forum posts / AI chat outputs.

### Phase 3 — Write / polish

14. Write in Simplified Chinese by default (Traditional only if the source or user's draft is Traditional). Follow the user's section order and emphasis. Expand their points with researched detail; mark each fact-supported sentence with a citation marker.
15. Use precise terminology with first-use glosses where helpful (e.g. 包衣 = 内务府奴仆/皇室世仆, 软烟罗 vs 蝉翼纱).
16. Cite properly:
    - Inline footnote-style markers `[¹]`, `[²]`… with a **引用来源** / **参考文献** list at the end (author, title, edition/publisher, year; for Wikisource, the text + edition note; for web, site + title + access date).
    - For text you quote verbatim, quote exactly (including chapter/回目), and give the source immediately.
    - Include an access date (今日日期) for web sources.

### Phase 4 — Corrections doc (conditional)

17. Quality control is the goal; the corrections doc is only the evidence. If every claim verifies against ≥2 independent sources, **no corrections doc is created** — do not manufacture one to "complete" the workflow.
18. Anything you could not verify, or that contradicts reliable sources, goes into `docs/YYMMDD-corrections-by-citation.md` (reuse today's date if none exists). Structure per the example `docs/260808-corrections-by-citation.md`: 校核总表 (table), 已修正逐条明细 (with 依据), 待核实清单, 引用来源清单.
19. If the article already has a corrections doc, append to it rather than creating a duplicate.

## Repo conventions (from AGENTS.md)

- Filenames: `docs/<YYMMDD>-<slug>.md`, lowercase hyphenated slug, 6-digit date prefix, no spaces. Images: `imgs/<YYMMDD>-<slug>.<ext>` (same date prefix). Reference images as `../imgs/<file>`.
- Update `README.md` (both the English and 中文 index tables) whenever an article or corrections doc is added, moved, or removed.
- This directory belongs to the parent `negtivSpace` repo — no nested `.git`.
- Do not create a corrections doc unless there is something to record.

## Verification checklist (run before finishing)

- [ ] The user's thought-flow is preserved: same order, same points, same conclusions; no silent restructuring.
- [ ] Every historical/literary claim has ≥2 independent reliable sources (from the trusted list); citations are attached to the specific claim.
- [ ] **Every cited source was actually opened and the supporting sentence was located in its content** — no citation rides on a claim the source does not state.
- [ ] The ≥2 sources are genuinely independent (not copies of one another); no ghost citations (plausible-looking titles or quoted sentences that exist nowhere).
- [ ] Every quoted sentence was searched on the web and surfaced in a primary text or an independently-verifiable source — nothing fabricated.
- [ ] Primary-text quotations match the original wording and chapter.
- [ ] No claim from untrusted sources (微博/微信/头条/抖音/个人博客) is treated as evidence.
- [ ] Unverifiable items are in the corrections doc under "待核实", not asserted in the article.
- [ ] If the user asked to be shown what changed, summarize: added support, corrected facts (before→after), and flagged items.
- [ ] Filename follows `YYMMDD-slug`; images referenced as `../imgs/<file>`; README is in sync; word count stated in the article matches the actual CJK character count (verify with a script, not by eye).
- [ ] Nothing committed unless the user explicitly asks.

## Error handling

- **User's draft conflicts with reliable sources**: show the user the discrepancy and both sides' evidence; propose the fix; wait for approval.
- **Source is paywalled / unavailable**: rely on the other independent source and note the gap in the corrections doc.
- **Ambiguous structure in the user's notes**: ask — do not guess the outline.
- **No reliable source found**: treat the claim as 待核实, do not assert it, tell the user explicitly.
