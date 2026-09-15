## Description:

Use this skill for EspoCRM requests to read, create, update, and delete data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to work with EspoCRM records, metadata, and current-user data through an OOMOL-connected account. It supports read actions directly and requires explicit user confirmation before create, update, or delete operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path can run remote installer scripts directly in a shell.

Mitigation: Review the installer source before use, prefer a trusted version-pinned oo CLI installation with checksum or signature verification, and avoid running installer commands unless setup actually fails.

Risk: Create, update, and delete actions can change or remove EspoCRM data.

Mitigation: Confirm the exact action, target record, payload, and expected effect with the user before running write or destructive connector actions.

## Reference(s):

- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [EspoCRM homepage](https://www.espocrm.com/)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run successfully.]

## Skill Version(s):

1.0.3 (source: server release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
