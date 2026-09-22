## Description:

Turns a supplied URL or webpage link into a promo, social ad, or product demo video workflow through the dLazy hosted URL-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and marketing teams use this skill when they want an agent to turn a webpage URL into a promotional, advertising, or product-demo video workflow. The skill is a wrapper around the dLazy hosted service and requires dLazy CLI authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files can be sent to the dLazy hosted service.

Mitigation: Use the skill only with data approved for dLazy processing and review local policy before attaching files.

Risk: Authentication stores a dLazy API key in local CLI configuration.

Mitigation: Rely on OS-user file permissions, avoid sharing configuration files, and rotate or revoke keys when needed.

Risk: The workflow depends on a pinned npm CLI package and hosted endpoints.

Mitigation: Review the pinned @dlazy/cli package or source before installation in strict supply-chain environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown-style agent guidance with inline shell commands and hosted-service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference dLazy project ids, authentication state, uploaded files, and streamed service responses.]

## Skill Version(s):

1.0.15 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
