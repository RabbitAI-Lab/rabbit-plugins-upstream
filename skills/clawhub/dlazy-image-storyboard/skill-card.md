## Description:

Guides film, advertising, short-video, and educational storyboard creation through approved planning, character design, scripts, and image generation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams and content creators use this skill to plan cinematic or narrative storyboards, approve character references and panel scripts, and generate images one at a time for final assembly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storyboard prompts and referenced media are sent to dLazy cloud services.

Mitigation: Use only content approved for external processing and confirm each generation step.

Risk: An external npm CLI and dLazy API key are required; login can save the key locally.

Mitigation: Review the CLI before installation; use npx or DLAZY_API_KEY to avoid a long-lived global install or saved key.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Image URLs, Guidance]

**Output Format:** [Bulleted Markdown with storyboard prompts, generation commands, and image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [User approval gates before generation; panel specifications and A4 print/PDF assembly guidance.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
