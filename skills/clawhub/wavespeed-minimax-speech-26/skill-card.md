## Description:

Convert text to speech using MiniMax Speech 2.6 Turbo via WaveSpeed AI, with voice selection, emotion control, language options, and audio output settings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wavespeed](https://clawhub.ai/user/wavespeed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate spoken audio from text through WaveSpeed AI's MiniMax Speech 2.6 Turbo model, including voice, emotion, language, and output-format controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on live npm packages for the WaveSpeed CLI or MCP server.

Mitigation: Verify the package publisher before installation and pin reviewed versions or run the tooling in an isolated environment when appropriate.

Risk: WaveSpeed credentials are stored locally or supplied through an environment variable.

Mitigation: Use wavespeed login or WAVESPEED_API_KEY as documented, and do not paste API keys into chat.

## Reference(s):

- [WaveSpeed MCP server](https://github.com/WaveSpeedAI/mcp-server)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The external WaveSpeed run returns an audio output URL and can download audio files when requested.]

## Skill Version(s):

2.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
