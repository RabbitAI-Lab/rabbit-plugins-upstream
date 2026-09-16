## Description:

httpSMS (httpsms.com). Use this skill for ANY httpSMS request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate an OOMOL-connected httpSMS account from an agent, including account lookup, phone listing, billing reads, message retrieval, conversation listing, SMS/MMS sending, and message deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly.

Mitigation: Review the setup path before installation and prefer verified official documentation or a pinned, checksum-verified oo CLI release.

Risk: Message reads, sends, and deletes affect sensitive account data and communications.

Mitigation: Confirm recipients, message IDs, action type, and payload details before write or destructive actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-httpsms)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [httpSMS Homepage](https://httpsms.com/)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May execute live httpSMS connector actions through the oo CLI when the user has authenticated and connected the service.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
