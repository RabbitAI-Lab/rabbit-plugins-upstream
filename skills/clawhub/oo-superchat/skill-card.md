## Description:

Superchat (superchat.com). Use this skill for ANY Superchat request - reading, creating, and updating data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Superchat through an OOMOL-connected account, including reading workspace, channel, and contact data; managing contacts; and sending email, SMS, or WhatsApp template messages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer commands for the oo CLI.

Mitigation: Review the installer path before use and prefer a verified, pinned, or manually inspected oo CLI installation method.

Risk: Write actions can create or update contacts and send outbound Superchat messages.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running write or message-send actions.

## Reference(s):

- [Superchat homepage](https://www.superchat.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-superchat)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before Superchat actions and reports connector responses as JSON when commands are run with --json.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
