## Description:

翻译 translates text and files between English and Chinese, with support for batch translation, terminology consistency, and preserving document or code-comment formatting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to translate English and Chinese text, documentation, code comments, Markdown files, and business messages while preserving formatting and terminology.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read/write access and command execution that exceed a normal translation workflow.

Mitigation: Review before installing, remove or tightly scope exec permission, and grant file access only to translation inputs and outputs.

Risk: Translated content may be processed by an LLM or external API.

Mitigation: Avoid submitting secrets or restricted content unless the deployment uses an approved model and data-handling path.

Risk: Unrelated automation and messaging language in the artifact may confuse expected behavior.

Mitigation: Treat translation as the intended function and remove unrelated automation or messaging claims before broad use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/translate-en-zh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files, Guidance]

**Output Format:** [Plain text or Markdown, with optional translated file output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May preserve source formatting and terminology across translated text or documents.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
