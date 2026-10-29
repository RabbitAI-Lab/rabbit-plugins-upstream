## Description:

Helps create Amazon listing main images, secondary images, and A+ brand content with platform-focused visual guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Amazon sellers and ecommerce creative teams use the skill to plan and generate main and secondary listing images, product infographics, lifestyle and detail images, and A+ brand content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy hosted services for image generation.

Mitigation: Upload only product files that are approved for cloud processing.

Risk: The CLI stores an API key locally, and its implementation and claimed credential-file permissions were not fully audited.

Mitigation: Protect the saved key and rotate or revoke it if exposed.

Risk: The skill contains conflicting CLI version references (1.2.3 and 1.0.9).

Mitigation: Confirm the package version and review its release details before installation.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Images, Image-generation guidance, Markdown]

**Output Format:** [Generated product image assets with Markdown status and hosted image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The requested scope determines the image set: main and secondary listing images, A+ modules, or a full suite.]

## Skill Version(s):

1.3.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
