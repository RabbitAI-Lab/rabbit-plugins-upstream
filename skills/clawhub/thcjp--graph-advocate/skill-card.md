## Description:

图谱 routes blockchain data questions to relevant Graph Protocol services and returns routing guidance or live data responses for analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and automation users can use this skill to route blockchain data questions to Graph Protocol-related services, select subgraphs, optimize GraphQL queries, and support reporting or market analysis tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests read, write, and command execution tools without clear operational boundaries.

Mitigation: Install it with the minimum tool permissions needed for the task, and avoid granting write or shell execution access unless a reviewed workflow requires them.

Risk: The skill may use API credentials for external blockchain data services.

Mitigation: Use a limited-scope API key, provide it through environment variables, and rotate it if logs or workspace files might expose it.

Risk: The documented behavior and sample output are inconsistent, which can make downstream automation depend on unreliable fields.

Mitigation: Validate returned data shape and source freshness before using outputs in reports, trading workflows, or automated decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/graph-advocate)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with JSON examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require an API key and network access to retrieve external blockchain data.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata; artifact frontmatter declares 2.9.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
