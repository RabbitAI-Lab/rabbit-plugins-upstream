## Description:

WeCom Voice Agent helps an agent handle WeCom voice-message workflows, including intent recognition, multi-turn dialogue, task execution, outbound calling, call notes, compliant recording, call scheduling, declarative intents, custom intent plugins, unified session management, IVR menus, and entity extraction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, support teams, and developers use this skill to build or operate a WeCom voice assistant that routes transcribed voice messages into intents, actions, IVR flows, call records, and user-facing replies. It is intended for enterprise WeCom bot scenarios that need local processing, configurable intents, and controlled handling of voice-call records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive network, webhook, recording, and local retention behavior may be under-disclosed.

Mitigation: Review and reconcile the privacy and network disclosures before production use, including callback exposure, recording behavior, transcript storage, and retention periods.

Risk: Webhook and custom API integrations can expose enterprise data or secrets if deployed without hardened controls.

Mitigation: Use verified WeCom callback authentication, restrict allowed custom API destinations, protect secrets, and avoid directly exposing a local webhook without enterprise access controls.

Risk: Recordings, transcripts, sessions, tickets, and scheduled call data may persist locally beyond policy expectations.

Mitigation: Define and enforce retention, deletion, and access-control policies for all local voice, transcript, session, ticket, and scheduled-call data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)
- [Step-by-step setup guide](references/step_by_step_setup.md)
- [WeCom bot API reference](references/wecom_bot_api.md)
- [WeCom smart bot documentation](https://developer.work.weixin.qq.com/document/path/101039)
- [WeCom error code reference](https://developer.work.weixin.qq.com/document/path/90313)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON, YAML, Python, and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce WeCom text or voice replies, structured intent data, call summaries, local session records, and configuration edits depending on the workflow.]

## Skill Version(s):

2.6.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
