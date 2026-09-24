## Description:

GPT-only: turns text into expressive speech and a verified audio file in ChatGPT Work/Codex; requires GPT browser control and FFmpeg/FFprobe, and is not native to OpenClaw.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ciklopentan](https://clawhub.ai/user/ciklopentan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to convert supplied text into expressive speech, assemble MP3 segments, and validate the final audio file before delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Browser-based TTS services may receive text supplied to the agent.

Mitigation: Use the skill for non-sensitive text, require local synthesis for private material, or get explicit permission before sending confidential content to a TTS service.

Risk: The manifest product scope and implicit invocation setting are broader than the skill documentation.

Mitigation: Review the configured product list and implicit invocation setting before broad deployment.

Risk: External TTS service limits, voices, and output behavior can change.

Mitigation: Recheck current service limits before each run and validate segment count, duration, ordering, and MP3 decoding before delivery.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ciklopentan/skills/text-to-audio-gpt)
- [TTSFree Russian text-to-speech page](https://ttsfree.com/text-to-speech/ru)

## Skill Output:

**Output Type(s):** [Files, Shell commands, Guidance]

**Output Format:** [MP3 audio file with concise Markdown status and validation details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires browser-accessible TTS plus FFmpeg/FFprobe; validates MP3 segment compatibility, duration, and decoding.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
