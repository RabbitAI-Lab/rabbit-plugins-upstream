## Description:

Trello lets an agent read, create, update, search, and archive Trello boards, lists, cards, labels, members, checklists, comments, and attachments through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Trello workspaces from an agent session through the OOMOL oo CLI, including reading Trello data, creating or updating boards, lists, cards, checklists, comments, attachments, labels, and members, and performing explicitly confirmed destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include unpinned remote installer commands that can execute code on the user's machine.

Mitigation: Review the setup path before installing, install the oo CLI from trusted OOMOL documentation, and inspect installer code before running it.

Risk: The skill can change or archive Trello content through connected-account actions.

Mitigation: Confirm exact payloads for write actions and require explicit approval before destructive actions such as archiving cards or lists or removing labels or members.

Risk: Connected Trello credentials may grant access beyond the immediate task.

Mitigation: Connect Trello only with permissions the user is comfortable granting and re-check connection or scope errors before retrying.

## Reference(s):

- [ClawHub Trello skill page](https://clawhub.ai/oomol/skills/oo-trello)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Trello homepage](https://trello.com)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI commands and connector JSON responses; write and destructive Trello actions require user confirmation.]

## Skill Version(s):

1.0.4 (source: SKILL.md metadata and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
