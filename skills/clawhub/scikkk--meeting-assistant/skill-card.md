## Description:

用于构建和排查 SenseAudio 会议助手，覆盖实时会议转写、说话人区分、实时翻译、会议纪要生成、行动项提取与转录导出。Build and troubleshoot SenseAudio meeting assistants for live meeting transcription, speaker-aware records, realtime translation, meeting note generation, action item extraction, and transcript export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scikkk](https://clawhub.ai/user/scikkk)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to build meeting assistants that combine SenseAudio ASR with live captions, speaker-aware transcription, translation, meeting notes, action item extraction, and transcript export. It supports both realtime WebSocket meetings and offline recording workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting audio and transcripts may contain sensitive participant, business, or regulated information and may be sent to SenseAudio.

Mitigation: Confirm participant consent and organizational approval before use, and avoid regulated or highly confidential meetings unless SenseAudio is sanctioned for that data.

Risk: API keys and historical transcript access can expose meeting data if stored or shared improperly.

Mitigation: Keep SENSEAUDIO_API_KEY in environment or secret storage, restrict access to transcript retrieval, and define encryption, retention, and deletion practices for recordings and logs.

Risk: Meeting summaries and action items can misstate decisions, owners, or deadlines if generated from incomplete or noisy transcripts.

Mitigation: Separate transcript text from model-generated summaries, preserve speaker and timestamp evidence, and mark uncertain owners or due dates instead of inventing them.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/scikkk/skills/meeting-assistant)
- [SenseAudio homepage](https://nightly.senseaudio.cn)
- [SenseAudio API key page](https://nightly.senseaudio.cn/platform/api-key)
- [Realtime Workflow](references/realtime-workflow.md)
- [Offline Meeting Transcription](references/offline-meeting-transcription.md)
- [Note Generation](references/note-generation.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown with code, shell command, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include meeting transcript schemas, API request examples, model selection guidance, and export-ready meeting notes.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
