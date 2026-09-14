## Description:

Generate images with the Kling o1 model from text prompts and optional reference images through the dLazy CLI and hosted API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate or edit images with Kling o1 using text prompts and up to ten image references.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, selected media, generated outputs, and API key setup involve dLazy infrastructure.

Mitigation: Install only if you trust dLazy and avoid sending sensitive local files or confidential prompt content.

Risk: The skill depends on the external @dlazy/cli npm package and a local dLazy API key configuration.

Mitigation: Prefer npx for non-persistent use, review the package before installation, and rotate or revoke API keys when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-image-o1)
- [ClawHub publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying CLI returns JSON containing generated image output URLs or asynchronous task status.]

## Skill Version(s):

1.3.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
