## Description:

Turns product photos, links, specs, manuals, catalogs, or marketplace listings into polished product demo, showcase, or ad videos for ecommerce and cross-border selling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and ecommerce teams use this skill to create product demo, showcase, and advertising videos from product media, product documents, or marketplace links. It is suited for shopping videos, TikTok Shop assets, Amazon listing promotion, and cross-border selling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on the third-party @dlazy/cli npm package and dLazy hosted service.

Mitigation: Use the pinned package version from the skill metadata, prefer npx for temporary use when a persistent global binary is not desired, and review the package and service before installing.

Risk: Prompts, selected attachments, and the dLazy API key are handled by the dLazy CLI and service.

Mitigation: Use a revocable API key, rotate or revoke it when needed, and upload only files intended for dLazy processing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI source metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands and streamed agent responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated product-video workflow outputs from the dLazy hosted service; local file attachments are uploaded through the dLazy CLI when used.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
