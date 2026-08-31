## Description:

Creates marketing and promotional videos from product, brand, or brief inputs for social advertising and ecommerce campaigns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, marketers, and ecommerce teams use this skill to request conversion-focused product videos from product specs, manuals, catalogs, listings, brands, or campaign briefs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, product materials, and attached files are sent to dLazy's hosted API and file storage.

Mitigation: Use only with content acceptable for dLazy processing; use per-run API keys or clear project sessions when reducing local or remote persistence matters.

Risk: The broad marketing title may imply general marketing video creation, while the reviewed behavior is primarily ecommerce and product-listing video generation.

Mitigation: Use the skill for product and ecommerce video workflows, and verify fit before applying it to broader brand or campaign video tasks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-marketing-video)
- [dLazy publisher profile](https://clawhub.ai/user/dlazyai)
- [dLazy service homepage](https://dlazy.com)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline bash commands and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce generated video assets or links through the dLazy service; attached local files can be uploaded to dLazy storage.]

## Skill Version(s):

1.0.7 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
