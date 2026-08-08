## Description:

党政机关公文标准排版与质检校对技能，依据 GB/T 9704-2012 将 Markdown、TXT、DOCX 或带文本层的 PDF 草稿转换为 Word 公文，检查 .docx 格式合规性，并按规则进行文风净化。

This skill is ready for commercial/non-commercial use.

## Publisher:

[chesaram](https://clawhub.ai/user/chesaram)

### License/Terms of Use:

MIT-0

## Use Case:

Public-sector staff, administrative assistants, and agents supporting them use this skill to format Chinese official-document drafts, inspect Word documents for GB/T 9704-2012 formatting issues, and produce reviewable style-cleaning reports. It is intended for formatting, quality checking, and surface wording cleanup, not for drafting official content or validating facts.

### Deployment Geography for Use:

Global, for users preparing Chinese official documents under GB/T 9704-2012.

## Known Risks and Mitigations:

Risk: The skill reads user-provided documents and writes Word or report outputs locally.

Mitigation: Provide only files intended for processing, choose output paths deliberately, and review generated documents and reports before relying on them.

Risk: Style-cleaning can change surface wording based on fixed rules, which may affect exact official phrasing.

Mitigation: Review the style-cleaning report before accepting wording changes, and use dry-run or review-only behavior when exact language matters.

Risk: The skill checks format and style but does not validate facts, policy authority, document substance, or institutional approval requirements.

Mitigation: Have the responsible human reviewer confirm factual content, policy basis, issuing authority, and unit-specific formatting rules before release.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/chesaram/skills/gongwen-format-pro)
- [GB/T 9704-2012 Parameter Reference](artifact/references/gb9704-2012.md)
- [Quality Check Checklist](artifact/references/qc-checklist.md)
- [Style-Cleaning Rules](artifact/references/style-guide.md)
- [CLI Reference](artifact/references/cli-reference.md)
- [FAQ](artifact/references/faq.md)

## Skill Output:

**Output Type(s):** [files, markdown, shell commands, configuration, guidance]

**Output Format:** [DOCX files, Markdown reports, JSON configuration, and concise text guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs local scripts against user-provided documents and may produce Word files, quality-check reports, style-cleaning reports, backups, and configuration-driven outputs.]

## Skill Version(s):

1.0.1 (source: server release evidence and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
