## Description:

Read, search and send Hike Messenger chats via the hkcli command-line tool. Use when the user asks about their Hike messages or wants to message someone on Hike.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinaycodeaxe](https://clawhub.ai/user/vinaycodeaxe)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use hkcli to read, search, or summarize Hike chats and to send messages or files when specifically requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because one referenced local path could not be resolved.

Mitigation: Consider whether the unresolved reference matters before installing; completed scans reported no findings.

Risk: Sending Hike messages or files can expose private content or reach the wrong recipient.

Mitigation: Act only when asked, resolve the recipient, show the exact content, and wait for the user's confirmation before sending.

## Reference(s):

- [hkcli documentation](https://vinaycodeaxe.github.io/hkcli/)
- [ClawHub skill release](https://clawhub.ai/vinaycodeaxe/skills/hkcli)
- [hkcli Go module](https://github.com/vinaycodeaxe/hkcli)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text, Files]

**Output Format:** [Markdown guidance and shell command examples; chat content as text or downloaded files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires hkcli and a valid Hike login; sending requires user confirmation of the resolved recipient and exact content.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
