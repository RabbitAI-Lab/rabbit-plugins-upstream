## Description:

AgentCall lets an AI agent join Google Meet, Microsoft Teams, and Zoom meetings as a bot with voice conversation, visual presence, screenshare, chat, and real-time transcription.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnpatternai](https://clawhub.ai/user/johnpatternai)

### License/Terms of Use:

MIT

## Use Case:

Developers and AI-agent users use this skill to bring an agent into live meetings for voice participation, note-taking, support, coding collaboration, presentation support, and meeting-aware task execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Live meeting participants can influence the agent through transcripts while the agent may have local tool access.

Mitigation: Use only in trusted meetings or sandboxed projects with a narrow tool allowlist, and require explicit local confirmation before file reads, shell commands, code edits, commits, credential access, or new network destinations.

Risk: AgentCall API keys may be stored in local config or exposed through environment handling.

Mitigation: Prefer environment or OS secret storage, avoid exposing keys in chats or repositories, and rotate keys if exposed.

Risk: Tunnels, shared local webpages, or saved transcripts may expose sensitive local applications or confidential meeting content.

Mitigation: Tunnel only intentional local services and avoid saving confidential transcripts in repositories.

Risk: Stop hooks can keep an agent loop active while a meeting call is in progress.

Mitigation: Avoid the Stop hook unless needed, understand its persistence behavior, and remove it after the call.

## Reference(s):

- [README](artifact/README.md)
- [Skill reference](artifact/SKILL.md)
- [AgentCall API reference](artifact/references/api.md)
- [Collaborative mode guide](artifact/references/guides/collaborative-mode.md)
- [Crash recovery guide](artifact/references/guides/crash-recovery.md)
- [Interruption handling guide](artifact/references/guides/interruption-handling.md)
- [Webpage audio guide](artifact/references/guides/webpage-audio.md)
- [Webpage AV guide](artifact/references/guides/webpage-av.md)
- [Webpage AV screenshare guide](artifact/references/guides/webpage-av-screenshare.md)
- [UI templates guide](artifact/references/guides/ui-templates.md)
- [AgentCall website](https://agentcall.dev)
- [AgentCall API keys](https://app.agentcall.dev/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration snippets, and JSON command/event examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a meeting URL and may use mode, voice strategy, port, template, timeout, and AgentCall API key settings.]

## Skill Version(s):

1.1.15 (source: evidence release, .claude-plugin/plugin.json, and CHANGELOG released 2026-07-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
