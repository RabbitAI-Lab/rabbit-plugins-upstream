## Description: <br>
Summarize strength-training recordings/transcripts into WorkoutSummary notes with durations, sets/reps, and coach cues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fangxuyi](https://clawhub.ai/user/fangxuyi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users use this skill to turn local strength-training recordings or transcript files into concise WorkoutSummary notes. It preserves timing evidence where available, summarizes exercises, sets, reps, durations, and coach cues, and supports Chinese/English trainer sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Workout audio and transcripts can contain sensitive personal information, and optional cloud transcription sends files to a third-party provider. <br>
Mitigation: Prefer local Whisper for private recordings; use Groq, OpenAI, or another cloud backend only when credentials are configured and the user explicitly accepts upload to that provider. <br>
Risk: The exercise matching helper can download and cache an external exercise dataset when no local dataset or cache path is supplied. <br>
Mitigation: Pre-supply a local exercise dataset or approved cache path in environments that should avoid automatic external downloads. <br>
Risk: Transcription uncertainty can lead to incorrect durations, sets, reps, or health-related claims in the summary. <br>
Mitigation: Preserve segment timestamps, calculate durations from transcript ranges where possible, mark ambiguous values as approximate, and do not invent weights, pain details, diagnoses, or medical conclusions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fangxuyi/skills/strength-training-recording-summary) <br>
- [Strength Training Recording Summary Workflow](references/summary-workflow.md) <br>
- [hasaneyldrm exercises dataset](https://raw.githubusercontent.com/hasaneyldrm/exercises-dataset/main/data/exercises.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or plain text WorkoutSummary notes with optional inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print the summary directly or save transcript and summary files when the user requests an output path or recurring local workflow.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
