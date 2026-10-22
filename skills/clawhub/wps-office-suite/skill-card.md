## Description:

Automates creation, editing, analysis, and conversion of Word, Excel, and PowerPoint documents using available office software or Python tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams use this skill to create, edit, analyze, format, and convert office documents, including spreadsheets and presentations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An optional document-search open action can execute unsafe shell commands when filenames are controlled by others.

Mitigation: Avoid search --open in directories with untrusted filenames until the shell invocation is replaced with argument-vector execution.

Risk: Document operations can read or change local files, including important originals.

Mitigation: Review file targets and keep backups before running edits or conversions.

Risk: Optional cloud or LLM integrations can send document content externally, and scheduling can run tasks later.

Mitigation: Review configured external services and scheduled tasks before enabling them; use local processing for sensitive documents.

## Reference(s):

- [WPS Office Suite release](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [Government document formatting rules](artifact/references/gongwen_rules.yaml)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance and commands; optional JSON command results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can create or modify local office documents.]

## Skill Version(s):

5.3.5 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
