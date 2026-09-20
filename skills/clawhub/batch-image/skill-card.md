## Description:

Creates a batch product-image generation pipeline from a SKU CSV, keeping shared visual specifications stable while varying product details, with concurrency, retries, resume support, budget guardrails, and review outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, ecommerce operators, and catalog teams use this skill to turn product manifests into consistent commercial product images while tracking retries, budget, and review artifacts. It is suited for batch SKU workflows where visual consistency and product fidelity need to be checked before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manifest-driven shell examples may execute unsafe content if the manifest is untrusted.

Mitigation: Use trusted manifests, prefer the bundled Node batch script, run `--dry-run`, and review generated commands before full execution.

Risk: Prompts and product images can be sent to the selected cloud provider.

Mitigation: Set an explicit provider, use appropriate credentials, and avoid passing sensitive local files or internal URLs as image inputs.

Risk: Batch generation can spend credits quickly or create unusable outputs at scale.

Mitigation: Run a single SKU first, sample several SKUs, use cost estimation and `--max-credits`, then review the batch manifest and contact sheet before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/batch-image)
- [Model flags](artifact/references/model-flags.md)
- [Platform image specifications](artifact/references/platform-specs.md)
- [Provider CLI reference](artifact/references/provider-cli.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Files, Markdown]

**Output Format:** [Markdown guidance with inline shell commands; bundled scripts can produce image files, JSON manifests, and HTML contact sheets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run planning, provider selection, retry controls, output directories, budget limits, and optional platform checks.]

## Skill Version(s):

1.0.11 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
