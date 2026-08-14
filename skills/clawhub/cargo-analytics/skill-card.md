## Description:

Download workflow run results, export segment data, and monitor run metrics using the Cargo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Cargo workspace run metrics, count failures, download run or batch outputs, and export segment data. It supports measurement and retrieval workflows, not root-cause diagnosis or billing analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authenticated Cargo CLI access can query and export workspace run and segment data.

Mitigation: Install and use the skill only in workspaces where the agent is allowed to access that data, and verify the active account with cargo-ai whoami before running commands.

Risk: The failed-record rerun workflow can create new batches, consume credits, and trigger workflow side effects.

Mitigation: Require explicit user approval before any cargo-ai orchestration batch create command.

Risk: Large exports or broad analytics queries can retrieve more data than intended.

Mitigation: Prefer scoped workflow UUIDs, batch UUIDs, status filters, date ranges, and limits before downloading or exporting results.

## Reference(s):

- [Cargo Analytics on ClawHub](https://clawhub.ai/cargo-ai/skills/cargo-analytics)
- [Cargo Skills repository](https://github.com/getcargohq/cargo-skills)
- [Run analytics examples](references/examples/run-analytics.md)
- [Data export examples](references/examples/exports.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce Cargo CLI commands for analytics queries, exports, downloads, and reruns of failed records.]

## Skill Version(s):

1.4.3 (source: frontmatter, skill-metadata.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
