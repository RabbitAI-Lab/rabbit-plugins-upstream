## Description:

Provides Git push troubleshooting and recovery guidance for GitHub, Gitee, and AtomGit, including credential failures, proxy or transport timeouts, direct push templates, and Git Data API fallback workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to diagnose failed Git pushes, avoid credential and proxy pitfalls, and choose direct Git or API-based recovery steps for publishing repositories to supported remotes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mutable or unpinned installation sources can change after review.

Mitigation: Review the exact artifact or install from a pinned release or commit before enabling the skill.

Risk: Global installation can broaden the skill's availability beyond the immediate task.

Mitigation: Install only in the required agent or project scope unless global use is explicitly needed.

Risk: Credential, proxy, remote visibility, or ref update steps can alter repository access or publishing state.

Mitigation: Require explicit per-action confirmation before modifying credentials, proxies, remotes, repository visibility, or push refs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/github-api-push-workaround)
- [LGD Hub homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Code]

**Output Format:** [Markdown with inline shell commands and workflow guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose credential, proxy, remote visibility, or ref update actions that require explicit user confirmation before execution.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
