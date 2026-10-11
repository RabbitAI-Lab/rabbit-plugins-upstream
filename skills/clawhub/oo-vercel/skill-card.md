## Description:

Helps agents manage Vercel projects, deployments, domains, environment variables, webhooks, and logs through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage Vercel projects and deployments, including domains, environment variables, webhooks, and runtime logs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The recommended remote CLI installer cannot be verified from the skill alone.

Mitigation: Review the skill and install the oo CLI manually from a verified source only if you trust OOMOL and its distribution path.

Risk: Vercel write and destructive actions can change projects, deployments, or production traffic.

Mitigation: Require explicit confirmation of the target, payload, and effect before any write or destructive action.

## Reference(s):

- [Vercel skill release](https://clawhub.ai/oomol/skills/oo-vercel)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI installation guide](https://cli.oomol.com/install-guide.md)
- [Vercel](https://vercel.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with bash commands and Vercel action results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include JSON action results and deployment status.]

## Skill Version(s):

1.0.5 (source: skill frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
