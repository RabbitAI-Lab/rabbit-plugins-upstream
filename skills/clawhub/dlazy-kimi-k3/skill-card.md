## Description:

Moonshot AI thinking model with text, image, and video understanding for complex analysis, coding, and writing tasks that need long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and other external users can use this skill to route prompts and optional image or video inputs to dLazy's hosted Kimi K3 model for analysis, coding help, and writing support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy's hosted service for inference.

Mitigation: Avoid submitting sensitive data or local files unless cloud processing and upload are intended.

Risk: The skill depends on the dLazy npm CLI and a local dLazy API key.

Mitigation: Prefer on-demand npx execution when practical, keep the API key scoped and rotated, and install only when the dLazy CLI is trusted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI responses use JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompts plus optional image and video inputs through the dLazy CLI; asynchronous calls may return a generation ID.]

## Skill Version(s):

1.2.11 (source: release metadata; artifact frontmatter references dLazy CLI 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
