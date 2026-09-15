## Description:

Route4Me lets an agent inspect schemas and manage Route4Me optimizations through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to list Route4Me optimizations and, with confirmation, create or delete optimization problems through an OOMOL-connected Route4Me account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a remote installer script for the oo CLI.

Mitigation: Review installer source and prefer a verified package manager or signed, versioned installer before running setup commands.

Risk: The skill can create or delete Route4Me optimization data.

Mitigation: Inspect the live action schema, confirm exact payloads and targets with the user, and require explicit approval before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-route4me)
- [Route4Me Homepage](https://route4me.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [OOMOL Route4Me Connection](https://console.oomol.com/app-connections?provider=route4me)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Actions should inspect live schemas before sending JSON payloads; write and destructive operations require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
