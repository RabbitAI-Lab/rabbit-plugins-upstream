## Description:

Guides an agent to generate transition videos from first and last frame images using Jimeng through the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to guide an agent in producing a coherent video transition between two supplied images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media may be uploaded to the third-party cloud service.

Mitigation: Only provide prompts and files intended for upload.

Risk: Authentication saves an API key to local CLI configuration.

Mitigation: Protect the local key or provide it per invocation; rotate it if exposed.

Risk: Installing the third-party CLI introduces package supply-chain exposure.

Mitigation: Review the CLI package before installing; use the documented npx invocation to avoid a persistent global installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-i2v-first-tail)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and service result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The service may return a generated media URL or an asynchronous task identifier.]

## Skill Version(s):

1.3.26 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
