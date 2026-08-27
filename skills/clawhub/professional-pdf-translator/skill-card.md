## Description:

Automates long-form PDF translation by extracting pages, matching user-provided glossaries, guiding Chinese translation, maintaining a dynamic terminology list, and appending formatted results to DOCX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cecil727](https://clawhub.ai/user/cecil727)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, translators, researchers, and other document-heavy users can use this skill to translate long PDFs with consistent terminology and formatted DOCX output. It is suited to novels, academic papers, technical white papers, rules documents, standards, and other terminology-rich PDFs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow reads user-selected PDF and glossary files, which may contain confidential or sensitive document content.

Mitigation: Use the skill only with documents the agent is allowed to read, and keep inputs in controlled local paths.

Risk: The workflow writes to user-selected DOCX, temporary text, and dynamic glossary paths, so an unsafe path choice can modify existing important files.

Mitigation: Choose a dedicated output directory and avoid pointing DOCX or glossary paths at important existing files.

## Reference(s):

- [Professional PDF Translator ClawHub listing](https://clawhub.ai/cecil727/skills/professional-pdf-translator)
- [Referenced Tiangong WPS Word automation skill](https://clawhub.com/skill/tiangong-wps-word-automation-cn)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; helper scripts emit JSON status and write DOCX or glossary files during use.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads selected PDF and glossary files; writes the chosen DOCX, temporary text, and dynamic glossary files.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
