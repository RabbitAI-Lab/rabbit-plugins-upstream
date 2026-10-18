## Description:

Helps agents use Cargo to execute actions and workflows, manage batch runs and node graphs, message AI agents, and inspect orchestration results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to run Cargo actions and workflows, test small batches before wider execution, visualize node graphs, and inspect run results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Cargo commands can change orchestration resources and trigger live connector actions.

Mitigation: Confirm the active workspace and review proposed changes before execution.

Risk: Large batch runs can affect many records and incur usage costs.

Mitigation: Sample a small batch first; require explicit approval before all-row or full-segment runs.

Risk: Uploaded records or webhook destinations can expose sensitive data.

Mitigation: Upload secrets or regulated data only with approval, and use trusted webhook URLs.

Risk: Installing the CLI from a floating latest version can change runtime behavior.

Mitigation: Pin or otherwise control the Cargo CLI version where appropriate.

## Reference(s):

- [Cargo Orchestration skill listing](https://clawhub.ai/cargo-ai/skills/cargo-orchestration)
- [Cargo skills project homepage](https://github.com/getcargohq/cargo-skills)
- [Node selection guide](references/node-selection.md)
- [Batch and async polling guide](references/polling.md)
- [Filter syntax guide](references/filter-syntax.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown]

**Output Format:** [Markdown with Cargo CLI commands and workflow examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include diagrams, JSON payloads, and summaries of run results.]

## Skill Version(s):

1.14.0 (source: skill frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
