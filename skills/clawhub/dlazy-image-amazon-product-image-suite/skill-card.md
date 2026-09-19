## Description:

A professional product image generation skill purpose-built for Amazon product detail pages, including main images, secondary images, product infographics, lifestyle shots, detail shots, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers, marketplace operators, and e-commerce creative teams use this skill to plan and generate Amazon-ready product image sets, including compliant main images, conversion-oriented secondary images, and A+ content modules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy CLI requires an API key, and a login or auth command can store that key in the local CLI configuration.

Mitigation: Verify that this storage model is acceptable, rotate or revoke keys from the dLazy dashboard when needed, or provide DLAZY_API_KEY per run instead of saving a key.

Risk: Product prompts and supplied media may be uploaded to dLazy hosted services for model processing and result hosting.

Mitigation: Avoid uploading private, unreleased, regulated, or otherwise sensitive product media unless that external processing is approved.

Risk: Release documentation has package-version and installation details that should be checked before installation.

Mitigation: Confirm that @dlazy/cli@1.2.3 is the intended package and prefer npx if a persistent global install is not desired.

Risk: Generated e-commerce images may include product claims, callouts, or visual elements that require marketplace and brand review.

Mitigation: Review every generated image for Amazon image policy compliance, claim accuracy, brand fit, and misleading accessories before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI source repository](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration instructions]

**Output Format:** [Markdown with task plans, image checklists, prompt drafts, image URLs, and inline bash command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key; prompts and referenced media may be sent to dLazy hosted services for generation.]

## Skill Version(s):

1.3.18 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
