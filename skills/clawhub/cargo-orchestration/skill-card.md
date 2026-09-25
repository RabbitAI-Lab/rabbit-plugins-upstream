## Description:

Helps agents discover and run Cargo actions, workflows, and batches, build orchestration graphs, and inspect runtime results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and Cargo workspace operators use this skill to discover connector actions, run or schedule workflows, test and edit node graphs, and inspect execution history. It also guides users through sampling and approving large batches before full enrollment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Actions may run in the wrong workspace or with broader access than intended.

Mitigation: Confirm the active workspace with `cargo-ai whoami` and use least-privilege or test credentials before making changes.

Risk: A batch or empty filter may process every matching record and incur unexpected costs.

Mitigation: Sample 10–20 records, check the record count and credit estimate, and obtain explicit approval before full enrollment; avoid empty filters unless intentional.

Risk: Uploaded files and signed download URLs may expose sensitive workspace data.

Mitigation: Handle uploaded data and signed URLs as sensitive and limit their distribution.

Risk: Installing the CLI from a moving latest version may change its behavior.

Mitigation: Pin the `@cargo-ai/cli` version when possible.

## Reference(s):

- [Cargo Orchestration release on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo skills homepage (listed in release metadata)](https://github.com/getcargohq/cargo-skills)
- [Node selection guidance](references/node-selection.md)
- [Node graph reference](references/nodes.md)
- [Batch polling reference](references/polling.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Markdown]

**Output Format:** [Markdown with Cargo CLI commands and optional JSON or Mermaid snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include workflow or batch results returned by the Cargo CLI.]

## Skill Version(s):

1.13.0 (source: skill frontmatter and ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
