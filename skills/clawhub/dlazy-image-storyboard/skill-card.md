## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan-first, render-later flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams, developers, and agents use this skill to turn film, advertising, short-video, educational, or comic-style briefs into gated storyboard plans, character references, panel prompts, and generated storyboard imagery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files may be sent to dLazy cloud endpoints for image generation.

Mitigation: Use the skill only when sending that content to dLazy is acceptable, and avoid sensitive media unless the deployment has approved that data flow.

Risk: Using the dLazy CLI requires an API key and may store credentials in local CLI configuration.

Mitigation: Prefer the DLAZY_API_KEY environment variable when persistent local configuration is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The workflow depends on installing or running the third-party npm CLI.

Mitigation: Review the CLI source or npm package before global installation, or use the pinned npx command for on-demand execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with storyboard planning bullets, prompt drafts, confirmation gates, generated image URLs, and inline shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The workflow uses user confirmation gates before image generation and runs one synchronous dLazy CLI generation command at a time.]

## Skill Version(s):

1.3.20 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
