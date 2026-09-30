## Description:

Guides film, advertising, short-video, and educational storyboard creation through a plan-first, render-later workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan characters, script and approve storyboard panels, generate images, and prepare cinematic or narrative storyboard layouts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media may be sent to dLazy, and generated image URLs are hosted there.

Mitigation: Avoid sending sensitive briefs or media unless dLazy's cloud handling is acceptable.

Risk: Login stores an API key in local CLI configuration.

Mitigation: Protect the local configuration or use the DLAZY_API_KEY environment-variable option.

Risk: Installing the CLI globally runs third-party package code.

Mitigation: Review the npm package and linked CLI source before installing, or use the documented on-demand invocation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source (listed in skill metadata; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Image URLs]

**Output Format:** [Bulleted storyboard plans and scripts, image links, and print/PDF layout guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires confirmation at key stages before generating successive images.]

## Skill Version(s):

1.3.24 (source: ClawHub release metadata; embedded skill frontmatter: 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
