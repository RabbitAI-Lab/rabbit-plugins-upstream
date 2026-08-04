## Description: <br>
Join Meeting helps an agent join supported online meetings, monitor voice state, manage meeting lifecycle events, generate transcripts and summaries, and handle TTS playback events. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teams, workflow operators, and agent developers use this skill to automate meeting participation, transcription, TTS interaction, and post-meeting summaries where meeting-platform APIs and organizational policies allow it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic meeting participation, listening, transcription, and record storage can occur without clear consent, authorization, retention, or permission boundaries. <br>
Mitigation: Use only where participants are informed and consent, where the organization allows bots, transcription, and recording, and where transcript retention and deletion are defined. <br>
Risk: The skill requests broad read, write, and shell execution capabilities while relying on meeting-platform and TTS credentials. <br>
Mitigation: Limit credentials and file access, avoid granting shell execution unless the publisher narrows its need, and keep API keys scoped and out of logs or version control. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/join-meeting) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured JSON-style status output with configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include meeting status, transcript excerpts, summaries, action items, execution logs, and error details.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
