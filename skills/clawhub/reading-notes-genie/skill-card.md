## Description:

閱讀筆記精靈：輸入書名 / 上傳 PDF 或 EPUB，AI 自動生成章節摘要、精華語錄、讀書心得、知識點卡片，並匯出成 Markdown、Anki 卡片、PDF 等多種格式。差異化：結構化輸出而非普通摘要。

This skill is ready for commercial/non-commercial use.

## Publisher:

[xuan905](https://clawhub.ai/user/xuan905)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to turn book titles, PDFs, or EPUBs into structured reading notes, chapter summaries, quotations, reflections, and review cards. It is intended for workflows that export notes to Markdown, JSON, Anki formats, or PDF reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded or extracted book text can be sent to OpenAI, Anthropic, or a configured local model endpoint.

Mitigation: Use offline mode for sensitive material, or explicitly configure only a trusted provider and endpoint.

Risk: A remote LOCAL_MODEL_URL can receive source text if configured.

Mitigation: Keep LOCAL_MODEL_URL pointed at a trusted local service unless remote processing is intended.

Risk: Generated notes, quotations, cards, and reports may contain verbatim excerpts from copyrighted or proprietary source documents.

Mitigation: Review generated outputs before sharing and avoid processing restricted content without permission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/xuan905/skills/reading-notes-genie)
- [Python 3.9+](https://python.org)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown, JSON, Anki text/APKG, and PDF files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include quoted source excerpts and can be generated with OpenAI, Anthropic, local model endpoints, or offline keyword extraction.]

## Skill Version(s):

1.0.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
