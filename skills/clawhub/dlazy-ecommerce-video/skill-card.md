## Description:

Ecommerce video, product video, shopping ad video, ecommerce video generator: turn a product, photos, or link into a conversion-focused ecommerce ad video for store, TikTok, or ad use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and developers use this skill to turn product photos, product specifications, manuals, catalogs, or marketplace listings into conversion-focused ecommerce videos. It supports shopping ad workflows such as Amazon listing videos, TikTok Shop videos, and cross-border selling content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached product files are sent to the dLazy hosted service.

Mitigation: Use the skill only with product data appropriate for dLazy processing and avoid attaching sensitive files that should not leave the local environment.

Risk: Login can persist a dLazy API key in the local CLI configuration.

Mitigation: Use npx or DLAZY_API_KEY for a less persistent setup, and rotate or revoke the key from dLazy when access should change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-ecommerce-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown with inline bash code blocks and hosted service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the dLazy CLI to stream agent responses and may produce hosted ecommerce video assets through the dLazy service.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
