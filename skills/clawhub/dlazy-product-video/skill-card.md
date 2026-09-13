## Description:

Turns product photos, product links, specifications, manuals, or catalog content into product demo, showcase, or advertising video requests through the pinned dLazy product-to-ecommerce-video workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, marketers, and ecommerce teams use this skill to ask a hosted dLazy agent to create product demo, showcase, and advertising videos from product images, links, specifications, manuals, or catalogs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running the pinned npm CLI introduces ordinary package-install risk.

Mitigation: Review the dLazy CLI source or npm package before installation when high assurance is required, and avoid running npm or the CLI with administrator privileges.

Risk: Prompts and attached files are sent to dLazy services and local files may be uploaded to dLazy media storage.

Mitigation: Only attach files intended for upload to dLazy, and avoid submitting sensitive product or customer data unless the service terms and organization policy allow it.

Risk: The dLazy API key is stored locally or supplied through an environment variable.

Mitigation: Protect the local CLI configuration, use OS-user file permissions, and rotate the dLazy API key if compromise is suspected.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash code blocks and streamed CLI text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI package and may reference hosted product-video generation projects.]

## Skill Version(s):

1.0.12 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
