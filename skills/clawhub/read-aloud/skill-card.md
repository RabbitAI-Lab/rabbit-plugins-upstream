## Description:

Read Aloud turns user-provided text into a playable MP3 using AudioFlow text-to-speech while preserving per-request approval for remote processing and billing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niuzb](https://clawhub.ai/user/niuzb)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they want an agent to read aloud, narrate, or create speech from supplied text. The skill confirms consent, sends the approved text to AudioFlow TTS, downloads the generated MP3 locally, and returns playback-oriented details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved text is transmitted to AudioFlow for text-to-speech processing.

Mitigation: Require explicit per-request approval before synthesis and review the prompt carefully before sending private or sensitive text.

Risk: AudioFlow may charge for billable characters when synthesis is approved.

Mitigation: Disclose the paid TTS cost before each synthesis and avoid automatic retries because an uncertain response may already have incurred a charge.

Risk: The skill depends on an AudioFlow API token stored on the machine or provided through the environment.

Mitigation: Use the skill only on machines where storing an AudioFlow token is acceptable; keep credentials private and do not echo, log, or place tokens in command arguments.

## Reference(s):

- [Read Aloud on ClawHub](https://clawhub.ai/niuzb/skills/read-aloud)
- [AudioFlow TTS Service Endpoint](https://asr.audioflow123.com)
- [AudioFlow Sign-Up](https://audioflow123.com/signup)
- [AudioFlow Billing Dashboard](https://audioflow123.com/dashboard/billing)
- [AudioFlow Dashboard](https://audioflow123.com/dashboard)

## Skill Output:

**Output Type(s):** [Text, Files, Shell commands, Configuration, Guidance]

**Output Format:** [JSON result with a local MP3 file path and concise Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts non-empty text up to 4,096 Unicode characters and an optional speed from 0.5 to 2.0; generated MP3 files are saved locally.]

## Skill Version(s):

1.0.2 (source: server release evidence and artifact Version section)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
