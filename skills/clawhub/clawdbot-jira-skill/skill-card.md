## Description: <br>
Manage Jira issues, transitions, and worklogs via the Jira Cloud REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyjus25](https://clawhub.ai/user/kyjus25) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and Jira users use this skill to search issues, inspect issue details, create tasks, change status, assign work, comment, and summarize or log work through Jira Cloud. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a Jira API token for live Jira actions, including issue creation, status changes, assignment, comments, and worklog updates. <br>
Mitigation: Install only if the publisher is trusted, use a least-privileged Jira token or account, and review write commands before execution. <br>
Risk: Commands can operate across all Jira projects visible to the token when no project scope is configured. <br>
Mitigation: Set JIRA_BOARD when practical to limit searches and actions to intended Jira projects. <br>


## Reference(s): <br>
- [ClawHub Jira skill page](https://clawhub.ai/kyjus25/skills/clawdbot-jira-skill) <br>
- [Jira Cloud REST API documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/intro/) <br>
- [Atlassian API tokens](https://id.atlassian.com/manage-profile/security/api-tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Markdown command guidance plus JSON or plain text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl, jq, bc, python3, JIRA_URL, JIRA_EMAIL, and JIRA_API_TOKEN; JIRA_BOARD is optional for project scoping.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
