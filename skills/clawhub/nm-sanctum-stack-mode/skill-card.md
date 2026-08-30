## Description:

Detects shared stack membership and iterates a command across all PRs in base-to-tip order.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill when a pull request command supports stack mode and must run its normal review or fix workflow across dependent PRs in base-to-tip order, then post one consolidated summary on the root PR.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands using this skill can run review or fix workflows across multiple related PRs and post a consolidated comment on the root PR.

Mitigation: Use it in repositories where that PR-commenting authority is acceptable, and review the consolidated summary before posting when the calling workflow allows.

Risk: Auto-detected stack membership may include the wrong PR set or only one PR.

Mitigation: Confirm detected stacks when stack mode was not explicitly requested, and fall back to single-PR mode when only one PR is found.

Risk: A failed mid-stack PR can leave downstream PRs with stale context.

Mitigation: Stop iteration at the failed PR and leave downstream PRs untouched until the failure is resolved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-stack-mode)
- [claude-night-market sanctum plugin](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [guidance, shell commands, markdown]

**Output Format:** [Markdown with inline bash code blocks and command workflow instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can guide commands to create progress-tracking todos, resolve stack membership, iterate per-PR workflows, and post or update a consolidated root PR summary.]

## Skill Version(s):

1.9.19 (source: server release metadata; artifact frontmatter shows 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
