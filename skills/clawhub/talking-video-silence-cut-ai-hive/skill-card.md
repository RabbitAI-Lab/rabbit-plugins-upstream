## Description:

Helps Chinese-speaking content teams turn raw talking-video footage into a reviewable workflow for removing filler, preserving meaning, generating timecodes and subtitles, and producing vertical edits with optional AI-HIVE generation support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, sales teams, and content operators use this skill to plan and execute Chinese talking-video cleanup. It produces retained-section plans, deletion guidance, timecodes, subtitles, vertical-format edit commands, and optional AI-HIVE generation task records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store an AI-HIVE API key.

Mitigation: Use environment variables or a protected local config, avoid pasting real keys into chat or logs, and keep generated examples as placeholders.

Risk: The skill can upload user-selected media to AI-HIVE and submit potentially billable generation jobs.

Mitigation: Confirm media authorization, prompts, routing mode, pricing snapshot, and file paths before any upload or generation command.

Risk: The skill writes downloaded outputs and generated project files locally.

Mitigation: Choose output directories deliberately, preserve original source media, and inspect generated files before publication.

Risk: Aggressive removal of pauses, repetition, or off-topic sections can alter the speaker's intended meaning.

Mitigation: Review retained and deleted segments before final export, preserving negations, limitations, risk notices, and required factual context.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/wubin1836/skills/talking-video-silence-cut-ai-hive)
- [ClawHub publisher profile](https://clawhub.ai/user/wubin1836)
- [AI-HIVE chat entry](https://ai-hive.iclip.cn/chat)
- [AI-HIVE API base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance with bash commands, JSON project briefs, local media files, and AI-HIVE task records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-selected media to AI-HIVE, poll asynchronous generation tasks, and download outputs locally; local deterministic video edits require ffmpeg.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
