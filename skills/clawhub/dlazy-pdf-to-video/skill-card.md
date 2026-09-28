## Description:

Helps turn PDFs and other documents into narrated explainer, training, or presentation videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and teams use this skill to turn PDFs and other documents into narrated explainers, courseware, training videos, and report summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected documents and prompts are sent to dLazy for processing.

Mitigation: Attach only files approved for remote processing.

Risk: Using the skill runs a pinned third-party npm CLI.

Mitigation: Review the package before use and prefer on-demand npx execution if a global installation is unwanted.

Risk: Authentication saves a dLazy API key locally.

Mitigation: Protect the local configuration and rotate or revoke the key when necessary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-pdf-to-video)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Terminal text and Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based conversations support remotely generated video deliverables.]

## Skill Version(s):

1.0.20 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
