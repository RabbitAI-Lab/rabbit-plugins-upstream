## Description:

Enables an agent to operate Telnyx through an OOMOL-connected account for messaging profile lookup, message retrieval, and confirmed SMS or MMS sending.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, support teams, and operations users can use this skill to inspect Telnyx messaging profiles, retrieve message details, and send SMS or MMS messages through a connected Telnyx account. Write actions require confirmation of the exact payload and effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts that could execute arbitrary code if followed without verification.

Mitigation: Install the oo CLI through a verified, pinned, or signed release process and review the setup path before installing.

Risk: The send_message action can send SMS or MMS through the connected Telnyx account.

Mitigation: Confirm the exact send_message payload and user-visible effect before executing the write action.

## Reference(s):

- [ClawHub Telnyx Skill](https://clawhub.ai/oomol/skills/oo-telnyx)
- [Telnyx Homepage](https://telnyx.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action results are returned as JSON by the oo CLI when commands are executed.]

## Skill Version(s):

1.0.3 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
