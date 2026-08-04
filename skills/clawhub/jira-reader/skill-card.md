## Description: <br>
Read-only Jira lookup commands, including JSON task-directory output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[amaury95](https://clawhub.ai/user/amaury95) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operations teams use Jira Reader to let an agent perform read-only Jira Cloud lookups for issue details, JQL searches, project metadata, recent activity, assigned open work, and current-user task directories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A Jira read token gives the helper access to Jira data available to that token. <br>
Mitigation: Use a scoped Atlassian token with the minimum read permissions needed and avoid printing or committing tokens. <br>
Risk: Broad JQL searches can expose projects or issues the agent did not need for the current task. <br>
Mitigation: Keep JIRA_BASE_URL pointed at the intended Jira site and prefer project-scoped commands or JQL filters with conservative max result limits. <br>
Risk: The helper loads environment values from .env or JIRA_ENV_FILE, which may contain sensitive Jira credentials. <br>
Mitigation: Protect the environment file, set JIRA_ENV_FILE deliberately when using alternate credentials, and rely on existing process environment values when they should take precedence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/amaury95/skills/jira-reader) <br>
- [Publisher profile](https://clawhub.ai/user/amaury95) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON responses and concise Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Jira Cloud queries; my-tasks-directory groups assigned open issues by project and status and reports truncation when max results omit items.] <br>

## Skill Version(s): <br>
0.4.0 (source: release metadata, SKILL.md frontmatter, script constant) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
