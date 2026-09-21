## Description:

JustCall supports reading, creating, updating, and deleting JustCall contacts and users through the OOMOL-connected `justcall` connector and `oo` CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent inspect live JustCall action schemas and then list, retrieve, create, update, delete, or suppress JustCall contacts and users through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or invoke the OOMOL `oo` CLI as a connector layer for JustCall.

Mitigation: Install only if comfortable using OOMOL for JustCall access and verify the `oo` CLI installer source before running remote install commands.

Risk: Write and destructive actions can create, update, delete, or suppress JustCall contacts.

Mitigation: Require exact user confirmation of the target, payload, and expected effect before running write or destructive actions.

## Reference(s):

- [JustCall homepage](https://justcall.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline bash and PowerShell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are requested as JSON when commands run.]

## Skill Version(s):

1.0.1 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
