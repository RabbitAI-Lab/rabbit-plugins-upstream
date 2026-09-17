## Description:

Operate Postmark through an OOMOL-connected account for reading, creating, and updating emails, templates, server details, bounces, and outbound message data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Postmark transactional email workflows through the OOMOL oo CLI, including message search, bounce review, template management, and email sending.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented setup flow includes one-line remote installers for the oo CLI.

Mitigation: Install or update the oo CLI only after independently trusting and verifying the source.

Risk: Postmark write actions can send emails, batch sends, or change templates.

Mitigation: Confirm the exact payload and user-visible effect before running any write action.

Risk: Inline JSON payloads in shell commands can be malformed or expose sensitive content in command history.

Mitigation: Prefer passing JSON payloads through a file for actual Postmark actions.

## Reference(s):

- [Postmark homepage](https://postmarkapp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub Postmark skill page](https://clawhub.ai/oomol/skills/oo-postmark)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Code, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
