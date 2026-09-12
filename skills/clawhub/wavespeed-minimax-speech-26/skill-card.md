## Description:

Convert text to speech using MiniMax Speech 2.6 Turbo via WaveSpeed AI, with voice cloning, low-latency speech generation, multilingual support, emotion control, and voice presets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate speech audio from text through WaveSpeed AI's MiniMax Speech 2.6 Turbo model. It helps configure voice, emotion, speed, pitch, language, and audio output settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unpinned npm CLI or npx MCP setup can introduce normal package supply-chain risk.

Mitigation: Use pinned, reviewed package versions in sensitive environments.

Risk: Text submitted for speech generation is sent to WaveSpeed AI.

Mitigation: Install and use the skill only when that service is acceptable for the text or files being processed.

Risk: API keys may be exposed if pasted into chat.

Mitigation: Use the documented login flow or environment variable handling instead of sharing keys in chat.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wavespeed/skills/wavespeed-minimax-speech-26)
- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, API Calls]

**Output Format:** [Markdown with inline bash commands and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides text-to-speech requests that return generated audio URLs or downloaded audio files.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
