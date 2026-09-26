## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict 'plan first, render later' flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative teams use this skill to turn creative briefs into cinematic or narrative storyboard workflows with requirements gates, character reference planning, script structure, image generation steps, and final storyboard layout guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media paths or files may be sent to dLazy cloud endpoints for generation.

Mitigation: Use this skill only with content approved for dLazy cloud processing and avoid submitting sensitive media unless that use is authorized.

Risk: API keys may be stored in the local dLazy CLI configuration.

Mitigation: Prefer environment-variable credentials for short-lived use or rotate and revoke stored API keys when local credential persistence is a concern.

Risk: Generated outputs are hosted on files.dlazy.com.

Mitigation: Review generated result URLs and sharing expectations before distributing storyboard outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands]

**Output Format:** [Markdown text with bulleted plans, image-generation prompts, synchronous CLI commands, and generated image URLs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user confirmation gates before image generation and sends prompts or selected media to dLazy cloud endpoints.]

## Skill Version(s):

1.3.21 (source: server release evidence; artifact frontmatter lists 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
