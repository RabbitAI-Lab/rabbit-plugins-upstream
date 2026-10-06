## Description:

Enables session-targeted messaging between OpenClaw agents on different hosts over HTTPS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawreefantenna](https://clawhub.ai/user/clawreefantenna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw operators use Antenna to send messages to approved sessions on other hosts, manage peers, and prepare their installations for migration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unverified inbound content reaches an unsandboxed, shell-capable relay agent before authentication.

Mitigation: Install only if this exposure is acceptable; consider waiting for a deterministic inbound relay if stronger confinement is needed.

Risk: Broad peer or session access and leaked hook tokens can expose the gateway to unwanted messages.

Mitigation: Keep peer and session allowlists narrow, protect and rotate hook tokens, and prefer Ed25519 peers.

Risk: Sensitive messages in public groups may be readable outside the intended private peer exchange.

Mitigation: Avoid sending sensitive plaintext in public groups.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/clawreefantenna/skills/antenna)
- [Project repository (listed in skill metadata)](https://github.com/ClawReefAntenna/antenna)
- [User guide](artifact/references/USER-GUIDE.md)
- [Backup and readiness guide](artifact/references/BACKUP-AND-READINESS.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration guidance]

**Output Format:** [Plain-text messages and Markdown guidance with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Messages can be delivered to approved remote sessions.]

## Skill Version(s):

1.6.7 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
