## Description:

La Growth Machine lets an agent read, create, and update La Growth Machine data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Sales and growth operations teams use this skill to manage La Growth Machine audiences, leads, and members through authenticated connector actions. It supports read workflows directly and requires confirmation before write actions that change account data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts directly for the oo CLI.

Mitigation: Use a trusted package manager or a signed or checksum-verified oo CLI release instead of piping a remote installer directly into a shell.

Risk: Write actions can create or update La Growth Machine audiences and leads.

Mitigation: Confirm the exact action, payload, target account, and expected data changes with the user before running write actions.

## Reference(s):

- [La Growth Machine ClawHub listing](https://clawhub.ai/oomol/skills/oo-la-growth-machine)
- [La Growth Machine homepage](https://lagrowthmachine.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, JSON, Configuration guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
