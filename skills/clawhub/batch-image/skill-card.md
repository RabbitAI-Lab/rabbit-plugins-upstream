## Description:

Creates consistent commercial product images for batches of SKUs from a CSV manifest, with parallel execution, retries, resume support, cost estimates, and review contact sheets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce operators and creative teams use this skill to generate a consistent set of product photographs from SKU image and description rows, then track and review the batch before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports weak cost limits.

Mitigation: Estimate the full batch cost before submission, set an independent budget ceiling, and monitor provider usage while jobs run.

Risk: The security assessment reports that dry-run behavior can overwrite a manifest.

Mitigation: Keep a separate copy of the manifest and try dry runs with a disposable copy before processing the production batch.

Risk: The security assessment reports an image-auditing capability that does not match the advertised image-generation purpose.

Mitigation: Review that capability and confirm it is expected for your workflow before use.

Risk: The security assessment has partial coverage: 7 of 13 components were scanned, with others only partly inspected.

Mitigation: Treat the result as incomplete and review the remaining components before installing or running the skill.

## Reference(s):

- [Provider CLI reference](references/provider-cli.md)
- [Seedream model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [Image review guidance](https://github.com/dlazy-ai/ecommerce-skills/blob/main/skills/detect-task/skill.md)

## Skill Output:

**Output Type(s):** [Images, Shell commands, CSV reports, Markdown guidance]

**Output Format:** [Product image files (JPG, PNG, or WebP), CSV progress reports, and Markdown with shell-command examples]

**Output Parameters:** [1D (one output set per SKU)]

**Other Properties Related to Output:** [Outputs are organized by SKU; the documented batch limit is 100 products, with sample review recommended before publishing.]

## Skill Version(s):

1.0.30 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
