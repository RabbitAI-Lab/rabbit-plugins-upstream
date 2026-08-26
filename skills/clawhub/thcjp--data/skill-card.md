## Description:

A data lifecycle skill for extraction, cleaning, analysis, reporting, and visualization with Chinese-language interaction support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to process datasets, generate summaries and reports, and create visualizations from structured or semi-structured data. It is not intended for real-time streaming data or decisions that require human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file access and shell command capability for data-processing workflows.

Mitigation: Install only in workspaces where broad file access and shell commands are acceptable, and review commands before execution.

Risk: The artifact makes encryption, redaction, access-control, and command-whitelist claims that are not backed by the release evidence.

Mitigation: Rely on the agent platform or workspace controls for those protections, especially when handling private, business, or regulated data.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON examples and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce data summaries, cleaned data descriptions, analysis reports, visualization guidance, execution logs, and configuration instructions.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter states 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
