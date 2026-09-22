## Description:

Bilingual English-Chinese translation skill for direct text translation, batch file translation, terminology consistency, and Markdown-aware document translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jeffrey-zou](https://clawhub.ai/user/jeffrey-zou)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to translate English and Chinese text, code comments, business messages, technical documentation, and Markdown files while preserving readable structure where possible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper scripts write translated content to output files, which may overwrite or place files in unexpected locations if paths are chosen carelessly.

Mitigation: Review input and output paths before running file translation commands, and use a dedicated working directory for batch translation.

Risk: The server security guidance describes the translator as demo-level and warns not to expect exact terminology alignment or exact Markdown preservation.

Mitigation: Review translated output before relying on it for publication, legal, technical, or customer-facing use.

Risk: The skill processes user-provided documents and text, which may contain sensitive information.

Mitigation: Avoid translating sensitive documents unless the runtime and storage environment are trusted.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jeffrey-zou/skills/translate-en-zh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Shell commands, Guidance]

**Output Format:** [Plain text or Markdown, with optional translated text and Markdown files written by helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled scripts can write translated output files; review output paths before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
