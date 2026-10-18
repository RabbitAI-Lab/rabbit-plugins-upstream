## Description:

Uses a draft, editorial review, and revision workflow to produce polished translations with attention to terminology and regional language preferences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkxzhou](https://clawhub.ai/user/linkxzhou)

### License/Terms of Use:

MIT-0

## Use Case:

People translating or editing passages, articles, technical documents, and other longer text use this skill to improve accuracy, fluency, terminology, and regional phrasing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Long translations can leave drafts and final translations in .translate-work/ within the workspace, exposing sensitive text to anyone with workspace access.

Mitigation: Avoid highly sensitive long documents unless local draft storage is acceptable; remove .translate-work/ files when no longer needed.

## Reference(s):

- [ClawHub release: andrew-translate](https://clawhub.ai/linkxzhou/skills/andrew-translate)
- [Language and region reference](references/languages.md)
- [Translation prompt templates](references/prompts.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Translated text, preserving source formatting when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normally returns only the final translation; can provide drafting and review stages on request.]

## Skill Version(s):

1.3.0 (source: server-resolved release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
