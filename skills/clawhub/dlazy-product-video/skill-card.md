## Description:

Turns product photos, documents, or listing links into promotional product videos through dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketing teams use this skill to turn product images, documents, or store listings into product demos and ecommerce advertising videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and options are sent to dLazy, and attached product files are uploaded to dLazy storage.

Mitigation: Share only product assets approved for the hosted service; avoid confidential files unless their use is authorized.

Risk: Logging in or saving an API key stores credentials locally.

Mitigation: Protect local credentials and rotate or revoke the key if it is exposed.

Risk: The skill runs a third-party CLI package to access the hosted service.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package and its listed source before installing or using it with sensitive assets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text responses with generated video links or project status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated videos are created through dLazy's hosted service; project conversations can continue across turns.]

## Skill Version(s):

1.0.26 (source: ClawHub release metadata; artifact frontmatter says 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
