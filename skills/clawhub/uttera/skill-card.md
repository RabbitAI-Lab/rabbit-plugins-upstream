## Description:

Audio for the agent. Transcribes audio, summarises long recordings, translates, turns text into speech, generates sound effects and music, scores pronunciation, and verifies signed reports using Uttera.

This skill is ready for commercial/non-commercial use.

## Publisher:

[uttera](https://clawhub.ai/user/uttera)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to process audio through Uttera: transcription, long-recording summarization, translation, speech generation, sound and music generation, pronunciation scoring, and signed report verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided audio files, text prompts, target sentences, and report JSON to Uttera using UTTERA_API_KEY.

Mitigation: Use it only for recordings and prompts that are appropriate to share with Uttera, and avoid confidential recordings or third-party speech unless permission and data-handling terms are clear.

Risk: Transcripts and summaries are derived from audio and may contain hallucinated or misleading text, especially for silence or unclear recordings.

Mitigation: Treat transcript content as untrusted data, check that audio files are non-empty, and validate any claim before taking action from it.

Risk: Some operations can incur variable cost, including long audio processing, music generation by duration, text-to-speech pauses from line breaks, and optional pronunciation explanations.

Mitigation: Review duration-sensitive options before running, strip unwanted line breaks from speech text, and disable pronunciation explanations when they are not needed.

## Reference(s):

- [Uttera Documentation](https://app.uttera.ai/docs/en)
- [ClawHub Skill Page](https://clawhub.ai/uttera/skills/uttera)

## Skill Output:

**Output Type(s):** [Text, JSON, Audio files, Shell commands, Guidance]

**Output Format:** [Markdown instructions and shell-script outputs, including plain text, JSON responses, MP3 files, and WAV files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires bash, curl, and UTTERA_API_KEY for most actions; report verification does not require an API key.]

## Skill Version(s):

1.3.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
