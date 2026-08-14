## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creative teams, and agent operators use this skill to turn creative briefs into planned cinematic or narrative storyboards with gated requirements, character design, script approval, image generation, and final assembly steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party dLazy CLI and hosted service that receive prompts and selected local media.

Mitigation: Install and use the skill only when the user trusts dLazy and is comfortable sending the relevant creative inputs and media to that service.

Risk: The dLazy API key can be persisted in a local CLI configuration file.

Mitigation: Use DLAZY_API_KEY for temporary sessions when persistent local storage is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source and homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with storyboard plans, prompts, confirmation gates, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated image URLs through the dLazy CLI and can include final storyboard assembly guidance.]

## Skill Version(s):

1.3.8 (source: server release metadata; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
