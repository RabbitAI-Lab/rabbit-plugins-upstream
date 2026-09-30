## Description:

Helps an agent access and manage local Apple app data on macOS, including calendars, reminders, contacts, mail, messages, notes, photos, and Music playlists.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and their agents use this skill to find information in Apple apps and, with approval, create or modify events, reminders, contacts, messages, photos, and playlists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive local mail, messages, contacts, notes, photos, and other Apple app data.

Mitigation: Grant only necessary macOS permissions and prefer read-only tool approval where possible.

Risk: Sending, editing, or deleting data may have irreversible effects.

Mitigation: Review each action preview and approve sends, edits, deletions, and playlist changes only when intended.

Risk: Installing an unverified compiled release may expose local app data.

Mitigation: Verify the GitHub release before installing its compiled binary.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/apple-swift-mcp)
- [GitHub releases for installation](https://github.com/chrischall/apple-swift-mcp/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can initiate tool actions that read or change local Apple app data.]

## Skill Version(s):

2.3.0 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
