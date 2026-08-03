## Description: <br>
Read-only Jira Cloud lookup commands for scoped API tokens. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amaury95](https://clawhub.ai/user/amaury95) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to let an agent perform read-only Jira Cloud lookups, including issue details, JQL searches, project metadata, recent activity, assigned open work, and current-user context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Jira query results may include private issue details visible to the configured token. <br>
Mitigation: Install with a Jira API token scoped only to the projects the agent should read. <br>
Risk: Secrets can be exposed if tokens are placed in queries, issue content, logs, or committed environment files. <br>
Mitigation: Keep tokens in environment configuration, avoid putting secrets in JQL or issue text, and review outputs before sharing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amaury95/skills/jira-reader) <br>
- [Publisher profile](https://clawhub.ai/user/amaury95) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, JSON, Guidance] <br>
**Output Format:** [Compact JSON summaries and Markdown command guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Jira Cloud requests; large text fields are trimmed and credentials are avoided in output.] <br>

## Skill Version(s): <br>
0.3.1 (source: server release evidence, skill frontmatter, package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
