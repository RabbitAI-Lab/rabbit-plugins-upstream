## Description:

Guides film, advertising, short-video, and educational storyboard creation through a plan-first, render-later workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creative teams and agents use this skill to turn briefs into cinematic or narrative storyboard scripts, character references, and image-generation prompts, with approval gates before rendering and delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image generation depends on the third-party dLazy CLI and cloud service.

Mitigation: Review the @dlazy/cli package before installing and use npx if a persistent global installation is unwanted.

Risk: CLI login can store an API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-session access if a stored credential is unwanted.

Risk: Local media supplied for generation is uploaded to dLazy.

Mitigation: Only submit media files you intend to share with the provider.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source (tool reference; not verified skill provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Image-generation prompts, Shell commands, Image URLs, Storyboard layout guidance]

**Output Format:** [Bulleted Markdown with prompts, technical shot details, image links, and print/PDF layout specifications]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires explicit approval at the requirements, character, and script stages before image generation.]

## Skill Version(s):

1.3.34 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
