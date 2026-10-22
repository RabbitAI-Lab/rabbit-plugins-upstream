## Description:

Diagnoses Cargo workflow runs and batches by tracing execution, grouping failures, and attributing credit usage to workflows, nodes, and providers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to explain failed or incorrect Cargo runs, identify recurring batch errors, and find sources of workflow credit spend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the CLI from @latest may bring unreviewed changes.

Mitigation: Pin @cargo-ai/cli to a reviewed version before installation.

Risk: Diagnostics can expose workflow data and billing metrics through the Cargo account.

Mitigation: Use a trusted CLI and a least-privileged token; reserve admin access for billing attribution.

Risk: Re-running failed records can incur additional credits.

Mitigation: Pilot a small sample, estimate cost, and get approval before re-running the full batch.

## Reference(s):

- [Cargo Diagnostics on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-diagnostics)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Run trace](artifact/references/run-trace.md)
- [Batch error sweep](artifact/references/batch-error-sweep.md)
- [Play cost profile](artifact/references/play-optimize-credits.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Concise diagnosis with evidence summaries and optional CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include failure-group tables, exemplar run IDs, execution paths, and credit breakdowns.]

## Skill Version(s):

1.5.0 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
