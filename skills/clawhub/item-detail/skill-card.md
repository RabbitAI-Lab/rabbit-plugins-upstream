## Description:

Generates Chinese-language e-commerce product-detail image modules from a product photo and supplied selling points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce sellers and designers use this skill to turn a product photo and verified selling points into Chinese-language product-detail modules for a listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product photos, prompts, and generated outputs may be sent to the configured cloud provider.

Mitigation: Use dry-run to review requests and avoid confidential or unreleased images unless the provider's data handling is approved.

Risk: Provider credentials grant access to paid generation services.

Mitigation: Use scoped, revocable API keys and keep them out of prompts and shared files.

Risk: Generated Chinese text or product claims may be inaccurate or misleading.

Mitigation: Proofread every image and verify product features, specifications, and promotional claims before publication.

## Reference(s):

- [ClawHub item-detail listing](https://clawhub.ai/dlazyai/skills/item-detail)
- [Provider and CLI reference](references/provider-cli.md)
- [Model flags reference](references/model-flags.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Images]

**Output Format:** [Markdown guidance and CLI commands; generated product-detail images saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separate image modules may be assembled into a full product-detail page after review.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
