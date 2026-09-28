## Description:

Turns user-provided copy or outlines into shot-by-shot short-video storyboards while preserving the original spoken text.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and production teams use this skill to plan short-form video shots from supplied copy, including scene direction, camera movement, and verbatim spoken lines. The release also offers optional dLazy cloud image generation through a CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A storyboard request may lead to installation and execution of a third-party CLI for cloud image generation, despite the text-focused description.

Mitigation: Review the CLI and confirm cloud generation is intended before installing or running generation commands.

Risk: dLazy authentication can store an API key locally, and prompts or referenced media may be sent to dLazy cloud endpoints.

Mitigation: Use only approved credentials and content; check local credential storage and cloud-sharing requirements before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI project (release metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown storyboard with shot descriptions and spoken script; optional CLI commands and image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes video aspect ratio, resolution, dimensions, camera directions, and user-provided dialogue preserved verbatim.]

## Skill Version(s):

1.2.18 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
