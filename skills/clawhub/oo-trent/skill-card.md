## Description:

Trent lets agents send chat requests to Trent through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to interact with Trent from an agent session, inspect the live connector schema, and run supported Trent actions through OOMOL with server-side credential handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup recommends running remote installer scripts directly in a shell.

Mitigation: Use a pinned, signed, or checksum-verified oo CLI installation path, and run remote installer commands only after independently trusting the source.

Risk: The send_chat action is tagged as write-capable.

Mitigation: Confirm the exact payload and expected effect with the user before sending the Trent chat request.

## Reference(s):

- [ClawHub Trent skill page](https://clawhub.ai/oomol/skills/oo-trent)
- [Trent homepage](https://trent.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: server release metadata and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
