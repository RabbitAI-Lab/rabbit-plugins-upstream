## Description:

Cargo Analytics helps agents retrieve Cargo workflow run outputs, export segments or models to CSV or JSON, and report run or batch success and error counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and Cargo workspace users use this skill to monitor workflow runs, calculate error rates, download run or batch outputs, and export segment data while leaving diagnostics and billing questions to companion skills.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can export broad Cargo workspace data, including segment data and run outputs.

Mitigation: Confirm the active workspace, workflow or model UUID, filters, row limits, and intended recipient before generating or sharing exports.

Risk: Some commands return signed download URLs for CSV or JSON results.

Mitigation: Require explicit approval before sharing signed URLs, and treat downloaded files as workspace data subject to the user's access controls.

Risk: The failed-record rerun workflow can create new processing batches.

Mitigation: Require explicit approval before reruns and verify the selected record IDs, workflow UUID, and scope.

## Reference(s):

- [Cargo Analytics ClawHub listing](https://clawhub.ai/cargo-ai/skills/cargo-analytics)
- [Cargo Skills homepage](https://github.com/getcargohq/cargo-skills)
- [Data export examples](references/examples/exports.md)
- [Run analytics examples](references/examples/run-analytics.md)
- [Response shapes](references/response-shapes.md)
- [Troubleshooting](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct the agent to produce or handle CSV, JSON, gzipped CSV, signed download URLs, and scoped analytics queries.]

## Skill Version(s):

1.5.0 (source: frontmatter, skill-metadata.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
