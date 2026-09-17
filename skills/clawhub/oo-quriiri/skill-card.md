## Description:

Quriiri helps an agent operate Quriiri SMS workflows through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send Quriiri SMS messages, check delivery reports, and list authorized sender IDs through their connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can involve remote installer commands for the oo CLI.

Mitigation: Use an official, version-pinned, checksum- or signature-verified oo CLI installation path before running installer commands.

Risk: The send_sms action changes state by sending SMS messages through the connected account.

Mitigation: Confirm the exact recipient, sender, message body, and expected effect with the user before allowing send_sms.

Risk: The skill depends on a valid OOMOL sign-in and Quriiri account connection.

Mitigation: Resolve authentication, scope, credential, or billing errors through the OOMOL account and connection pages before retrying actions.

## Reference(s):

- [Quriiri homepage](https://quriiri.fi/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Quriiri skill page](https://clawhub.ai/oomol/skills/oo-quriiri)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before action payloads; write actions require explicit user confirmation.]

## Skill Version(s):

1.0.2 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
