## Description:

MiniMax helps agents operate MiniMax through an OOMOL-connected account using the oo CLI for model, video, token-estimation, and text-to-audio workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run MiniMax model, video-generation, token-estimation, and audio-synthesis actions through an OOMOL-connected account while checking live connector schemas before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may ask the agent to execute remote oo CLI installer scripts directly.

Mitigation: Review the oo CLI installation method before installing and prefer an official, version-pinned installer with checksum or signature verification.

Risk: Write or destructive MiniMax actions can create, modify, or delete MiniMax resources.

Mitigation: Require explicit user confirmation of the exact payload, effect, and target before write or delete actions.

Risk: The skill depends on an OOMOL account connected to MiniMax and may fail when authentication, scopes, credentials, application readiness, or billing are not valid.

Mitigation: Use an OOMOL account intended for MiniMax access and resolve authentication, connection, scope, credential, application, or billing errors before retrying.

## Reference(s):

- [ClawHub MiniMax skill page](https://clawhub.ai/oomol/skills/oo-minimax)
- [MiniMax homepage](https://www.minimax.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Files]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector responses shaped as data plus meta.executionId; video downloads may be stored in connector transit storage.]

## Skill Version(s):

1.0.5 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
