## Description: <br>
Use when the user has audio or video and wants a timestamped transcript (SRT) in the source language, routing Chinese audio to Volcano ASR and other supported languages to OpenAI Whisper with word-level timestamps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hanshaoyuyehanshaoyuye](https://clawhub.ai/user/hanshaoyuyehanshaoyuye) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, creators, and agents use this skill to turn source audio or video into source-language SRT subtitles with timestamped, punctuation-bounded cues. It is especially tuned for Chinese transcription via Volcano ASR and multilingual transcription via OpenAI Whisper. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio and transcript data may be sent to external transcription services. <br>
Mitigation: Use the skill only when sharing the audio with OpenAI or ByteDance/Volcano is acceptable for the use case. <br>
Risk: The workflow depends on local API credentials exposed to the agent session. <br>
Mitigation: Prefer narrowly scoped environment variables and avoid sourcing broad environment files when a smaller credential set is sufficient. <br>
Risk: ASR output can contain transcription errors, especially proper nouns and Chinese homophones. <br>
Mitigation: Review the generated SRT and correction diff before downstream publishing or reuse. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/hanshaoyuyehanshaoyuye/skills/wjs-transcribing-audio) <br>
- [OpenAI Audio Transcriptions API](https://api.openai.com/v1/audio/transcriptions) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell and Python examples that produce SRT subtitle files and ASR JSON intermediates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces source-language SRT with HH:MM:SS,mmm timestamps, sequential cues, punctuation-bounded segmentation, and optional Chinese correction review.] <br>

## Skill Version(s): <br>
8.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
