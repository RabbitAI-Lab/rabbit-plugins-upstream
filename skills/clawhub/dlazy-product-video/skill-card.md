## Description:

Turns product photos, documents, or shopping listings into product demonstration and advertising videos with optional multilingual voiceover and a virtual host.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and ecommerce teams use this skill to make product showcases, demos, and shopping ads from product images, documents, or listing links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to dLazy's hosted service.

Mitigation: Only submit prompts and attach files you are comfortable sharing with dLazy.

Risk: Authentication saves a dLazy API key in local CLI configuration.

Mitigation: Protect the local key, rotate or revoke it if exposed, and use the per-invocation environment variable when local persistence is unwanted.

Risk: Installing the CLI globally keeps a local executable installed.

Mitigation: Use the pinned on-demand command `npx @dlazy/cli@1.2.3` if you prefer not to retain a global CLI.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI homepage (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Video]

**Output Format:** [Streaming text responses and generated product video]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include multilingual voiceover and an optional virtual host.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata; skill files declare 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
