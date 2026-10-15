## Description:

Guides agents to draft seven-part, story-driven short-video spoken scripts and includes a dLazy image-generation workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Short-video creators and content teams use this skill to draft conversational, seven-part spoken scripts from a persona, audience pain point, or topic. The skill also includes a separate workflow for generating images with dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A spoken-script request can be redirected into installing or running dLazy image generation.

Mitigation: Use the image workflow only if intentionally requested and confirmed; otherwise use a script-only version without CLI and image-generation instructions.

Risk: The dLazy CLI may store an API key locally and send prompts or referenced media to dLazy services.

Mitigation: Review the CLI and its data handling before installation; avoid supplying sensitive prompts or media and protect or rotate the API key.

## Reference(s):

- [dLazy CLI source (skill metadata link)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-text-spoken-script)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Image links]

**Output Format:** [Paragraph-form spoken script; optional image prompts, commands, and result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scripts follow a seven-step structure; image generation requires separate confirmation.]

## Skill Version(s):

1.3.30 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
