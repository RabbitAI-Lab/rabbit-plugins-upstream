## Description:

WPS Office Suite helps agents automate Word, Excel, PPT, document conversion, document analysis, translation, meeting notes, reports, and email replies through local office engines, LibreOffice, pure Python fallbacks, and opt-in external AI services.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, students, and productivity-focused developers use this skill to create, edit, convert, analyze, translate, and summarize Office documents while selecting the available local or fallback document engine.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access and modify sensitive local Office documents and meeting content.

Mitigation: Run it only on documents you are authorized to process, review outputs before reuse, and keep backups before commands that edit, convert, overwrite, or clean up files.

Risk: Some commands can launch local applications, overwrite files, or terminate Office processes.

Mitigation: Close unrelated Office work before running automation, use explicit input and output paths, and avoid cleanup or process-release commands while unsaved documents are open.

Risk: External LLM or ASR methods may send document, email, or meeting content to configured services.

Mitigation: Use local or template modes for confidential content unless the endpoint, credentials, retention policy, and data handling requirements have been verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wps-office-suite)
- [README](artifact/README.md)
- [Architecture](artifact/ARCHITECTURE.md)
- [Requirements](artifact/requirements.txt)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown, shell commands, JSON-like command results, and generated Office document files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create, edit, convert, overwrite, or export local Office files depending on the selected command and engine.]

## Skill Version(s):

4.8.0 (source: frontmatter and server release evidence, released 2026-08-22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
