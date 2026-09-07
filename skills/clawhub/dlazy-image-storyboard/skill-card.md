## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, educators, and agent-assisted production teams use this skill to turn creative briefs into structured cinematic or narrative storyboard plans, character references, prompt drafts, and generated storyboard image deliveries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and referenced media are sent to the dLazy cloud service for generation.

Mitigation: Do not provide private media files, sensitive prompts, or confidential production material unless upload to dLazy is intended and approved.

Risk: Using the global npm install path can leave a persistent CLI on the system.

Mitigation: Prefer the pinned npx invocation or a sandboxed install when persistent global tooling is not desired.

Risk: API keys may be stored in the local dLazy CLI configuration.

Mitigation: Use DLAZY_API_KEY for less persistent credential use, and rotate or revoke keys from the dLazy organization dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with structured bullets and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce image generation commands and hosted image URLs through the dLazy CLI.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
