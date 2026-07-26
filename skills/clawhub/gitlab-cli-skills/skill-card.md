## Description: <br>
Provides GitLab CLI (glab) command reference and workflows for GitLab merge requests, CI/CD, issues, releases, repositories, authentication, variables, labels, milestones, snippets, and related GitLab operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to plan and run GitLab CLI workflows for repository work, merge requests, issues, CI/CD, releases, authentication, variables, and other GitLab operations. It helps an agent produce command-oriented guidance and pre-flight checks before GitLab actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitLab write operations could run against the wrong host or visible account. <br>
Mitigation: Confirm the GitLab host and visible account before any write, and use separate least-privilege bot or service-account tokens for different actors. <br>
Risk: Destructive GitLab commands can modify or delete project resources. <br>
Mitigation: Review commands that use delete, --yes, --force, or API write methods before execution, and confirm the intended project or group scope. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills) <br>
- [GitLab REST API Documentation](https://docs.gitlab.com/api/) <br>
- [GitLab GraphQL Documentation](https://docs.gitlab.com/api/graphql/) <br>
- [GitLab Duo CLI Documentation](https://docs.gitlab.com/user/gitlab_duo_cli/) <br>
- [NDJSON Specification](https://github.com/ndjson/ndjson-spec) <br>
- [JSON Lines](https://jsonlines.org/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GitLab host, account, token, and destructive-action review guidance before write operations.] <br>

## Skill Version(s): <br>
1.13.18 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
