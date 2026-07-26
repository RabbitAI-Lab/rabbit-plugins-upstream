## Description: <br>
Wecom Voice Agent helps agents handle WeCom voice interactions, including voice-message transcription handling, intent routing, task responses, call flows, meeting minutes, scheduling, compliance recording, and emotion-aware replies. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fyniujin](https://clawhub.ai/user/fyniujin) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and WeCom administrators use this skill to prototype and operate a WeCom voice assistant for employee-facing voice messages, call handling, task routing, scheduling, transcript summaries, and consent-based recording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The webhook processes WeCom callbacks and may handle sensitive call, transcript, session, and emotion data. <br>
Mitigation: Deploy only in an admin-controlled WeCom environment with HTTPS, WeCom signature/AES validation, restricted inbound access, and protected Token, Secret, and AESKey values. <br>
Risk: Outbound and batch calling, recording, transcription, and emotion tracking can create consent, retention, and disclosure obligations. <br>
Mitigation: Review or disable those features until consent flows, retention limits, deletion procedures, and local file-permission controls are approved. <br>
Risk: The artifact documents local recording, transcript, session, and call-record storage. <br>
Mitigation: Limit local storage to necessary data, restrict filesystem permissions, and enforce retention and deletion policies for recordings, transcripts, session files, and call records. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent) <br>
- [Step-by-step setup guide](references/step_by_step_setup.md) <br>
- [WeCom bot API reference](references/wecom_bot_api.md) <br>
- [WeCom official site](https://work.weixin.qq.com) <br>
- [WeCom intelligent bot documentation](https://developer.work.weixin.qq.com/document/path/101039) <br>
- [WeCom error code documentation](https://developer.work.weixin.qq.com/document/path/90313) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples, Python code paths, shell commands, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local operational guidance and helper-script outputs for WeCom voice, call, transcript, scheduling, recording, and emotion-analysis workflows.] <br>

## Skill Version(s): <br>
2.2.0 (source: SKILL.md frontmatter, README version history, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
