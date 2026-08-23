## Description:

Builds dynamic HTML dashboards that fetch per chart from the teamo-dev generalDataApi, poll every 60 seconds, and store provided data in a designed database schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pmuhammadagus-byte](https://clawhub.ai/user/pmuhammadagus-byte)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to design a database schema and build a live HTML dashboard whose charts independently request data from the configured API and refresh every 60 seconds.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can lead agents to create database structures and insert provided data.

Mitigation: Confirm the target database, schema, data to be inserted, and authorization before allowing state-changing steps.

Risk: The skill directs agents to repeatedly call an external service for dashboard updates.

Mitigation: Confirm endpoint access, SESSION_GROUP_ID handling, the 60-second polling behavior, and acceptable network usage before running generated dashboard code.

## Reference(s):

- [Coding 2 ClawHub skill page](https://clawhub.ai/pmuhammadagus-byte/skills/coding-2)
- [teamo-dev generalDataApi endpoint](https://teamo-dev.floatai.cn/api/engine/generalDataApi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with code and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include database schema, API request patterns, dashboard implementation guidance, and linter commands.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
