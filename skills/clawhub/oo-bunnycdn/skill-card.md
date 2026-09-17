## Description:

Guides an agent to operate BunnyCDN pull zones and cache purges through an OOMOL-connected oo CLI account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect BunnyCDN pull zones and purge pull-zone caches while relying on live action schemas and explicit confirmation for destructive operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include internet installer commands for the OOMOL CLI.

Mitigation: Use the setup path only after independently trusting and verifying the OOMOL CLI installer.

Risk: The skill has broad activation for BunnyCDN requests and includes a destructive cache purge action.

Mitigation: Use it only for intended BunnyCDN operations and confirm the exact cache purge target before execution.

## Reference(s):

- [BunnyCDN homepage](https://bunny.net/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-bunnycdn)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return JSON data from BunnyCDN connector actions when commands are executed.]

## Skill Version(s):

1.0.3 (source: evidence release version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
