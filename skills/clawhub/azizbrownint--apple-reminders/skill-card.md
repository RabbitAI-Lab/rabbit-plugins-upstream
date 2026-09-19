## Description:

List, add, edit, complete, or delete Apple Reminders and reminder lists via remindctl.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to manage Apple Reminders on macOS through the remindctl command-line tool, including listing, creating, editing, completing, and deleting reminders or reminder lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent to complete or delete reminders and delete reminder lists, which changes Apple Reminders data.

Mitigation: Confirm the user's intent and target reminder or list before running destructive remindctl commands.

Risk: The skill depends on a third-party macOS command-line tool installed through a Homebrew tap.

Mitigation: Review the remindctl Homebrew tap and install only on macOS systems where Apple Reminders access is intended.

## Reference(s):

- [remindctl](https://github.com/steipete/remindctl)
- [ClawHub skill page](https://clawhub.ai/azizbrownint/skills/apple-reminders)
- [Publisher profile](https://clawhub.ai/user/azizbrownint)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS-only workflow requiring the remindctl binary and Apple Reminders permission.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
