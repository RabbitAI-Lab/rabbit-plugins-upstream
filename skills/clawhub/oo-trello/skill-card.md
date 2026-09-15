## Description:

Trello connector skill for reading, creating, updating, and deleting Trello data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Trello boards, lists, cards, members, labels, checklists, comments, and search results through the oo CLI after connecting a Trello account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands from OOMOL-controlled endpoints.

Mitigation: Prefer an official package manager or manually download and verify the installer before running setup commands.

Risk: The skill can run write and destructive Trello actions that change, archive, remove, or overwrite workspace data.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before allowing write or destructive operations.

Risk: Use depends on trusting OOMOL's Trello connector and account connection flow.

Mitigation: Install only when the user is comfortable with that connector trust boundary and verify Trello connection scopes before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-trello)
- [Trello homepage](https://trello.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Trello action payloads and execution guidance for read, write, and destructive operations.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
