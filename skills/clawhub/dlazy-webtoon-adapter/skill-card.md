## Description:

Adapts web novels into Chinese-language webtoon plot breakdowns, episode plans, and scripts, with optional image-generation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and creative teams use this skill to turn supplied web-novel chapters into plot breakdowns, tagged episodes, and visual-first scripts in Chinese. It also offers optional guidance for generating images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running a third-party CLI can execute commands on the user's machine.

Mitigation: Review the CLI and request explicit confirmation before installation or each terminal command.

Risk: Prompts and selected local media may be sent to dLazy's cloud services.

Mitigation: Avoid sensitive files and obtain explicit confirmation before any upload.

Risk: Authentication can store a dLazy API key in local CLI configuration.

Mitigation: Prefer a one-off environment variable when appropriate, protect stored credentials, and rotate or revoke keys if exposed.

## Reference(s):

- [dLazy CLI repository (tool referenced by this skill)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Chinese-language Markdown in conversation, with optional shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Plot breakdowns, episode tags, and per-episode scripts; optional image-generation instructions require user confirmation.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
