## Description: <br>
Operate GitHub repositories, issues, pull requests, files, labels, and code search through GitHub REST API calls that use a GitHub Personal Access Token. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gaolfun](https://clawhub.ai/user/gaolfun) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and repository maintainers use this skill to inspect and operate GitHub projects from an agent workflow, including issue triage, pull request management, repository file changes, label management, and code search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Token-backed GitHub write access can merge pull requests, edit or delete files, and change issues. <br>
Mitigation: Use fine-grained, expiring tokens scoped to specific repositories; prefer read-only permissions unless write actions are required. <br>
Risk: Agent-proposed merge, delete, or direct file-update commands can modify repositories without clear confirmation safeguards. <br>
Mitigation: Require manual review before executing merge, delete, or direct file-update commands. <br>
Risk: Broad classic tokens can expose more private repository access than the workflow needs. <br>
Mitigation: Avoid broad classic repo scope and rotate or revoke tokens if exposure is suspected. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/gaolfun/skills/github-integration) <br>
- [GitHub API base URL](https://api.github.com) <br>
- [GitHub Personal Access Tokens](https://github.com/settings/tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command snippets and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses GitHub API responses and may propose write operations when the configured token permits them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
