## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and DevOps engineers use this skill to find command guidance and workflows for managing GitLab projects, merge requests, issues, repositories, CI/CD, authentication, and related operations with glab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The merge-request review workflow may run contributor-controlled tests with the agent's permissions and credentials.

Mitigation: Review untrusted code in an approved disposable sandbox without host credentials.

Risk: Governance setup may add hooks and periodic sync, and installation or update options may skip prompts.

Mitigation: Review these changes and options before using them, and approve only the specific setup or update actions intended.

## Reference(s):

- [GitLab CLI configuration: environment variables](https://docs.gitlab.com/cli/configuration/#environment-variables)
- [GitLab Quick Actions documentation](https://docs.gitlab.com/user/project/quick_actions/)
- [GitLab Snippets API](https://docs.gitlab.com/api/snippets/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command examples and workflows covering GitLab CLI operations.]

## Skill Version(s):

1.13.40 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
