## Description:

Create, view, edit, delete, search, move, or export Apple Notes via the memo CLI on macOS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers on macOS use this skill to create, find, edit, move, export, and delete Apple Notes through the memo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read, export, edit, move, and delete Apple Notes after macOS grants Automation access.

Mitigation: Preview or list notes before modifying them, and revoke Notes.app Automation permission when CLI access is no longer needed.

Risk: The skill depends on a third-party memo CLI and Homebrew tap.

Mitigation: Install only when the memo project and tap are trusted, and review the dependency before use.

## Reference(s):

- [memo CLI project](https://github.com/antoniorodr/memo)
- [apple-notes on ClawHub](https://clawhub.ai/azizbrownint/skills/apple-notes)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [macOS-only; requires the memo CLI and Apple Notes Automation permission.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
