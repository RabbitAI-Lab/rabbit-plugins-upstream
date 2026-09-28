## Description:

Guides agents through generating consistent product images from a SKU list with controlled concurrency, retries, resumable jobs, cost limits, and review outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce teams and developers use this skill to generate visually consistent product photos across a CSV of SKUs and review the resulting images before publication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Product images and prompts are sent to the selected cloud provider.

Mitigation: Confirm the materials can be shared with that provider and choose it explicitly before running.

Risk: Large jobs and retries can incur unexpected generation costs.

Mitigation: Run a dry run, test a small sample, and set an explicit budget limit before the full batch.

Risk: Untrusted CSV entries or an unintended output location can affect local job outputs.

Mitigation: Use a trusted manifest and select a deliberate project output directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/batch-image)
- [Provider CLI reference](references/provider-cli.md)
- [Model flags](references/model-flags.md)
- [Platform image specifications](references/platform-specs.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [When executed, the workflow saves product images, a per-SKU report, and optionally a contact sheet for review.]

## Skill Version(s):

1.0.14 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
