## Description:

Operate Rocket.Chat through an OOMOL-connected account to read rooms and messages and to post, update, or delete messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Rocket.Chat profiles, rooms, and messages, and to post, update, or delete messages through the oo CLI with user confirmation for write or destructive actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup instructions include one-line remote installer commands that execute mutable code.

Mitigation: Use an official, pinned, and verifiable installation method before relying on the oo CLI.

Risk: The skill can post, update, or delete Rocket.Chat messages.

Mitigation: Confirm the exact target, payload, and expected effect with the user before allowing write or destructive actions.

## Reference(s):

- [ClawHub Rocket.Chat skill page](https://clawhub.ai/oomol/skills/oo-rocket-chat)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Rocket.Chat homepage](https://www.rocket.chat)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown or text with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector command results are JSON objects that include returned data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
