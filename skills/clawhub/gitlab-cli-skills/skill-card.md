## Description:

Comprehensive GitLab CLI (glab) command reference and workflows for all GitLab operations. Use when working with merge requests, CI/CD pipelines, issues, releases, repositories, authentication, variables, labels, milestones, snippets, or any glab command. Covers 40+ sub-commands including glab mr, glab ci, glab issue, glab repo, glab release, glab variable, and more.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vince-winkintel](https://clawhub.ai/user/vince-winkintel)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release engineers use this skill as a reference for GitLab CLI commands and workflows across merge requests, CI/CD, issues, repositories, authentication, releases, and other GitLab operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Merge-request code may be run in an environment containing GitLab credentials or sensitive local files.

Mitigation: Run merge-request tests in a disposable environment without GitLab tokens or sensitive local files.

Risk: Tests passing could lead to changes being approved without an independent review.

Mitigation: Review changes independently before posting an approval.

Risk: Advertised automation scripts are missing, leaving their behavior unassessed.

Mitigation: Obtain and inspect the scripts before use; keep credentials narrowly scoped and separately review governance uploads, recurring jobs, and remote skill updates.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/vince-winkintel/skills/gitlab-cli-skills)
- [GitLab Model Context Protocol server documentation](https://docs.gitlab.com/user/model_context_protocol/mcp_server/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Code]

**Output Format:** [Markdown with shell command examples and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Command examples and operational guidance for GitLab CLI workflows.]

## Skill Version(s):

1.13.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
