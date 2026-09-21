## Description:

Produces a cost-gated set of product image options for listings, store pages, or ads by editing a real product photo once per style when available, or generating text-only prototype images when no product photo exists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ofoxai](https://clawhub.ai/user/ofoxai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent plan, price, and produce several product-image options for commerce content while preserving product identity when a real source photo is available. It is intended for multi-image product sets rather than one-off edits, video generation, or low-level image API work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends selected product photos and prompts to the Ofox image service and requires an OFOX_API_KEY.

Mitigation: Use it only with product imagery and prompts that are acceptable to send to Ofox, and configure the API key deliberately before running generation commands.

Risk: Paid image generation can spend money across multiple calls in a set.

Mitigation: Review the quoted total for the whole set before approving any paid run.

Risk: A missing core dependency may require an npx install command that writes outside the working directory.

Mitigation: Have the user review and run any install command themselves, confirming it targets only the intended dependency.

Risk: Using the generate route without a real product photo can create plausible but inconsistent product variants.

Mitigation: Prefer the edit route with a verified real product photo for real SKUs, and clearly label text-only generation as prototype imagery.

Risk: Generated sets may preserve product identity while still varying product scale or framing across images.

Mitigation: Inspect the set before delivery and plan post-processing if marketplace images need consistent scale or alignment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ofoxai/skills/product-image)
- [Publisher profile](https://clawhub.ai/user/ofoxai)
- [Product Image homepage from release metadata](https://github.com/ofoxai/skills/tree/main/skills/product-image)
- [Ofox API key management](https://app.ofox.ai)
- [Ofox model catalog](https://api.ofox.ai/v1/models)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, cost tables, and generated image file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OFOX_API_KEY, curl, jq, and the delegated ofox-image-core skill; the workflow quotes the total set cost before paid image generation.]

## Skill Version(s):

1.1.2 (source: server evidence, frontmatter, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
