## Description:

Turns a supplied webpage URL into a promotional, social ad, or product demo video through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and marketers use this skill to turn website or landing-page URLs into promotional videos, social ads, and product demos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to the dLazy hosted service; attached files are uploaded when used.

Mitigation: Only submit URLs, prompts, and optional files you are comfortable sharing with dLazy.

Risk: An API key may be saved locally, and a global npm installation persists the CLI.

Mitigation: Protect the local key or provide it per invocation; use the pinned npx option to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text with project updates and video-generation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is handled through a project-based dLazy service session.]

## Skill Version(s):

1.0.19 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
