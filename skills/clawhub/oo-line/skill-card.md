## Description:

LINE lets agents operate LINE through an OOMOL-connected account, including reading bot and profile details and sending text messages through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect LINE connector schemas, read LINE Official Account and user profile data, and send approved text messages through an OOMOL-connected LINE account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broadcast, multicast, and push actions can send LINE messages to one or many recipients.

Mitigation: Review the exact message body, recipient set, and intended effect with the user before approving any write action.

Risk: The connector depends on trusted OOMOL access to the user's LINE connection.

Mitigation: Install and use the skill only when OOMOL is trusted with the relevant LINE connector access.

## Reference(s):

- [LINE homepage](https://line.me)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-line)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration guidance, API Calls, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before building action payloads.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
