## Description:

Formats PRC party and government official-document drafts into GB/T 9704-2012 Word documents, checks existing .docx files for format issues, and cleans draft prose into formal government-document style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

External ClawHub users, document-preparation staff, and agents use this skill to turn user-provided official-document drafts into formatted Word files, run GB/T 9704-2012 format checks, and produce prose-cleanup reports. It is intended for formatting, checking, and style cleanup, not for drafting official content or validating facts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad triggers and fallback routing may cause the agent to run formatting or cleanup scripts before the user's intent is fully clear.

Mitigation: Confirm the intended mode before processing real documents, especially when the request is vague or the file contains sensitive material.

Risk: Style cleanup can rewrite user-provided text and may affect official wording if used without review.

Mitigation: Run style cleanup in report or dry-run form first, review automatic replacements, and require human confirmation for flagged terms.

Risk: The skill writes local files and may overwrite existing outputs.

Mitigation: Use explicit output paths, review generated backups, and avoid running on the only copy of an important draft.

Risk: PDF input or export can add document-handling risk when files are untrusted.

Mitigation: Use PDF export or PDF input only for documents the user trusts, and prefer editable .docx, .md, or .txt sources when possible.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/gongwen-format-pro)
- [Publisher Profile](https://clawhub.ai/user/chesaram)
- [GB/T 9704-2012 参数速查](references/gb9704-2012.md)
- [公文格式质检项清单](references/qc-checklist.md)
- [公文文风净化规则说明](references/style-guide.md)
- [脚本参数手册](references/cli-reference.md)
- [常见问题（FAQ）](references/faq.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [DOCX files, Markdown reports, JSON results, and concise user-facing status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local output files such as formatted .docx documents, style reports, quality-check reports, and backups of overwritten outputs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
