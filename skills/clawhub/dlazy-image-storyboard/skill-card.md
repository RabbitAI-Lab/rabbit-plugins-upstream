## Description:

A professional storyboard skill for film, advertising, short video, and educational narrative scenarios, built around a strict plan first, render later flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Filmmakers, advertisers, short-video teams, and educators can use the skill to turn a creative brief into a staged storyboard plan, structured panels, and image-generation prompts, then guide rendering through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy login or API-key setup and delegates rendering to an external CLI; the scan does not establish the CLI's downstream behavior.

Mitigation: Review the CLI and its data handling before use, send only prompts and media approved for dLazy, and use a key that can be rotated or revoked.

## Reference(s):

- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key setup](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions, Images]

**Output Format:** [Markdown storyboard plans, structured panel prompts, CLI instructions, and generated image links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses staged user confirmations before image generation; rendering is performed through the external dLazy CLI.]

## Skill Version(s):

1.3.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
