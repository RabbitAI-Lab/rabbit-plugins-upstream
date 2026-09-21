## Description:

WPS Office Suite helps agents create, edit, convert, analyze, format, watermark, redact, search, and summarize Word, Excel, and PowerPoint documents using WPS Office, Microsoft Office, LibreOffice, or pure Python fallbacks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can use this skill to automate common office-document workflows, including document creation, spreadsheet analysis, presentation generation, format conversion, public-document formatting, watermarking, redaction, and local document search.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify local office documents across broad workflows.

Mitigation: Back up important files before running document edits, conversions, watermarking, redaction, or batch operations.

Risk: Optional cloud, LLM, and memory or indexing paths can expose document contents outside a purely local workflow.

Mitigation: Use local-only modes for sensitive files, avoid untrusted LLM endpoints, and enable upload, memory, or deposit features only after confirming the destination.

Risk: Directory watching and scheduled automation can repeatedly process files or run commands without close supervision.

Mitigation: Review watch rules and scheduled commands before enabling them, and avoid force options unless the automation behavior is fully understood.

Risk: Complex office-format conversions can lose formatting or produce incomplete output.

Mitigation: Review converted documents before relying on them and keep the original source files available for rollback.

## Reference(s):

- [GB/T 9704 public-document formatting rules](artifact/references/gongwen_rules.yaml)
- [Contract Review skill interlink](https://skillhub.cn/skills/contract-review)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-oriented guidance for generating or modifying office documents and related files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local document files, conversion outputs, indexes, redaction manifests, watermarked files, and status messages depending on the selected workflow.]

## Skill Version(s):

5.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
