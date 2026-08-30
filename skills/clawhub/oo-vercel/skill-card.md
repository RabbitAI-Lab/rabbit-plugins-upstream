## Description:

Vercel (vercel.com). Use this skill for ANY Vercel request - reading, creating, updating, and deleting data. Whenever a task involves Vercel, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Vercel projects, deployments, domains, environment variables, webhooks, teams, and account context through an OOMOL-connected oo CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger state-changing Vercel operations for projects, domains, webhooks, and environment variables.

Mitigation: Confirm the exact action, target, and JSON payload with the user before running any action marked write.

Risk: The skill can delete environment variables or webhooks.

Mitigation: Require explicit approval for destructive actions and verify the target identifier before execution.

Risk: Vercel account access is mediated through an OOMOL-connected account.

Mitigation: Install only when OOMOL mediation is intended, and review connector payloads before approving account operations.

## Reference(s):

- [ClawHub Vercel skill page](https://clawhub.ai/oomol/skills/oo-vercel)
- [Vercel homepage](https://vercel.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
