## Description:

Generates Midjourney-style images through the dLazy CLI with aspect ratio, bot type, and grid or U1-U4 output controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and agents use this skill to request strongly stylized Midjourney-style image generation through dLazy, including aspect ratio, bot type, and output-selection controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on a third-party SaaS API and npm-distributed CLI, which creates ordinary service and supply-chain trust considerations.

Mitigation: Review the linked dLazy CLI source or npm package when supply-chain trust matters, and prefer npx or another isolated execution method over a persistent global install when practical.

Risk: Prompts and selected local media files may be sent to dLazy API and media-storage endpoints.

Mitigation: Only provide prompts and local files that are appropriate to send to dLazy, and review applicable service terms for the deployment context.

Risk: The dLazy API key is a credential stored in local CLI configuration or supplied through an environment variable.

Mitigation: Protect the API key like other credentials, use OS-level file permissions, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-mj-imagine)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [JSON result with generated image URLs or async task status, plus optional downloaded image files when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may send prompts and selected local media files to dLazy API and media-storage endpoints.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
