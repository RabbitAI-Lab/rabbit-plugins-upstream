## Description:

A Chinese multifunction toolbox skill that helps agents run common calculation, text, developer, media, system, and AI-office utility workflows, including v4.0 tax calculation data and exchange-rate cache freshness handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent for everyday utility work such as calculations, text processing, file and media conversion, HTTP testing, system checks, QR and password utilities, meeting notes, and weekly report generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The toolbox can persist tool inputs and outputs locally, which may expose sensitive prompts, documents, passwords, URLs, or meeting content through history-enabled workflows.

Mitigation: Avoid entering secrets or confidential content unless history behavior has been reviewed, disabled, or cleared after use.

Risk: Some workflows can send user-provided content to third-party services, including QR generation, online transcription, HTTP testing, entertainment, knowledge lookup, wallpaper, and exchange-rate features.

Mitigation: Use offline or manual modes for sensitive content and review destination services before submitting private links, documents, audio, or credentials.

Risk: File and media workflows may read or write local files and may install optional packages such as Pillow, PyPDF2, rembg, jieba, qrcode, FFmpeg, or Whisper after confirmation.

Mitigation: Install optional dependencies only from trusted sources and run file-changing workflows on reviewed copies or in a controlled workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/dgngjx-skill)
- [tax_2026.yaml](references/tax_2026.yaml)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files, guidance]

**Output Format:** [Markdown, plain text, JSON-like structured output, shell commands, and generated local files depending on the selected tool.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Some workflows may read or write local working files, persist local history, call external services, or require optional package installation after user confirmation.]

## Skill Version(s):

4.0.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
