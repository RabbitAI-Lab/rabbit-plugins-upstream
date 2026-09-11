## Description:

Authenticated messaging between OpenClaw instances over reachable HTTPS using built-in gateway webhook hooks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawreefantenna](https://clawhub.ai/user/clawreefantenna)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use Antenna to send authenticated cross-host messages between paired OpenClaw instances, manage peer registries, exchange bootstrap trust material, and check peer health without relying on visible chat channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Receiving remote messages requires a dedicated relay agent with sandbox disabled, broad session visibility, agent-to-agent access, and a bash exec allowlist.

Mitigation: Install only on hosts where that relay posture is acceptable, keep peer and session allowlists narrow, and review gateway changes before applying setup or upgrade plans.

Risk: Peer credentials, hook tokens, and relay secrets are sensitive local files.

Mitigation: Protect the skill secrets directory, keep secret files permission-restricted, use Antenna health checks, and prefer Ed25519 pairing over plaintext-legacy mode.

Risk: Dry-run output and ClawReef Public Groups can disclose message content or other sensitive plaintext.

Mitigation: Avoid sending credentials, private keys, regulated data, or sensitive operational details through public group routes or captured dry-run output.

Risk: Durable inbox auto-approval can allow trusted peers to deliver messages without per-message review.

Mitigation: Enable auto-approval only for peers that are fully trusted and keep inbound peer, outbound peer, and destination session allowlists constrained.

## Reference(s):

- [Antenna User Guide](references/USER-GUIDE.md)
- [Ed25519 Protocol v1](references/ED25519-PROTOCOL-V1.md)
- [OpenClaw 2026.8.1 Upgrade Guide](references/OPENCLAW-2026.8.1-UPGRADE.md)
- [Repository](https://github.com/ClawReefAntenna/antenna)
- [ClawHub Skill Page](https://clawhub.ai/clawreefantenna/skills/antenna)
- [ClawReef](https://clawreef.io)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, JSON configuration examples, and relay status text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Relay outputs are terse status strings such as delivered, queued, rejected, or error; setup and diagnostic flows may emit change previews and configuration guidance.]

## Skill Version(s):

1.6.5 (source: server release metadata, skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
