## Description:

Pushsafer (pushsafer.com). Use this skill for ANY Pushsafer request - reading, creating, and updating data. Whenever a task involves Pushsafer, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to list Pushsafer devices or groups and send Pushsafer notifications through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run internet-hosted oo CLI installer scripts.

Mitigation: Install only through a trusted OOMOL distribution path, inspect a versioned installer, and verify checksums or signatures when available.

Risk: The send_message action can deliver Pushsafer notifications to a device, group, or all devices.

Mitigation: Confirm the intended recipient, message payload, and effect with the user before sending.

## Reference(s):

- [Pushsafer homepage](https://www.pushsafer.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-pushsafer)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute Pushsafer connector actions through the oo CLI after checking the live action schema.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
