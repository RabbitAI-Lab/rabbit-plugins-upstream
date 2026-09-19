## Description:

SendFox (sendfox.com). Use this skill for ANY SendFox request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate SendFox through an OOMOL-connected account, including contact, list, membership, search, custom field, and unsubscribe workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that execute changing network content directly on the user's machine.

Mitigation: Review before installing, avoid curl|bash or irm|iex installer commands unless the source and contents have been independently verified, and prefer an official signed or checksum-verified oo CLI installation path.

Risk: Write and destructive SendFox actions can change contact, list, membership, or unsubscribe state.

Mitigation: Confirm the exact target, payload, and intended effect with the user before running write or destructive actions.

## Reference(s):

- [ClawHub SendFox skill page](https://clawhub.ai/oomol/skills/oo-sendfox)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [SendFox homepage](https://sendfox.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include SendFox connector command output summaries and setup guidance when authentication, connection, or billing errors occur.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
