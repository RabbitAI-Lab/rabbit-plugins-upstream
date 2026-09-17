## Description:

Textmagic helps an agent read, create, and update Textmagic account data through the OOMOL-connected oo CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Textmagic through an already connected OOMOL account, including reading contacts, lists, templates, and account details, creating contact lists, and sending SMS messages after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Install the oo CLI through a verified package, pinned release, checksum, or signature-checked download before running the skill.

Risk: Textmagic write actions can change account state, including creating contact lists and sending SMS messages.

Mitigation: Confirm the exact action, payload, recipients, and message body with the user before running any write action.

Risk: SMS sending can reach up to 1,000 phone numbers and may create cost, compliance, or messaging-abuse exposure.

Mitigation: Limit sends to the intended recipients, verify the message content, and check account billing or policy constraints before execution.

## Reference(s):

- [Textmagic homepage](https://www.textmagic.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-textmagic)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before action payloads; command responses are JSON objects containing data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
