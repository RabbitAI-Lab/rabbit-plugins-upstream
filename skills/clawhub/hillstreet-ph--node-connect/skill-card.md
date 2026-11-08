## Description:

Diagnose OpenClaw Control UI browser and native Android, iOS, or macOS node connection failures across route, auth, pairing, QR/setup-code, and reconnect states.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw operators and developers use this skill to diagnose browser and native node connection failures against one selected Gateway. It guides route and authentication checks, exact-request pairing, and verification of a fresh connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Device-pairing approvals can change authorization state. ClawScan reports that `devices approve --latest` is not read-only despite being described as a preview.

Mitigation: Confirm the target Gateway, re-list pending requests immediately before approval, and approve only a verified exact request ID; do not rely on `--latest` as a preview.

Risk: The security scan was partial because a referenced local path was missing, so related material may not have been inspected.

Mitigation: Review the complete installed skill and any related local material before using its pairing guidance.

## Reference(s):

- [Node Connect on ClawHub](https://clawhub.ai/hillstreet-ph/skills/node-connect)
- [Publisher profile: hillstreet-ph](https://clawhub.ai/user/hillstreet-ph)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown troubleshooting guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
