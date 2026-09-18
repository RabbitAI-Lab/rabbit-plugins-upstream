## Description:

Operates SafetyCulture through an OOMOL-connected account, including reading inspections, listing or searching actions, inspecting live action schemas, and creating SafetyCulture actions with confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support teams use this skill to run SafetyCulture read, search, and action-creation workflows through the OOMOL `oo` CLI. It is intended for agents that need to inspect the connector schema before constructing requests and confirm state-changing payloads before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute scripts from the network.

Mitigation: Review the `oo` CLI installation path first and prefer official, versioned, verifiable installers or package-manager instructions before running curl-to-bash or PowerShell `iex` commands.

Risk: SafetyCulture write actions can change workspace state.

Mitigation: Inspect the live action schema, confirm the exact payload and intended effect with the user, and only then run state-changing actions.

## Reference(s):

- [ClawHub SafetyCulture Skill](https://clawhub.ai/oomol/skills/oo-safetyculture)
- [SafetyCulture Homepage](https://safetyculture.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands are executed through the OOMOL `oo` CLI; state-changing SafetyCulture actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: artifact frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
