## Description: <br>
AgentCall lets an AI agent join Google Meet, Microsoft Teams, or Zoom meetings as a bot with voice, visual presence, real-time transcription, chat, screenshots, and optional screensharing. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[johnpatternai](https://clawhub.ai/user/johnpatternai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to let an AI agent attend and participate in video meetings, including speaking, listening to transcripts, sharing visual content, and helping with meeting workflows such as note-taking or support calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Meeting transcripts become agent input, so meeting participants may influence the agent's behavior during a call. <br>
Mitigation: Use the skill in trusted meetings or configure strict agent permissions before joining. <br>
Risk: Webpage modes can share local pages through AgentCall, which may expose unintended local content if the wrong service or port is selected. <br>
Mitigation: Share only intended local servers or public URLs, verify ports before use, and avoid exposing sensitive localhost services. <br>
Risk: API keys, transcripts, audio, or example logs may persist after use. <br>
Mitigation: Review saved AgentCall API keys and clean up transcript, audio, and log files according to the user's retention expectations. <br>


## Reference(s): <br>
- [AgentCall homepage](https://agentcall.dev) <br>
- [Skill README](README.md) <br>
- [Complete Skill Reference](SKILL.md) <br>
- [AgentCall API Reference](references/api.md) <br>
- [Collaborative Mode Guide](references/guides/collaborative-mode.md) <br>
- [Interruption Handling Guide](references/guides/interruption-handling.md) <br>
- [Crash Recovery Guide](references/guides/crash-recovery.md) <br>
- [Webpage AV Guide](references/guides/webpage-av.md) <br>
- [Webpage AV Screenshare Guide](references/guides/webpage-av-screenshare.md) <br>
- [Webpage Audio Guide](references/guides/webpage-audio.md) <br>
- [UI Templates Guide](references/guides/ui-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON command examples, configuration snippets, and optional generated meeting notes or logs.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill can also drive meeting-side speech, chat, screenshots, and screenshare actions through AgentCall when invoked by an agent.] <br>

## Skill Version(s): <br>
1.1.15 (source: server release evidence and .claude-plugin/plugin.json, released 2026-07-01 in CHANGELOG.md) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
