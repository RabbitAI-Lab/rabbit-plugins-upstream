## Description:

Provides Chinese-English and English-Chinese translation for text, documents, code comments, and email while preserving formatting and terminology where possible.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers use this skill to translate Chinese and English text, Markdown documents, code comments, and business writing. It is also intended for batch translation workflows that need consistent terminology and preserved formatting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags broad read, write, and exec permissions plus automation and messaging claims that do not fit a translation-only skill.

Mitigation: Install only when those permissions are acceptable, run in a sandbox, and prefer a version that removes exec access and unrelated workflow or messaging claims.

Risk: Translated content can expose sensitive text to the active agent or model provider.

Mitigation: Review inputs for secrets, personal data, and confidential material before translation, and avoid sending restricted content unless the deployment policy allows it.

Risk: Translation quality may vary for specialized terminology, code comments, or high-impact communications.

Mitigation: Have a qualified reviewer check important outputs and provide glossary or terminology guidance for domain-specific material.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/translate-en-zh)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Plain text or Markdown, with translated content preserving source structure when possible.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include translated files or configuration guidance when the agent uses file or shell access.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
