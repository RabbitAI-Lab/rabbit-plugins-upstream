## Description: <br>
Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering agents use this skill to select and run GitLab CLI workflows for merge requests, issues, CI/CD, repositories, releases, authentication, variables, labels, milestones, snippets, and related GitLab operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: GitLab write operations and destructive commands can affect merge requests, issues, runners, tokens, packages, releases, or repository state. <br>
Mitigation: Require explicit confirmation before commands using --force, --yes, deletes, runner changes, token rotation, merges, approvals, or quick-action batches. <br>
Risk: A reused shell or shared glab configuration can cause actions to run as the wrong GitLab account or against the wrong host. <br>
Mitigation: Verify the active GitLab host and account immediately before writes, and use least-privilege bot or service tokens where possible. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills) <br>
- [GitLab REST API documentation](https://docs.gitlab.com/api/) <br>
- [GitLab GraphQL documentation](https://docs.gitlab.com/api/graphql/) <br>
- [GitLab Duo CLI documentation](https://docs.gitlab.com/user/gitlab_duo_cli/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and command reference text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the glab CLI for command execution outside the skill text.] <br>

## Skill Version(s): <br>
1.13.21 (source: ClawHub server evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
