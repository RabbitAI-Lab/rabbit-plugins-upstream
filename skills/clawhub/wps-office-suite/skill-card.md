## Description:

WPS Office Suite helps agents automate Word, Excel, PowerPoint, format conversion, document search, watermarking, redaction, templates, and office workflow tasks across WPS Office, Microsoft Office, LibreOffice, and pure Python modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to create, edit, analyze, convert, search, and manage office documents through agent-generated commands and guidance. It is suited for office productivity workflows that need local or configurable document automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive documents may be processed through optional external LLM or cloud modes.

Mitigation: Use local modes for sensitive content unless the endpoint, credentials, and data-handling policy are trusted.

Risk: Opening search results from shared or untrusted folders can expose unsafe files.

Mitigation: Avoid doc_search --open on shared or untrusted folders and restrict search paths to trusted directories.

Risk: Watch rules and scheduled tasks can run long-lived automation.

Mitigation: Inspect YAML watch rules and scheduled task definitions before enabling automation.

Risk: Office automation and format conversion can modify files or lose complex formatting.

Mitigation: Back up important documents and review generated or converted files before distribution.

## Reference(s):

- [WPS Office Suite on ClawHub](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [gongwen_rules.yaml](references/gongwen_rules.yaml)
- [Contract review skill](https://skillhub.cn/skills/contract-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated office documents or supporting JSON when relevant]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify Word, Excel, PowerPoint, PDF, text, template, watermark, redaction, and search index files depending on the selected workflow.]

## Skill Version(s):

5.2.5 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
