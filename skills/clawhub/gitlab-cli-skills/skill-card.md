## Description: <br>
Comprehensive GitLab CLI (glab) command reference and workflows for GitLab operations across merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and related glab commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to choose and compose GitLab CLI commands for repository work, merge request review, issue triage, CI/CD debugging, releases, authentication, and GitLab administration. It is most useful for terminal-centered GitLab workflows where an agent should propose commands, scripts, or configuration steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitLab write operations can affect the wrong host, project, or visible account if authentication context is stale or ambiguous. <br>
Mitigation: Verify the target host and current GitLab account before write operations, and prefer scoped bot or service accounts for agent activity. <br>
Risk: Commands involving tokens, variables, runners, deletes, merges, and raw API calls can expose secrets or make high-impact changes. <br>
Mitigation: Use least-privilege credentials, avoid printing or saving tokens, and require explicit review before destructive or administrative commands. <br>


## Reference(s): <br>
- [GitLab REST API documentation](https://docs.gitlab.com/api/) <br>
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/) <br>
- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/) <br>
- [GitLab Duo CLI documentation](https://docs.gitlab.com/user/gitlab_duo_cli/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration instructions] <br>
**Output Format:** [Markdown with inline shell commands and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitLab CLI command examples, API request examples, workflow steps, and safety checks for GitLab write operations.] <br>

## Skill Version(s): <br>
1.13.19 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
