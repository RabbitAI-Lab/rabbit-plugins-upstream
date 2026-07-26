## Description: <br>
GitLab API integration for repository operations, including reading, writing, creating, deleting files, listing projects, and managing branches. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[d1gl3](https://clawhub.ai/user/d1gl3) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to let an agent inspect and change GitLab repositories through the GitLab REST API, including file reads, writes, deletes, project listing, directory listing, and branch operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A GitLab personal access token can read or modify repositories according to its scopes. <br>
Mitigation: Use a dedicated least-privilege token, prefer read-only scopes unless writes are needed, and protect the token file with restrictive permissions. <br>
Risk: Write and delete operations can change repository files. <br>
Mitigation: Manually confirm the project, branch, path, content, and commit message before any write or delete operation. <br>
Risk: Self-hosted instance configuration can direct API calls to a non-default GitLab server. <br>
Mitigation: Configure only trusted GitLab instances and verify the instance URL before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/d1gl3/skills/gitlab-api) <br>
- [GitLab REST API documentation](https://docs.gitlab.com/ee/api/api_resources.html) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, API calls, configuration] <br>
**Output Format:** [Markdown guidance with bash and curl examples plus a shell helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a GitLab personal access token from GITLAB_TOKEN or ~/.config/gitlab/api_token and can emit JSON-derived command output through jq.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
