## Description:

Enigma enables agents to operate Enigma through an OOMOL-connected account for business search, entity lookup, aggregate counts, KYB verification, account metadata, list management, and background task tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to call Enigma through the OOMOL `oo` CLI while relying on the connected OOMOL account for credentials. It supports read workflows, list creation and deletion, suggestions, KYB verification, schema inspection, and asynchronous task status checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that may execute unverified code.

Mitigation: Prefer a verified, version-pinned oo CLI installation method and review installer contents before running shell or PowerShell installer commands.

Risk: The skill can propose create, update, delete, billing, or KYB-related Enigma actions.

Mitigation: Confirm the exact action, payload, target resource, and expected effect with the user before executing state-changing, destructive, billing, or KYB-related commands.

Risk: Action payloads can become stale or incorrect if they are constructed without current schema details.

Mitigation: Inspect the live connector schema before building payloads and match command data to the authoritative schema returned by the connector.

## Reference(s):

- [ClawHub Enigma skill page](https://clawhub.ai/oomol/skills/oo-enigma)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Enigma homepage](https://www.enigma.com)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, code]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should be reviewed before executing write, destructive, billing, or KYB-related Enigma actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
