## Description:

WPS Office Suite helps agents automate local office workflows across WPS Office, Microsoft Office, LibreOffice, and pure Python modes, including document creation, editing, conversion, spreadsheet analysis, chart generation, document translation, meeting minutes, and COM health checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, students, and office automation developers use this skill to create, edit, analyze, translate, convert, and manage Word, Excel, PowerPoint, PDF, and related office files through agent-guided commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can modify local documents, create backup copies, and perform high-impact office automation actions.

Mitigation: Run it on copies of important files, keep backups, and review generated or modified documents before relying on them.

Risk: Document, audio, or transcript content may be sent to external services when cloud translation, speech, or LLM methods are explicitly selected.

Mitigation: Use local-only methods for sensitive content and opt into cloud methods only after confirming data-flow and credential implications.

Risk: COM release and force-cleanup actions can close or disrupt WPS or Microsoft Office applications.

Mitigation: Save open documents and avoid force cleanup while unsaved Office or WPS files are open.

Risk: Format conversion or complex office automation may lose layout fidelity or produce incorrect outputs.

Mitigation: Inspect converted files and validate analyses, formulas, charts, and generated presentations before distribution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [README](README.md)
- [Skill definition](SKILL.md)
- [Architecture overview](ARCHITECTURE.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline shell commands, JSON-like command results, and generated or edited office files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can create or modify local Word, Excel, PowerPoint, PDF, CSV, template, transcript-derived, and translated files when the user runs the generated commands.]

## Skill Version(s):

4.6.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
