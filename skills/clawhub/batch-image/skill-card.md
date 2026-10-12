## Description:

Guides batch creation of visually consistent e-commerce product images from a SKU list, with retries, resumable runs, and review outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to turn a product CSV and reference images into a coordinated set of product photos, with per-SKU output and batch review guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Large paid image-generation batches can run without an enforced confirmation, budget cap, or 100-item limit.

Mitigation: Run --dry-run first, set a positive --max-credits and a small --limit, and review estimated spend before expanding the batch.

Risk: Product images and prompts sent to an external provider may expose confidential assets.

Mitigation: Use a dedicated workspace, inspect CSV and image paths, and send confidential assets only when external processing is intended.

## Reference(s):

- [Provider CLI and data flow](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [Marketplace image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides generation of per-SKU image files, status reports, and contact sheets for review.]

## Skill Version(s):

1.0.20 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
