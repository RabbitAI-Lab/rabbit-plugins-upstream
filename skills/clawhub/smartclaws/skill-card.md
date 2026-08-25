## Description:

SmartClaws guides OpenClaw agents through setup and operation for publishing, reading, and managing IoT telemetry and commands on-chain on SKALE.

This skill is ready for commercial/non-commercial use.

## Publisher:

[eduv09](https://clawhub.ai/user/eduv09)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to set up SmartClaws OpenClaw agents, configure wallet, network, and job state, record deployment facts, and operate IoT devices through SmartClaws plugin tools with confirmed authority.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact SmartClaws tools can register entities, grant roles, publish messages, disclose encrypted data, manage viewing keys, and create backups.

Mitigation: Keep write, disclose, register, role, key, and backup tools limited to trusted sessions, and review the SmartClaws tool allowlist after setup.

Risk: An agent may act outside intended authority if AGENTS.md, SMARTCLAWS.md, on-chain roles, or session permissions are incomplete or inconsistent.

Mitigation: Require owner-confirmed authority and goal settings before writes, resolve names and roles with SmartClaws plugin tools, and refuse operation until setup readiness checks pass.

Risk: Wallet files, private keys, config secrets, and backups may expose signing authority if handled directly.

Mitigation: Use plugin wallet/status tools for addresses and readiness, never read or print wallet secrets, and keep backups owner-managed and local.

Risk: Encrypted telemetry or commands can be unreadable or overexposed if viewing keys and reader ACLs are mismanaged.

Mitigation: Generate and register viewing keys after funding, grant encrypted-channel reader access only to required wallets, and verify disclosure access before relying on encrypted data.

## Reference(s):

- [SmartClaws ClawHub skill page](https://clawhub.ai/eduv09/skills/smartclaws)
- [SmartClaws homepage](https://github.com/skalenetwork/smartclaws)
- [SmartClaws setup guide](SETUP.md)
- [SmartClaws mechanics](MECHANICS.md)
- [SMARTCLAWS deployment facts template](templates/SMARTCLAWS.example.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON/YAML configuration examples, and workspace file templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces setup guidance and template content; does not itself return private keys or authoritative blockchain state.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
