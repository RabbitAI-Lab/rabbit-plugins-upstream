## Description: <br>
Transcribe pre-recorded audio files or URLs with Gladia for batch or asynchronous transcription, speaker diarization, subtitles, PII redaction, translation, named entity recognition, summarization, chapterization, audio-to-LLM, and related audio intelligence workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gladiaio](https://clawhub.ai/user/gladiaio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to implement SDK-first pre-recorded audio and video transcription workflows with Gladia, including job creation, polling or webhook delivery, job management, and extraction of transcript and audio intelligence results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio files, audio URLs, transcripts, and derived audio intelligence may be sent to Gladia for processing. <br>
Mitigation: Confirm the user is allowed to share the audio or URL with Gladia, and avoid confidential, regulated, or highly personal recordings unless Gladia's retention, compliance, and privacy terms meet the use case. <br>
Risk: Incorrect polling or raw REST usage can create excessive requests or missed job completion handling. <br>
Mitigation: Prefer the official SDK, use webhooks or callbacks when suitable, and apply exponential backoff when raw REST polling is necessary. <br>


## Reference(s): <br>
- [Transcription Options Reference](artifact/references/transcription-options.md) <br>
- [Managing Pre-Recorded Jobs](artifact/references/managing-jobs.md) <br>
- [Delivery and Response Reference](artifact/references/delivery-and-response.md) <br>
- [Pre-recorded quickstart](https://docs.gladia.io/chapters/pre-recorded-stt/quickstart) <br>
- [Audio intelligence overview](https://docs.gladia.io/chapters/pre-recorded-stt/audio-intelligence) <br>
- [API reference: pre-recorded init](https://docs.gladia.io/api-reference/v2/pre-recorded/init) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, markdown] <br>
**Output Format:** [Markdown guidance with JavaScript, TypeScript, Python, JSON, and REST examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include SDK-first recommendations, raw REST fallback steps, transcription option mappings, polling guidance, webhook notes, and response parsing guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
