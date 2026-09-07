## Description:

A professional product image generation skill purpose-built for Amazon product detail pages, including main images, secondary images, infographics, lifestyle shots, detail close-ups, and A+ Brand Content modules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, agencies, and e-commerce teams use this skill to plan and generate Amazon-ready product image sets and A+ Brand Content. It guides agents through scoped image planning, prompt drafting, consistency checks, and single-step dLazy CLI generation commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party CLI that may be installed globally or run through npx.

Mitigation: Prefer isolated npx execution or a sandbox and verify the @dlazy/cli package provenance before use.

Risk: Product prompts and media paths may be sent to dLazy API and file-hosting endpoints.

Mitigation: Avoid sending sensitive product media, private files, customer data, or unreleased product details unless the data handling terms are acceptable.

Risk: User-influenced product text can be incorporated into terminal commands.

Mitigation: Use safe argument handling and review command text before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-image-amazon-product-image-suite)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include current phase, image checklist, main-image consistency verdict, next confirmation request, and todo status.]

## Skill Version(s):

1.3.14 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
