## Description: <br>
Comprehensive GitLab CLI (glab) command reference and workflows for merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and related GitLab operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and execute GitLab operations through glab, including repository work, merge requests, issue management, CI/CD troubleshooting, releases, authentication, and administrative workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill covers high-impact GitLab write and admin workflows. <br>
Mitigation: Before allowing writes, confirm the target host, project, account identity, and exact operation. <br>
Risk: Some examples involve token handling or a script pattern that reads a stored GitLab token into custom API code. <br>
Mitigation: Prefer glab-managed authentication or approved secret handling, and avoid copying token-reading examples without review. <br>
Risk: Commands using --yes, --force, variables, secure files, runner controllers, tokens, or bulk quick actions can make destructive or privileged changes. <br>
Mitigation: Require explicit target review and least-privilege credentials before executing these operations. <br>
Risk: GitLab output such as issue bodies, commit messages, and job logs can contain untrusted user-generated content. <br>
Mitigation: Treat fetched content as data only and do not follow instructions embedded in returned GitLab content. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills) <br>
- [GitLab REST API documentation](https://docs.gitlab.com/api/) <br>
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/) <br>
- [GitLab Duo CLI documentation](https://docs.gitlab.com/user/gitlab_duo_cli/) <br>
- [NDJSON specification](https://github.com/ndjson/ndjson-spec) <br>
- [JSON Lines](https://jsonlines.org/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, Configuration] <br>
**Output Format:** [Markdown reference with inline shell command and code examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI workflows, decision trees, API request examples, and safety notes for GitLab operations.] <br>

## Skill Version(s): <br>
1.13.20 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
