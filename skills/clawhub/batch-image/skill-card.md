## Description:

This skill helps agents run repeatable dLazy batch image generation for up to 100 product SKUs using a shared visual specification, per-SKU product descriptions, controlled concurrency, retries, SKU-based archiving, and summary reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams, creative operators, and developers use this skill to generate visually consistent product images across many SKUs from a CSV or JSON manifest. It is intended for batch product-image workflows such as seasonal catalog creation, campaign refreshes, and store-wide visual updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images, prompts, and generated assets are handled by dLazy's cloud service.

Mitigation: Review data-handling requirements before use and avoid submitting sensitive or restricted product assets unless approved.

Risk: Using dLazy login or auth set stores an API key locally.

Mitigation: Protect the local CLI config, prefer scoped organization keys, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Large SKU batches can consume credits quickly.

Mitigation: Run dry-run estimates and small sample batches before submitting a full product catalog.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/batch-image)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Files]

**Output Format:** [Markdown guidance with bash commands, CSV/JSON manifest examples, JSON CLI responses, saved image paths, and summary reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports dry-run cost checks, async task IDs, retry loops, SKU-based file naming, and per-batch report generation.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
