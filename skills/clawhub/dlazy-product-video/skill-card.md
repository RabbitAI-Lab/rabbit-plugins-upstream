## Description:

Turns a product's photos, details, or listing link into a polished product demo, showcase, or ad video through the dLazy hosted product-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and commerce teams use this skill to create conversion-focused product videos from product images, product information, or marketplace links. It is intended for ecommerce demos, ads, and cross-border selling workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and files attached with --files may be sent to dLazy's hosted service.

Mitigation: Avoid attaching confidential product files unless dLazy's terms and organizational policy allow it.

Risk: The dLazy CLI can store a local API key.

Mitigation: Use OS user-restricted config storage and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-product-video)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown with inline bash code blocks and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The dLazy service may produce product-video assets outside the local skill context.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
