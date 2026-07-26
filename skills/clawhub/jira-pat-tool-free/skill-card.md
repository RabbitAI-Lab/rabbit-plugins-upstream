## Description: <br>
Jira PAT 管理基础版 helps an agent use a Jira personal access token to inspect, search, update, comment on, and create issues on self-hosted Jira instances. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, project managers, and individual Jira users can use this skill to query Jira issues, run JQL searches, inspect workflow transitions, and prepare issue updates in SSO/SAML environments that rely on a personal access token. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change Jira records through a personal access token, including status transitions, comments, field updates, and new issues. <br>
Mitigation: Use a least-privilege Jira PAT and review every proposed Jira mutation before allowing execution. <br>
Risk: Jira personal access tokens and callback URLs can expose sensitive access if stored or sent carelessly. <br>
Mitigation: Keep tokens out of plain config files and only use callback URLs whose destinations are trusted. <br>
Risk: The security scan found under-scoped trigger and privacy guidance for a tool that can access Jira work items. <br>
Mitigation: Use the skill only for explicitly requested Jira work and avoid sharing unnecessary issue content or credentials. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/jira-pat-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, shell commands, and structured JSON-like responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Jira REST API commands, environment variable setup, result summaries, status codes, and execution logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
