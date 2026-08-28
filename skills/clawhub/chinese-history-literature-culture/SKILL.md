---
name: chinese-history-literature-culture
description: >
  Write, polish, and cite Chinese-language articles on Chinese history,
  literature, and culture (Five Dynasties & Ten Kingdoms, silk, Dream of the
  Red Chamber, 洛神赋, 脂砚斋, etc.). Use when the user shares their own
  outline, notes, or stream-of-thought for a 中文历史/文学/文化 article and
  wants the agent to follow that thought-flow (must), expand with web
  research,   and produce a polished, well-cited draft. Output is in Chinese
  (simplified by default); source material may be in any language. Covers
  creation, polishing, fact-checking, and source selection.
---

# 中文历史·文学·文化写作 (Chinese History / Literature / Culture Writing)

Write, polish, and cite Chinese articles about Chinese history, literature, and culture. The user supplies the thinking; you supply the structure-faithful expansion, web research, and citations. Output is in Chinese (simplified by default); source material may be in any language.

This skill complements `astro-sync` (publishing). Writing happens here; publishing happens there.

## Golden rules

1. **Follow the user's thought-flow — must.** The user's outline, sequencing, analogies, claims, and conclusions are the skeleton. Preserve them. Never silently rearrange the user's structure into a generic essay template, never drop their points, and never swap in your own thesis.
2. **Keep their voice.** Polish wording and grammar, but do not flatten the user's tone into a house style. A personal, essayistic voice stays a personal, essayistic voice.
3. **Cite, don't assert.** Every historical or literary claim gets checked against at least two independent, reliable sources. Anything that cannot be verified is NOT asserted in the article; it goes into the batch corrections doc under "待核实" (see AGENTS.md → Working rules → Verify facts before publishing).
4. **Flag before replacing.** If the user's thought contains a factual error, keep their intent, propose the corrected wording, and get explicit approval before swapping it in (AGENTS.md: "Get approval before any change").
5. **Never cite a source you have not opened and checked.** A "source" that is merely indexed in search results, or that lives on a trusted domain but does not actually contain the claimed sentence, is not a source — it is a ghost citation. Every citation must be verified against the source's actual content (see Phase 3).

## Inputs

- `source` — the user's raw text: an outline, bullet notes, a stream of thought, or a rough draft. May be pasted directly or given as a file path.
- `mode` — what the user wants this run:
  - `create` — turn notes/thoughts into a full article.
  - `polish` — improve an existing draft (grammar, flow, clarity, style) while preserving structure and voice.
  - `cite` — add/verify citations for an existing article (may combine with polish). Default: follow whatever the user asked; ask if unclear.
- `audience` / `tone` — optional; e.g. "general readers", "academic-leaning", "blog-style". Default: general literate audience.

## Source quality — trusted vs. untrusted

**Trusted** (meet the ≥2-sources rule):
- Primary-text archives: Wikisource (维基文库) — classical texts, 二十四史, 诗文集, 白话小说原文.
- Official academic institutions: 中国社科院考古研究所 kaogu.cn, 中国社会科学网 cssn.cn, 故宫博物院, 国家图书馆, university presses.
- Academic presses & canonical editions: 中华书局 (点校本二十四史, 《南唐二主词校订》等), 上海古籍出版社, 人民文学出版社, 商务印书馆.
- Wikipedia entries (维基百科) that carry references.
- Peer-reviewed journals / academic databases (中国知网 CNKI, ResearchGate).

**NOT trusted** (never count as evidence): 微博 / WeChat / 头条 / 抖音 / TikTok / 哔哩哔哩弹幕 / personal blogs / 百度百科 无参考文献词条 / forum posts / AI chat outputs.

## Workflow

### Phase 1 — Understand the thought-flow (do not skip)

1. Read the user's input end to end.
2. Extract and restate the user's **own** structure back to them: main sections, key claims, and the connecting logic. List anything you plan to add, cut, or move.
3. Confirm with the user before writing the article, unless they asked for an immediate draft and the structure is unambiguous.

### Phase 2 — Research & source curation

For each claim that needs support (dates, events, attributions, quotations, chapter references, terminology):

4. **Search the web** for each fact independently. Prefer site-restricted queries against trusted domains, e.g. `site:zh.wikisource.org 洛神赋` or `kaogu.cn 钱山漾 年代`.
5. **Cross-check with at least two independent, reliable sources.** When the sources disagree, record the discrepancy in the corrections doc rather than silently picking a side.
6. **Prefer primary text over commentary.** For classical works (洛神赋, 红楼梦, 旧五代史, 人间词话, 诗经, 全宋词…), quote from the primary text where possible (Wikisource scans/editions, 中华书局点校本), and verify the exact wording and chapter (回目) number. When a fact appears in both a primary text and a secondary commentary, cite the primary text; the commentary may be wrong or derivative.
7. For literature, verify **chapter attributions against the original text**, not memory: e.g. for《红楼梦》刘姥姥一进荣国府=第六回, 元妃省亲=第十八回; for《诗经》check poem titles against《毛诗正义》; for五代史料 verify episode numbers against《旧五代史》or《新五代史》.
7a. **Know when one source suffices.** Well-established facts in primary texts (e.g. a poem's exact wording in Wikisource, a chapter number in《红楼梦》) need only one verified source. Reserve the ≥2-source requirement for contested claims, interpretive assertions, and historical attributions.
7b. **《红楼梦》: know the version systems before attributing anything.** The work survives in two textual families whose 回目 AND 正文 both differ: the 脂评抄本系统 (甲戌/己卯/庚辰…, all ending at chapter 80) and the 程高本系统 (程甲/程乙, 120 chapters, 后四十回 compiled by 程伟元/高鹗). Consequences:
    - **脂批 ceiling**: 脂砚斋 commentary exists only for the first eighty chapters. Any claimed 脂批 on a 后四十回 event (焚稿、妙玉被掠、宝玉出家…) is automatically suspect — reject unless a specific 本 + 回数 is named.
    - **Name the edition when quoting**: e.g. the 第四十一回 回目 is「栊翠庵茶品梅花雪　怡红院劫遇母蝗虫」in 庚辰本 but「贾宝玉品茶栊翠庵」in 程甲本; the《警幻仙姑赋》has 异文 across editions (待止而欲行 / 欲止而仍行；秋菊被霜 / 秋蕙披霜). State which system you quote from; where readings differ, record the variant instead of silently picking one.

**Fetching primary texts — practical tips** (learned the hard way):
- Wikisource《红楼梦》chapter pages use zero-padded titles: `紅樓夢/第041回` works; non-padded forms (`第四十一回`) 404. URL-encode the Chinese title path.
- Some Chinese text sites serve GBK and come back as mojibake through web fetch (e.g. purepen.com). Do not fight them — fall back to another host carrying the same text: zh.wikisource.org, 识典古籍 (shidianguji.com), 古文岛 (guwendao.net), 国学梦 (guoxuemeng.com).
- For 脂本 extent and 回目 lists, publisher catalogue pages (e.g. 国家图书馆出版社 nlcpress.com for 庚辰本) are a reliable quick check.

### Phase 3 — Source verification (verify the truth)

A trusted domain is not proof. The claim must be **actually present in the source's content**, not merely plausibly attributed to it. For every claim:

8. **Open each source and locate the exact passage.** Fetch the page (wikisource, kaogu.cn, cssn.cn, Wikipedia article body, etc.) and confirm the specific sentence or data point appears there verbatim or in substance. If you cannot retrieve the full content, you may not cite it — put it in 待核实.
9. **Match claim ↔ source one-to-one.** Pair every fact in the draft with the exact sentence(s) that support it in each source. If a source does not actually say what the draft claims, drop that source or fix the claim; do not keep a citation next to a claim it does not support.
10. **Check source independence.** Two sources that copy one another (e.g. an article, a WeChat re-post, and a blog all reproducing the same 维基百科 text; or a Wikipedia entry whose only references are the very claim sites) count as ONE source, not two. Look for genuinely independent origins — a primary text, an academic paper, an official institution report.
11. **Watch for ghost citations.** A citation is suspicious if: the title looks plausible but no copy exists; the quoted sentence cannot be found anywhere in the cited work; or search returns only secondary mentions. AI-generated and memory-invented citations (e.g. 爱国书社1927, 中华书局 《李煿词作赏析》) must be detected and removed — see `docs/260808-corrections-by-citation.md` for worked examples.
11a. **Treat high-risk claim types as unverified until found verbatim.** In AI-drafted literary articles, three patterns are fabricated most often: (i) character dialogue ("X 对 Y 说：……"); (ii) usage statistics about an author or text ("脂砚斋评注中最常出现的词汇是痴/绝/悲/幽"); (iii) 批语归因 — attributing an unnamed paraphrase to a commentator without 本 + 回数. Each must be located word-for-word in the primary text or named edition before it stays in the draft; otherwise it goes to 待核实 (see `docs/260822-corrections-by-citation.md` rows 3–11 for worked examples).

### Phase 4 — Write / polish

12. Write in Simplified Chinese by default (Traditional only if the source or user's draft is Traditional). Follow the user's section order and emphasis. Expand their points with researched detail; mark each fact-supported sentence with a citation marker.
13. **Remove duplication.** Each fact should appear only once per entry. After writing a section, read it end-to-end and cut any sentence that restates information already present — whether in a biographical one-liner, an analysis paragraph, the introduction, or the conclusion. Common patterns: biographical context repeating the analysis paragraph, the结语 echoing the introduction, or two paragraphs in the same entry making the same point with different words.
14. Use precise terminology with first-use glosses where helpful (e.g. 包衣 = 内务府奴仆/皇室世仆, 软烟罗 vs 蝉翼纱). Annotate uncommon characters with pinyin on first use using `字（pinyin）` format — e.g. 杕杜（dì dù）、蝃蝀（dì dōng）、隮（jī）、淇（qí）、滺滺（yōu yōu）、桧（guì）、睆（huàn）、菅（jiān）、澌（sī）、钏（chuàn）. Do not annotate common characters or characters already widely known to the target audience.
15. **Maintain structural consistency.** All entries in a list-style article should use the same heading level (e.g. all `##`). Do not use labels that imply hierarchy (附录, 补充) unless the user explicitly requests them. If the article has a conclusion (结语), place it at the very end — never in the middle. The introduction should not announce a two-tier structure (main body + appendix) unless the user's thought-flow explicitly designs one. Maximum heading depth is `###`; anything deeper becomes bold run-in labels (`**小标题**` on its own line, or `**标签**：` leading a list/paragraph) rather than numbered `####` headings — no 4.2.3-style levels.
16. Cite properly:
    - Inline footnote-style markers `[¹]`, `[²]`… with a **引用来源** / **参考文献** list at the end (author, title, edition/publisher, year; for Wikisource, the text + edition note; for web, site + title + access date).
    - For text you quote verbatim, quote exactly (including chapter/回目), and give the source immediately.
    - Include an access date (今日日期) for web sources.

### Phase 5 — Corrections doc (conditional)

17. Quality control is the goal; the corrections doc is only the evidence. If every claim verifies against ≥2 independent sources, **no corrections doc is created** — do not manufacture one to "complete" the workflow.
18. Anything you could not verify, or that contradicts reliable sources, goes into `docs/YYMMDD-corrections-by-citation.md` (reuse today's date if none exists). Structure per the example `docs/260808-corrections-by-citation.md`: 校核总表 (table), 已修正逐条明细 (with 依据), 待核实清单, 引用来源清单.
19. If the article already appears in an older corrections doc, cross-reference the prior fixes by doc + row number (e.g. 「260808 #35」) instead of re-litigating settled items. Create a new dated doc only when this audit is a separate pass over the article (e.g. a re-review with a different focus); build on the old rows you rely on, and keep the 处置分类 (①已修正 / ②待核实 / ③已核对) consistent across docs.

### Phase 6 — Post-writing citation audit

After the article is complete, verify every citation and quoted reference:

20. **Search each quoted sentence on the web.** Take every verbatim quote (classical poetry, historical texts, primary sources) and search it in full or by its distinctive clause. Confirm it surfaces in the primary text or independently-verifiable sources.
21. **Verify exact wording.** Classical texts often have variant editions. Confirm the quote matches the edition you cite (e.g. 中华书局点校本 vs. Wikisource). If the user's source uses a different reading, note the variant rather than silently "correcting" it.
22. **Check attribution accuracy.** Confirm the quoted line actually comes from the work you attribute it to (author, title, chapter/回目). Misattribution is common — verify against the primary text, not secondary commentary.
23. **Apply corrections.** If any citation is inaccurate (wrong character, wrong source, wrong attribution), fix the article and record the change in the corrections doc per Phase 5. After fixing, re-check the affected section for duplication or flow breaks (Phase 4).

## Repo conventions (from AGENTS.md)

- Filenames: `docs/<YYMMDD>-<slug>.md`, lowercase hyphenated slug, 6-digit date prefix, no spaces. Images: `imgs/<YYMMDD>-<slug>.<ext>` (same date prefix). Reference images as `../imgs/<file>`.
- Update `README.md` (both the English and 中文 index tables) whenever an article or corrections doc is added, moved, or removed.
- This directory belongs to the parent `negtivSpace` repo — no nested `.git`.
- Do not create a corrections doc unless there is something to record.

## Verification checklist (run before finishing)

- [ ] **Phase 1**: User's thought-flow preserved — same order, same points, same conclusions; no silent restructuring.
- [ ] **Phase 2**: Every historical/literary claim has ≥2 independent reliable sources; primary texts preferred over commentary; chapter attributions verified against original; 《红楼梦》claims respect the 脂批 ch80 ceiling and name their edition (脂本 vs 程高本).
- [ ] **Phase 3**: Every cited source was actually opened and the supporting sentence was located; sources are genuinely independent; no ghost citations; dialogue quotes, usage statistics, and 批语归因 located verbatim in a primary text or named edition.
- [ ] **Phase 4**: No fact is stated twice within the same entry (biographical context, analysis paragraph, introduction, or conclusion); no sentence in the conclusion restates the introduction word-for-word.
- [ ] **Phase 6**: Post-writing citation audit completed — every quote verified against primary source, exact wording confirmed, attributions checked.
- [ ] No claim from untrusted sources (微博/微信/头条/抖音/个人博客) is treated as evidence.
- [ ] Unverifiable items are in the corrections doc under "待核实", not asserted in the article.
- [ ] If the user asked to be shown what changed, summarize: added support, corrected facts (before→after), and flagged items.
- [ ] Uncommon characters annotated with pinyin on first use; common/known characters left unannotated.
- [ ] Filename follows `YYMMDD-slug`; images referenced as `../imgs/<file>`; README is in sync; word count stated in the article matches the actual CJK character count (verify with: `python3 -c "import re; print(len(re.findall(r'[\u4e00-\u9fff]', open('FILE').read())))"`).
- [ ] Nothing committed unless the user explicitly asks.

## Error handling

- **User's draft conflicts with reliable sources**: show the user the discrepancy and both sides' evidence; propose the fix; wait for approval.
- **Sources conflict and neither is clearly right**: record both versions in the corrections doc under "待核实"; do not silently pick one side. Present the conflict to the user with the evidence for each.
- **Source is paywalled / unavailable**: rely on the other independent source and note the gap in the corrections doc.
- **Ambiguous structure in the user's notes**: ask — do not guess the outline.
- **No reliable source found**: treat the claim as 待核实, do not assert it, tell the user explicitly.
- **Article is too long for target format**: ask the user which sections to trim or merge; do not silently cut content. If trimming is needed for blog publishing, use the `astro-sync` skill's length conventions as a guide.
