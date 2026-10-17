## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan cinematic or narrative storyboards, approve character designs and scripts, and generate storyboard images in stages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media are sent to dLazy's cloud service.

Mitigation: Upload only content appropriate for a third-party service; avoid confidential prompts and sensitive media.

Risk: Using the cloud CLI requires an API key, and a global installation or CLI login can persist credentials locally.

Mitigation: Review the CLI package before installation; consider on-demand npx use or the DLAZY_API_KEY environment variable instead of persistent installation or saved credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands, Image URLs]

**Output Format:** [Bulleted storyboard plans, character specifications, panel scripts, generation commands, and links to generated images]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation at planning, character, script, and image-generation stages; specifies an A4 landscape storyboard layout for print or PDF export.]

## Skill Version(s):

1.3.32 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
