## Description:

Read, search and send Hike Messenger chats via the hkcli command-line tool. Use when the user asks about their Hike messages or wants to message someone on Hike.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vinaycodeaxe](https://clawhub.ai/user/vinaycodeaxe)

### License/Terms of Use:

MIT-0

## Use Case:

People who use Hike can ask an agent to read, search, and summarize chats, inspect contacts or groups, and download media through their logged-in hkcli account. They can also ask it to send a text or file after confirming the recipient and exact content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports benign with medium confidence, but notes an unresolved local reference and partial analysis; its verdict is not a guarantee of safety.

Mitigation: Review the unresolved reference and decide whether the skill's purpose and scope are acceptable before installing.

Risk: The skill can access private Hike messages and send text or files through the logged-in account.

Mitigation: Use --read-only for read-only tasks. Before sending, confirm the resolved recipient and exact content with the user, and quote only the private content needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vinaycodeaxe/skills/hkcli)
- [hkcli documentation](https://vinaycodeaxe.github.io/hkcli/)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Text or JSON results and concise guidance, with shell command examples where useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include private chat excerpts; quote only what the user needs.]

## Skill Version(s):

1.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
