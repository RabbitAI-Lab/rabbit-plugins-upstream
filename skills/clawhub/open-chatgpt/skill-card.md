## Description:

Opens Brave browser directly to ChatGPT for instant AI conversations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to open ChatGPT quickly in Brave from a voice or typed trigger phrase, especially when switching between AI tools or preparing to paste content into ChatGPT.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill launches Brave and opens an external ChatGPT web session, and the inspected Windows path uses shell=True.

Mitigation: Install only if that browser-launch behavior is expected; review Windows launch behavior before managed or enterprise deployment.

## Reference(s):

- [ChatGPT](https://chat.openai.com)
- [ClawHub skill page](https://clawhub.ai/ruchir17-cmd/skills/open-chatgpt)

## Skill Output:

**Output Type(s):** [Shell commands, Text, Guidance]

**Output Format:** [Text status message with platform-specific browser launch command behavior]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Opens an external Brave browser session to ChatGPT; requires Brave, internet access, and a ChatGPT account.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
