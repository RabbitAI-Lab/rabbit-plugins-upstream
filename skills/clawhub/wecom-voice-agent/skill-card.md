## Description:

wecom-voice-agent helps agents configure and operate a WeCom voice assistant for voice-message intake, intent routing, call workflows, consented recording, follow-up tasks, and ticket escalation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and enterprise WeCom administrators use this skill to deploy a voice assistant that interprets WeCom voice-message transcripts, routes intents, manages call records, schedules follow-ups, and escalates strong negative sentiment into tickets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive call transcripts, tickets, phone numbers, memory entries, and emotion labels may be stored or shared in enterprise deployments.

Mitigation: Review and approve data handling before production use, including retention, access controls, and sharing boundaries for call records, tickets, phone numbers, and emotion labels.

Risk: Optional MCP, supervisor webhook, and custom-intent integrations can invoke configured executable paths or enterprise endpoints.

Mitigation: Enable ZWJH_MCP_SERVER, SUPERVISOR_WEBHOOK, and custom_intents.yaml only after paths and endpoints are allowlisted, credentials are protected, TLS verification is fixed, and administrators approve the integrations.

Risk: A public webhook endpoint can expose enterprise voice workflows if it is not deployed behind validated WeCom signatures and hardened HTTPS.

Mitigation: Expose the webhook only behind validated WeCom signatures and a hardened HTTPS deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)
- [WeCom bot API reference](references/wecom_bot_api.md)
- [Step-by-step setup guide](references/step_by_step_setup.md)
- [WeCom intelligent bot official documentation](https://developer.work.weixin.qq.com/document/path/101039)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with JSON/YAML configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes local Python scripts and configuration files for WeCom voice workflows.]

## Skill Version(s):

2.7.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
