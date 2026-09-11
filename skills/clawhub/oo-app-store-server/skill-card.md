## Description:

Guides agents to operate Apple's App Store Server API through an OOMOL-connected account using the oo CLI for reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect App Store Server connector schemas and run OOMOL account-backed actions for subscriptions, transactions, notifications, refunds, app transactions, and order lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can operate on sensitive App Store commerce data.

Mitigation: Use only a least-privilege OOMOL connection scoped to the required App Store Server API work.

Risk: Some actions can change subscriptions, transactions, consumption information, or app account tokens, including irreversible renewal extensions.

Mitigation: Require explicit user approval for each state-changing operation and confirm the exact payload and expected effect before execution.

Risk: The setup guidance includes remote installer pipe commands.

Mitigation: Prefer a verified package-manager installation or checksum-verified CLI install path before running the oo CLI.

## Reference(s):

- [App Store Server API documentation](https://developer.apple.com/documentation/appstoreserverapi)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agents should inspect live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
