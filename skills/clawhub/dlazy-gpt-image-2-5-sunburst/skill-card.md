## Description:

Guides agents to generate and edit detailed images using the dLazy GPT Image 2.5 Sunburst service, including reference images, aspect ratios, and quality settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-image generation or image edits with reference images through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files submitted for image generation may leave the user's machine, and generated assets are hosted by dLazy.

Mitigation: Do not submit sensitive prompts or images unless dLazy's data handling is acceptable.

Risk: Logging in can persist a dLazy API key locally.

Mitigation: Use a per-invocation DLAZY_API_KEY or npx when less local persistence is preferred, and protect stored credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-sunburst)
- [dLazy CLI source (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return hosted image links or an asynchronous task ID; images may optionally be downloaded locally.]

## Skill Version(s):

1.2.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
