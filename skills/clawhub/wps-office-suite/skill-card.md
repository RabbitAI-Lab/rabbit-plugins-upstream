## Description:

WPS Office Suite helps agents automate Word, Excel, PowerPoint, document conversion, templates, AI-assisted text workflows, meeting summaries, reports, and local Office engine selection across WPS, Microsoft Office, LibreOffice, and pure Python modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, students, and developers use this skill to create, edit, analyze, translate, convert, and generate office documents from agent-driven commands. It is suited to workflows that need local Office automation with optional AI assistance for text, reports, translation, formulas, and meeting notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive document, contract, invoice, meeting audio, or regulated data may leave the local process through AI/router paths or an OpenAI-compatible endpoint.

Mitigation: Review AI features before installation, use local-only modes for confidential data, and route content only through approved endpoints.

Risk: The release-all health action can perform forceful local Office cleanup while unsaved documents are open.

Mitigation: Save and close Office documents before running release-all, and avoid forceful cleanup unless the impact is understood.

Risk: Feedback email generation can include system and environment details.

Mitigation: Inspect generated feedback emails before sending and remove any sensitive environment information.

Risk: Office automation and format conversion can alter important files or lose complex formatting.

Mitigation: Back up important files before modification and review generated or converted documents before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [README](artifact/README.md)
- [Architecture](artifact/ARCHITECTURE.md)
- [Skill definition](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON command results, and generated office files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local DOCX, XLSX, PPTX, PDF, TXT, CSV, and template files.]

## Skill Version(s):

4.9.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
