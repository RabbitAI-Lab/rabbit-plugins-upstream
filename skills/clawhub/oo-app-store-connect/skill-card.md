## Description:

App Store Connect lets agents use the OOMOL app_store_connect connector and oo CLI to read, create, update, and delete App Store Connect data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and release operators use this skill to inspect App Store Connect action schemas and run account administration workflows for app metadata, TestFlight, review submissions, pricing, subscriptions, Game Center, webhooks, certificates, and provisioning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can perform broad App Store Connect account-changing operations.

Mitigation: Connect a least-privileged App Store Connect account and require explicit user confirmation before write, destructive, publish, send, release, reorder, or redeliver actions.

Risk: Some documented setup paths use pipe-to-shell installation commands.

Mitigation: Use a verified installer source and integrity check, or follow the install guide instead of executing remote installer output directly.

Risk: Incorrect payloads can affect live App Store Connect records.

Mitigation: Inspect the live action schema with oo connector schema before constructing each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-app-store-connect)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [App Store Connect](https://appstoreconnect.apple.com/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses return JSON with data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: skill metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
