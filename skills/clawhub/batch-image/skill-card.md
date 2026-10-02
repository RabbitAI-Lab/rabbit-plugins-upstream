## Description:

Guides batch generation of visually consistent e-commerce product images from a SKU list, with retries, resume support, cost limits, and review outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to turn product-image manifests into coordinated product photography while tracking batch progress, costs, and images needing review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and referenced image URLs may be sent to a selected cloud image provider.

Mitigation: Use only approved product assets and choose an explicit provider after checking its data-handling terms.

Risk: Large batches can incur unexpected generation charges or create unwanted local files.

Mitigation: Use dry-run and a small sample first, set a cost limit, and choose a safe output directory.

Risk: Copying shell snippets with untrusted CSV rows can introduce unsafe command handling.

Mitigation: Prefer the included batch workflow over shell snippets for untrusted manifests.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [Image model options](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with command examples and CSV manifest guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution can save generated images, batch reports, and a contact sheet locally.]

## Skill Version(s):

1.0.16 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
