## Description:

Helps turn product photos, specifications, or listings into shopping and promotional videos using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Sellers and marketers use this skill to request product demo and advertising videos from product images, documentation, or ecommerce listings, including multilingual shopping videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to dLazy's hosted service.

Mitigation: Only submit files and information you are comfortable sharing with dLazy.

Risk: Logging in saves an API key on the local machine.

Mitigation: Protect the local CLI configuration and rotate or revoke the key if exposed.

Risk: A global CLI installation persists beyond a single invocation.

Mitigation: Use the pinned npx invocation if a global installation is not desired.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Text via the dLazy CLI; the hosted service generates product videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports follow-up turns within a project and optional file attachments.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
