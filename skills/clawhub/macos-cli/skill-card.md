## Description:

Control a Mac from the terminal with the `macos` command (Calendar, Reminders, Contacts, Mail, Messages, Notes, Safari, Photos, Music, files, windows, screenshots, OCR, the Accessibility tree and system settings), where every command that returns data prints JSON with --json; run `macos doctor --for-agent` before anything else.

This skill is ready for commercial/non-commercial use.

## Publisher:

[manuaudio](https://clawhub.ai/user/manuaudio)

### License/Terms of Use:

MIT-0

## Use Case:

Mac users and their agents use this skill to inspect and manage macOS apps, personal data, files, and system settings through the `macos` command-line interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can retrieve sensitive personal data, including Keychain credentials and private messages.

Mitigation: Use only the data needed for the task and avoid exposing retrieved secrets or private content in responses.

Risk: Write commands can send messages, delete or alter data, and change system settings.

Mitigation: Run `macos doctor --for-agent` first, review each command's effects, and run write commands only when the person has requested that change.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/manuaudio/skills/macos-cli)
- [Project installation guide](https://github.com/manuaudio/macos-cli#install)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown instructions with shell command examples; command results are JSON when supported.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may read data or change macOS state depending on the requested action.]

## Skill Version(s):

0.9.1 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
