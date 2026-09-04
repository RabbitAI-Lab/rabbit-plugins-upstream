## Description:

Creates a batch ecommerce image-generation workflow from a product CSV, using a fixed visual specification with per-SKU variables, concurrency, retries, resume support, budget guards, and contact-sheet reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators, designers, and developers use this skill to generate visually consistent product images across many SKUs from CSV manifests, product reference images, and shared visual specifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package includes a broader task registry beyond batch product-image generation, including unrelated image and video tasks such as watermark removal.

Mitigation: Review or restrict scripts/lib/tasks.json before deployment and invoke only the batch-image task set needed for the release.

Risk: Prompts and selected product images are uploaded to the configured cloud provider during generation.

Mitigation: Use approved provider accounts and avoid uploading confidential, sensitive, or unlicensed assets unless the provider terms and data handling are acceptable.

Risk: Large batch runs can consume credits quickly or continue producing low-quality outputs at scale.

Mitigation: Run dry-runs and small samples first, keep concurrency bounded, use budget limits, and review generated samples before full production batches.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [seedream-5.0 model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy CLI](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with bash and Node.js commands plus generated image files, JSON manifests, optional HTML contact sheets, and optional compliance reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Batch outputs can include per-SKU image files, retry state, a batch manifest, quality or platform-compliance notes, and a contact sheet for human review.]

## Skill Version(s):

1.0.5 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
