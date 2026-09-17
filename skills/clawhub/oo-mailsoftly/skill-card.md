## Description:

This skill helps agents read, create, update, and organize Mailsoftly contacts and contact lists through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage Mailsoftly contact records and contact lists from an agent, including searches, reads, list membership changes, and write operations after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on OOMOL as an intermediary for Mailsoftly account access.

Mitigation: Install and use it only when the user accepts that dependency and has connected Mailsoftly through OOMOL.

Risk: Write actions can change Mailsoftly contacts or contact list membership.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write or destructive.

Risk: The first-time setup path includes a pipe-to-shell installer command.

Mitigation: Prefer a verified official oo CLI installation method and avoid running installer commands blindly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mailsoftly)
- [Mailsoftly homepage](https://mailsoftly.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo connector commands and JSON request payloads; connector results are returned by the oo CLI as JSON.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
