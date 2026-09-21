## Description:

Formats WeChat public account articles by converting Markdown into WeChat-compatible inline-styled HTML with themes, custom presets, and component blocks; its docs also describe article writing, image, search, and publishing workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agentforge-cyber](https://clawhub.ai/user/agentforge-cyber)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, operators, and agents use this skill to convert prepared Markdown articles into WeChat-ready HTML with selectable themes and reusable layout components. With explicit authorization, its broader workflow notes can also guide drafting, image, search, upload, and draft-publishing steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package presents a local formatter but also includes instructions for web search, AI image generation, WeChat uploads, account switching, and draft publishing.

Mitigation: Use the skill with explicit scope limits: run only the local Python formatter for Markdown-to-HTML conversion unless the user separately approves search, image, upload, account, or publishing actions.

Risk: Publishing-related workflow notes can involve WeChat app secrets or account configuration if those paths are enabled.

Mitigation: Do not provide WeChat app secrets for formatting-only use, and review any account configuration or publishing command before execution.

Risk: Generated HTML is optimized for WeChat constraints but may still render differently across editor, API, and client environments.

Mitigation: Preview the generated article.html and perform a WeChat draft or client rendering check before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/agentforge-cyber/skills/aws-wechat-article-formatting)
- [WeChat HTML constraints](artifact/references/wechat-html-constraints.md)
- [Formatting preset guide](artifact/references/presets/README.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with bash examples, YAML configuration, and generated WeChat-compatible HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The primary formatter writes article.html; broader workflow actions such as web search, AI image work, uploads, and draft publishing should be enabled only with explicit user approval.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
