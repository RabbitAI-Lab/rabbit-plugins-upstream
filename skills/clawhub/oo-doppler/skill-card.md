## Description:

Doppler (doppler.com). Use this skill for ANY Doppler request: reading, creating, updating, and deleting data through the OOMOL-connected Doppler connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Doppler projects, environments, configs, secrets, service tokens, syncs, integrations, and change requests from an agent workflow. It supports read-only inspection as well as confirmed write and destructive operations against a connected Doppler account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can retrieve, export, create, update, or delete Doppler secrets and tokens.

Mitigation: Install only for trusted OOMOL-managed workflows and require explicit confirmation before secret, token, write, or destructive operations.

Risk: First-time setup includes one-line remote installer commands.

Mitigation: Avoid running remote installers unless the installer source has been verified.

## Reference(s):

- [Doppler homepage](https://www.doppler.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Doppler skill](https://clawhub.ai/oomol/skills/oo-doppler)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action schemas before execution and returns connector responses as JSON.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
