## Description:

拆书家技能。输入一本书（PDF/EPUB/TXT/Markdown/书名/链接），输出结构化拆书笔记（总概括+核心提炼+逐章拆解+行动清单），并可一键生成美观的可视化 HTML 拆书报告。适合读书笔记、知识提炼、快速掌握一本书、做课程分享、写书评等场景。触发词：拆书、读书笔记、这本书讲了什么、帮我读一本书、书摘提炼、book breakdown、读书报告。

This skill is ready for commercial/non-commercial use.

## Publisher:

[yysws5566](https://clawhub.ai/user/yysws5566)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, educators, writers, and knowledge workers use this skill to turn a book, book file, title, link, or chapter request into structured reading notes, core concept extraction, chapter breakdowns, and action checklists. It can also produce Markdown notes and a self-contained visual HTML book report when requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may create Markdown or HTML book-note files in the workspace.

Mitigation: Review proposed filenames and destinations before allowing file creation, especially when working in shared or sensitive workspaces.

Risk: The skill may search online for book metadata, reviews, ratings, author background, and table-of-contents information by default.

Mitigation: For private manuscripts, confidential PDFs, or sensitive reading lists, request offline-only processing or pure text output.

Risk: Generated summaries can omit nuance or reflect incomplete source extraction.

Mitigation: Check chapter/page references and any uncertainty notes before using the output for teaching, publication, or decision-making.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yysws5566/skills/book-breakdown)
- [Publisher profile](https://clawhub.ai/user/yysws5566)
- [HTML report template](artifact/templates/book-report-template.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, configuration, guidance]

**Output Format:** [Markdown, plain text, and self-contained HTML report files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create workspace book-note files and may use online book metadata unless the user asks for offline-only processing.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
