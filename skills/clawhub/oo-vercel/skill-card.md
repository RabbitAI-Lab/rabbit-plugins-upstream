## Description:

Vercel (vercel.com). Use this skill for ANY Vercel request - reading, creating, updating, and deleting data. Whenever a task involves Vercel, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Vercel projects, deployments, domains, teams, environment variables, webhooks, runtime logs, and related account resources through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands for the OOMOL CLI.

Mitigation: Review the installation path and prefer official, signed, versioned, or package-manager-based installation before allowing any installer command to run.

Risk: Some supported Vercel actions can create, update, or delete resources.

Mitigation: Confirm the exact action, target, and JSON payload before approving write or destructive operations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-vercel)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Vercel homepage](https://vercel.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or request JSON payloads matching live OOMOL connector action schemas.]

## Skill Version(s):

1.0.4 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
