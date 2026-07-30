## Description: <br>
Create WorkoutSummary notes from strength-training recordings or transcripts. Accepts audio (.m4a, .mp3, .wav, .caf) and transcript files (.md, .txt, .srt, .vtt, .json); outputs total time, exercises completed, sets/reps, durations, and concise coach notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fangxuyi](https://clawhub.ai/user/fangxuyi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert strength-training recordings or transcripts into compact WorkoutSummary notes with total duration, completed exercises, sets, reps, durations, and concise coach cues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Audio transcription may use optional cloud services when configured, which can expose workout recordings or transcripts to a third-party provider. <br>
Mitigation: Use an existing transcript or local Whisper for privacy-sensitive sessions, and only use cloud transcription when the user has chosen and configured that provider. <br>
Risk: The exercise-matching helper may fetch and cache a public exercise dataset from GitHub. <br>
Mitigation: Provide a local exercises.json dataset when network fetching or local caching is not desired. <br>
Risk: Workout summaries could overstate sets, reps, weights, pain details, diagnoses, or medical conclusions if unsupported by the transcript. <br>
Mitigation: Keep counts and notes grounded in the transcript, mark uncertain values as approximate, and avoid medical conclusions. <br>


## Reference(s): <br>
- [Strength Training Recording Summary Workflow](references/summary-workflow.md) <br>
- [Exercise Dataset](https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json) <br>
- [Groq Audio Transcriptions API](https://api.groq.com/openai/v1/audio/transcriptions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text WorkoutSummary notes with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print the summary by default or save generated transcripts and summaries when the user supplies an output path.] <br>

## Skill Version(s): <br>
0.1.10 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
