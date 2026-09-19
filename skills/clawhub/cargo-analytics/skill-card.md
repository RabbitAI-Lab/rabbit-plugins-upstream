## Description:

Helps agents measure Cargo workflow runs, download run and batch outputs, export segment or model data to CSV or JSON, and report success, error, and output counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and revenue teams use this skill to inspect Cargo run metrics, monitor workflow success and error counts, and retrieve generated outputs or segment exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The install metadata uses @cargo-ai/cli@latest, so the CLI version can change after review.

Mitigation: Pin the Cargo CLI to a reviewed release before deployment and update the pin only through normal change review.

Risk: The skill includes batch rerun commands that can change workspace state.

Mitigation: Require explicit user confirmation before reruns or other workspace-changing commands, and verify the target workflow, batch, and record IDs first.

Risk: Generated exports and signed URLs may contain sensitive workspace data.

Mitigation: Treat downloaded files and signed URLs as sensitive, restrict sharing, and store outputs only in approved locations.

Risk: Analytics commands require Cargo authentication and may expose broader workspace data than intended.

Mitigation: Use a read-only or least-privilege Cargo token for analytics and confirm the active workspace with cargo-ai whoami before running commands.

## Reference(s):

- [Cargo Analytics on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-analytics)
- [Cargo skills homepage](https://github.com/getcargohq/cargo-skills)
- [Response shapes](references/response-shapes.md)
- [Run analytics examples](references/examples/run-analytics.md)
- [Data export examples](references/examples/exports.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to produce or retrieve CSV and JSON exports through Cargo CLI commands.]

## Skill Version(s):

1.6.0 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
