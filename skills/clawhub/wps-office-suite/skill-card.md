## Description:

WPS Office Suite helps agents create, edit, analyze, translate, convert, and generate Word, Excel, PowerPoint, PDF, Markdown, and meeting-minute documents using WPS, Microsoft Office, LibreOffice, or pure Python engines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to automate local office-document workflows such as document creation, spreadsheet analysis, presentation generation, format conversion, translation, contract review, and meeting-minute generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify local office documents and process document folders.

Mitigation: Use explicit input and output paths, keep backups of important files, and review generated or modified documents before relying on them.

Risk: The skill can forcibly close Office processes through cleanup commands.

Mitigation: Avoid release-all or force cleanup commands unless Office processes can be safely closed without losing work.

Risk: Optional ASR and LLM methods may send documents or recordings to the configured external provider.

Mitigation: Use external ASR or LLM methods only for content approved for that provider, and prefer local modes for sensitive documents or recordings.

Risk: Format conversion and automation may lose complex formatting or produce imperfect document structure.

Mitigation: Review converted files and generated presentations, especially when preserving original layout is important.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [README](artifact/README.md)
- [Architecture](artifact/ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON-like command results, and generated or modified office-document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include local document edits, converted files, generated templates, analysis summaries, translation results, and troubleshooting guidance.]

## Skill Version(s):

4.7.0 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
