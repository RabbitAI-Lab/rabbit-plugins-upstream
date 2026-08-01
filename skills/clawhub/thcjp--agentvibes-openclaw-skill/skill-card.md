## Description: <br>
AgentVibes OpenClaw Skill lets agents provide configurable text-to-speech with voice switching, personality styles, speed controls, effects, background music, replay, translation, and provider management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add spoken output to OpenClaw, Codex-style, Cursor, or similar assistant sessions, including voice selection, previews, replay, language-learning speech, and local provider control. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill expects exec-capable behavior for audio playback, updates, cleanup, downloads, and related local actions. <br>
Mitigation: Review the skill before installation, run it only in trusted workspaces, and require explicit /agent-vibes commands before local command execution. <br>
Risk: Voice downloads and update commands can introduce unreviewed external files or behavior. <br>
Mitigation: Confirm the provider and source before downloading or updating, and prefer reviewed voice packages from known sources. <br>
Risk: Cached and replayable spoken outputs may retain sensitive text from recent assistant responses. <br>
Mitigation: Avoid speaking secrets or regulated data, use mute when handling sensitive content, and clean cached audio when retention is not needed. <br>
Risk: Broad automatic triggers may cause unwanted speech or actions during normal agent work. <br>
Mitigation: Prefer explicit /agent-vibes commands and avoid enabling broad automatic triggers unless the workspace owner has reviewed the behavior. <br>


## Reference(s): <br>
- [Agentvibes Openclaw Skill on ClawHub](https://clawhub.ai/thcjp/skills/agentvibes-openclaw-skill) <br>
- [Piper voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance, Audio] <br>
**Output Format:** [Markdown guidance with slash commands, inline command examples, and generated spoken audio through configured TTS providers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Retains recent spoken outputs for replay and may download voices, update tooling, or delete cached audio when explicitly directed.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 4.6.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
