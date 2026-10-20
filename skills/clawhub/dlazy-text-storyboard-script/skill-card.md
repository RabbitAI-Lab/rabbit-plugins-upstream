## Description:

Turns themes, outlines, or structured copy into detailed short-video storyboards with shot directions and spoken scripts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to turn supplied copy into shootable short-video shot lists while preserving the original spoken text.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Despite its text-only description, the skill also directs the agent to install and use a CLI for external image generation.

Mitigation: Review the skill and CLI before use; keep execution limited to the storyboard task unless the user explicitly approves image generation.

Risk: CLI use may require an account and API key and may send prompts or referenced media to dLazy services.

Mitigation: Obtain consent before sending content, avoid sensitive media, and manage the API key securely.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands]

**Output Format:** [Markdown storyboard with video parameters, numbered shots, shooting directions, and verbatim spoken script; optional CLI image-generation commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 9:16 and 720p when unspecified; spoken copy should remain unchanged.]

## Skill Version(s):

1.2.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
