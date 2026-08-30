## Description:

Permissions, address management, and delegation in Structs for granting or revoking permissions on objects or addresses, registering additional signing keys, managing multi-address accounts, and setting up minimum-permission delegate agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[abstrct](https://clawhub.ai/user/abstrct)

### License/Terms of Use:

MIT-0

## Use Case:

External Structs players and agent operators use this skill to inspect, grant, revoke, and verify permission bits, signing keys, address registration, and delegate-agent access. It is especially relevant when configuring mining bots, watcher agents, co-pilots, guild rank permissions, or account key rotation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Permission and address-management commands can permanently change who can act for a Structs player or object.

Mitigation: Use interactive transaction review, grant only minimum-necessary bits, avoid PermAll except for keys fully controlled by the user, and verify permissions after each change.

Risk: Registering an address with unverified proof material can attach authority to a key the user does not control.

Mitigation: Verify proof provenance before address registration and confirm the resulting address-player linkage with Structs query commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/abstrct/skills/structs-permissions)
- [Structs permissions mechanics](https://structs.ai/knowledge/mechanics/permissions)
- [Structs command conventions](https://structs.ai/skills/conventions)
- [Structs agent security](https://structs.ai/awareness/agent-security)
- [Structs authentication protocols](https://structs.ai/protocols/authentication)
- [Structs CLI install](https://structs.ai/skills/structsd-install/SKILL)
- [Structs guild permissions](https://structs.ai/skills/structs-guild/SKILL)
- [Structs streaming](https://structs.ai/skills/structs-streaming/SKILL)
- [Structs async operations](https://structs.ai/awareness/async-operations)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown guidance with inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires structsd on PATH and a signing key for transaction execution.]

## Skill Version(s):

1.25.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
