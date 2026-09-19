## Description:

Product video, product demo video, product ad video, product showcase - turn a product's photos or link into a polished demo or ad video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce sellers, and marketing teams use this skill to create product demo, showcase, and ad videos from product images, documents, catalogs, or marketplace links through dLazy's hosted CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and attached files are sent to dLazy services.

Mitigation: Review product content before submission and avoid sending sensitive files unless dLazy's hosted processing is approved for the use case.

Risk: A saved dLazy API key can persist in the local CLI configuration.

Mitigation: Use DLAZY_API_KEY per invocation when persistence is not desired, and rotate or revoke saved keys from the dLazy dashboard when needed.

Risk: Installing a third-party CLI globally persists executable code on the system.

Mitigation: Review the @dlazy/cli package/source before installation and prefer the pinned npx command for nonpersistent use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI command examples and operational notes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; attached local files may be uploaded to dLazy media storage before use.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
