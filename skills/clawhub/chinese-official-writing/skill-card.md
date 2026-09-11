## Description:

用于中文公文、事务性材料和新闻稿件的起草、改写、压缩和复核，并按文种、行文关系、格式和事实边界检查正式中文材料。

This skill is ready for commercial/non-commercial use.

## Publisher:

[gongyu0918-debug](https://clawhub.ai/user/gongyu0918-debug)

### License/Terms of Use:

MIT

## Use Case:

Employees, external users, and teams that prepare Chinese official documents use this skill to draft, revise, compress, review, and format formal workplace materials such as requests, reports, notices, letters, meeting minutes, rules, speeches, research summaries, news copy, and AI-compute review materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated official-document drafts may contain unsupported factual claims if the user provides sparse or ambiguous source material.

Mitigation: Review factual claims, dates, amounts, organizations, approvals, and required document elements against user-provided source material before official use.

Risk: The optional local linter processes DOCX, text, and Markdown drafts and may be unsuitable for untrusted or very large files.

Mitigation: Use the optional linter only on trusted, appropriately sized files and treat its findings as review signals rather than automatic edits.

Risk: Optional hooks are documented separately and are outside the base skill's automatic install path.

Mitigation: Review the hook documentation and enable hooks only in a supported host environment after confirming their behavior.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/gongyu0918-debug/skills/chinese-official-writing)
- [README](README.md)
- [Reference Index](references/reference-index.md)
- [Information Selection](references/information-selection.md)
- [Genre Routing](references/genre-routing.md)
- [Final Review Layers](references/final-review-layers.md)
- [GB/T 9704 Formatting](references/format-gbt9704.md)
- [Hook Usage Documentation](https://github.com/gongyu0918-debug/chinese-official-writing-skill/blob/main/chinese-official-writing/hooks/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, code, shell commands, configuration]

**Output Format:** [Plain text or Markdown, with optional code blocks or shell commands for linting and document workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for human review before official use; the optional local linter reports language, format, and repetition risks but does not automatically rewrite drafts.]

## Skill Version(s):

1.6.33 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
