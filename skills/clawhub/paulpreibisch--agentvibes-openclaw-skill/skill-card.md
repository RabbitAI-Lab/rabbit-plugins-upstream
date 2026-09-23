## Description:

AgentVibes provides offline text-to-speech controls for Claude Code and OpenClaw, including voice switching, personality styles, speed, effects, background music, language learning mode, verbosity, mute, replay, and provider selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[paulpreibisch](https://clawhub.ai/user/paulpreibisch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to manage text-to-speech voice selection, speech style, playback options, and language learning narration for Claude Code and OpenClaw sessions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact is documentation-only and does not include the AgentVibes runtime that performs TTS downloads or playback.

Mitigation: Review the separate runtime or plugin before granting file, network, or system audio permissions.

Risk: Voice downloads and audio playback may rely on components outside the inspected artifact.

Mitigation: Confirm the active provider and permissions before enabling downloads, background music, effects, or replay in shared or sensitive environments.

## Reference(s):

- [Piper Voices on Hugging Face](https://huggingface.co/rhasspy/piper-voices)
- [ClawHub Skill Page](https://clawhub.ai/paulpreibisch/skills/agentvibes-openclaw-skill)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown with slash-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill documents voice, provider, playback, effects, language, verbosity, and cleanup commands; the inspected artifact does not include executable TTS code.]

## Skill Version(s):

4.6.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
