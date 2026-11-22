# Overview (English)

## Overview (English)

Do not open with "here is the main content". First decide what the reader will *do* with it, choose one of five output format families, then compress under fidelity rules.

| Reader's purpose | Format family |
|---|---|
| After a meeting, who does what | Minutes |
| Choose among several options | Comparison |
| Explain how something evolved | Timeline |
| Scan and forward quickly | Bullets |
| Archive as a knowledge card | Card |

**Three hard rules.** Nothing absent from the source is written. Every figure is copied verbatim. Conditions are never compressed away.

**What is machine-checkable (v2.0).**

| Command | What it proves | Output |
|---|---|---|
| `python scripts/summarize_pro.py extract --file doc.md` | Which facts the source actually contains: dates, figures, speakers, action items, decisions, conditionals | Skeleton + fact list |
| `python scripts/summarize_pro.py citecheck --file out.md --source doc.md` | Every sentence in your draft is traceable to the source; untraceable ones are listed | Traceability report |
| `python scripts/summarize_pro.py selfcheck --file out.md --format minutes` | The chosen format family carries all required sections | `PASS` / `FAIL` + missing elements |

Run `python tests/run_golden.py` for the 10-case golden set (10/10 PASS locally) and `python demo/run_demo.py` for the end-to-end proof, which deliberately corrupts a figure and a date to show they are caught. Standard library only, no network.

**中文正文如下。**

# 增强版内容总结：先选格式，再守忠实

拿到一篇长文、一段录音转写、一堆聊天记录时，**不要上来就写「主要内容如下」**。先按用户要的「用途」选对输出格式族，再按忠实性纪律压缩。
