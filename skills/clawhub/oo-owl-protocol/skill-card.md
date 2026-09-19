## Description:

Owl Protocol (owlprotocol.xyz). Use this skill for Owl Protocol requests to read, create, and update data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Owl Protocol action schemas, read project and token metadata, and patch token metadata through the OOMOL `oo` CLI after confirming write payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install `oo` only through a verified, versioned vendor method and review installer contents before execution.

Risk: `patch_project_token` changes Owl Protocol token metadata.

Mitigation: Fetch the live action schema and require explicit user confirmation of the exact payload and intended effect before running write actions.

Risk: Authentication, connection, or billing recovery steps can redirect the user into account setup flows.

Mitigation: Run setup or recovery steps only after a matching command failure and avoid proactively opening login or connection URLs.

## Reference(s):

- [Owl Protocol homepage](https://owlprotocol.xyz)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Owl Protocol skill](https://clawhub.ai/oomol/skills/oo-owl-protocol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
