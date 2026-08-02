## Description: <br>
Helps agents manage self-hosted Jira issues with a Personal Access Token, including issue lookup, JQL search, transitions, comments, field updates, and issue creation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual Jira users use this skill to guide an agent through self-hosted Jira issue operations in SSO/SAML environments using a PAT. It is intended for single-task Jira work such as reading issues, searching with JQL, changing status, commenting, updating fields, and creating issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change real Jira data through PAT-authenticated commands, including transitions, comments, field updates, and issue creation. <br>
Mitigation: Use a least-privilege PAT, scope it to non-critical projects where possible, and require the agent to show the exact Jira write action for approval before execution. <br>
Risk: Jira PATs and callback URLs may expose sensitive access if broadly scoped, logged, or reused carelessly. <br>
Mitigation: Avoid broad callback URLs, keep tokens out of committed files and logs, rotate PATs regularly, and review command output before sharing it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jira-pat-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON examples, and structured Jira operation results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use JIRA_PAT and JIRA_URL environment variables to call Jira REST APIs; write actions should be shown for approval before execution.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
