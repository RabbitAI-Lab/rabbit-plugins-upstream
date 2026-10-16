## Description:

Uses a hosted Kimi K3 model for complex analysis, coding, and writing with text, image, and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask the agent to analyze complex questions, draft writing, and generate code using text prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The third-party CLI stores a dLazy API key locally.

Mitigation: Review the CLI before installation, protect local credentials, and rotate or revoke the key in the provider dashboard if needed.

Risk: Prompts and explicitly referenced media files are sent to dLazy's hosted service.

Mitigation: Avoid submitting sensitive prompts or media unless the service's handling of that data is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Text or Markdown; CLI responses use a JSON envelope]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts up to 10 images and 8 videos; asynchronous requests can return a task ID.]

## Skill Version(s):

1.2.25 (source: server-resolved ClawHub release; bundled CLI pinned to 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
