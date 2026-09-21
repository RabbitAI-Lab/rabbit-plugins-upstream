## Description:

Keygen lets agents read and manage Keygen account resources through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operations teams use this skill to inspect and manage licenses, policies, products, users, groups, machines, components, processes, entitlements, and license validation in a connected Keygen account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform high-impact write and destructive actions in a connected Keygen account.

Mitigation: Confirm the exact payload, target, and expected effect before write actions, and require explicit approval for destructive actions.

Risk: First-time setup includes optional pipe-to-shell install commands for the oo CLI.

Mitigation: Verify the OOMOL CLI installer and prefer the official install guide before running install commands.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-keygen)
- [Keygen Homepage](https://keygen.sh)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses with data and meta.executionId when actions are run.]

## Skill Version(s):

1.0.4 (source: evidence release.version and skill metadata.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
