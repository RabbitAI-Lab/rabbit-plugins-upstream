## Description:

WhatsAble (whatsable.app) helps agents read, create, and update WhatsAble data through the OOMOL oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users with an OOMOL-connected WhatsAble account use this skill to inspect live connector schemas and send WhatsApp text messages with optional attachment URLs. Write actions require confirming the recipient, message body, attachment URL, and intended effect before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send WhatsApp messages through a connected WhatsAble account.

Mitigation: Confirm the recipient, message body, attachment URL, and intended effect with the user before allowing any send_message run.

Risk: Authentication, connection setup, or billing recovery steps could be triggered unnecessarily.

Mitigation: Run setup steps only after an oo command fails with the matching authentication, connection, or billing error.

## Reference(s):

- [WhatsAble ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-whatsable)
- [WhatsAble Homepage](https://whatsable.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON from the oo connector run flow, including data and meta.executionId.]

## Skill Version(s):

1.0.0 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
