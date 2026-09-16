## Description:

Operate JumpServer through an OOMOL-connected account for searching and reading accounts, assets, nodes, asset permissions, terminal sessions, and users.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and IT administrators use this skill to inspect JumpServer resources through OOMOL's JumpServer connector. It supports read-only listing and search workflows for managed accounts, assets, nodes, permission rules, terminal sessions, and users.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Review the installer path before use and prefer a verified package or reviewed download for the oo CLI.

Risk: The connector can expose JumpServer data according to the scopes connected through OOMOL.

Mitigation: Connect only JumpServer scopes you are comfortable exposing through this connector and inspect the live action schema before each connector action.

## Reference(s):

- [JumpServer Homepage](https://www.jumpserver.org)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-jumpserver)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown guidance with bash and PowerShell command blocks; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
