## Description:

BaseLinker lets agents read, create, and update BaseLinker data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations users use this skill to inspect BaseLinker connector schemas and run inventory and order-management actions through an OOMOL-connected oo CLI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct remote script execution for installing the oo CLI.

Mitigation: Use an official signed or checksum-verified installer where available, inspect downloaded install scripts before execution, and run setup without elevated privileges.

Risk: Some BaseLinker actions can change state.

Mitigation: Inspect the live action schema first and confirm the exact payload and effect with the user before running actions marked as write or destructive.

## Reference(s):

- [ClawHub BaseLinker Skill](https://clawhub.ai/oomol/skills/oo-baselinker)
- [BaseLinker Homepage](https://baselinker.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL BaseLinker Connection](https://console.oomol.com/app-connections?provider=baselinker)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live connector schemas before running BaseLinker actions and to confirm state-changing payloads before execution.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
