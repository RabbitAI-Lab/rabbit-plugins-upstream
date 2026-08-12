## Description:

WPS Office Suite helps agents create, edit, analyze, convert, and troubleshoot Word, Excel, PPT, meeting-minute, and office-document workflows using WPS Office, MS Office, LibreOffice, or pure Python engines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, office workers, and agent operators use this skill to automate local document creation, editing, analysis, conversion, template generation, meeting-minute creation, and Office/WPS environment checks. It is suited for workflows that need generated files, command guidance, or structured troubleshooting around Word, Excel, PPT, PDF, and audio-to-minutes tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports under-disclosed cloud data transfer through optional ASR or LLM modes.

Mitigation: Use explicit local-only options for confidential content and avoid cloud ASR or external LLM modes for sensitive meetings or documents.

Risk: The skill can perform powerful local document and application-control actions.

Mitigation: Review commands before execution, operate only on intended files, and keep backups of important documents before automated edits or conversions.

Risk: COM cleanup and release-all commands may close or kill WPS or Office processes.

Mitigation: Run COM cleanup only after saving work and confirm that closing Office/WPS processes is acceptable for the current session.

Risk: Backups may be created under WPS_Backup and contain document contents.

Mitigation: Review and manage WPS_Backup files according to the sensitivity and retention needs of the source documents.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [README.md](artifact/README.md)
- [ARCHITECTURE.md](artifact/ARCHITECTURE.md)
- [SKILL.md](artifact/SKILL.md)
- [Tesseract OCR reference](https://github.com/UB-Mannheim/tesseract/wiki)
- [LibreOffice](https://www.libreoffice.org/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated office files such as DOCX, XLSX, PPTX, PDF, CSV, TXT, HTML, JSON, and meeting-minutes documents]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify local office files, generated templates, health-check JSON, backups under WPS_Backup, and converted document outputs.]

## Skill Version(s):

4.5.0 (source: SKILL.md frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
