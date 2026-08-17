## Description:

Helps an agent operate a WeCom voice assistant that handles voice-to-text callbacks, intent routing, office-task responses, call records, voicemail summaries, and consent-aware call recording.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WeCom administrators use this skill to configure and test a voice-enabled enterprise assistant for single-chat voice callbacks, weather and time responses, scheduling or todo workflows, message sending, and call follow-up. It is intended for enterprise messaging and voice-call workflows where callback authentication, secret handling, retention, and recording consent are configured by the deploying organization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public webhook exposure can allow unauthorized callback traffic or message injection if deployed without strong authentication.

Mitigation: Deploy only behind authenticated HTTPS and enable WeCom signature, token, and EncodingAESKey validation before production use.

Risk: WeCom secrets and callback credentials could be exposed through local configuration, examples, logs, or public tunnel workflows.

Mitigation: Store secrets outside shared files, restrict access to deployment logs, and avoid ad hoc public tunnels for production deployments.

Risk: Sessions, transcripts, recordings, logs, tickets, and call records may contain sensitive voice or business data.

Mitigation: Configure explicit retention and deletion policies for all local data stores and verify recording consent before retaining call audio or transcripts.

## Reference(s):

- [Step-by-step WeCom smart robot setup](artifact/references/step_by_step_setup.md)
- [WeCom smart robot API reference](artifact/references/wecom_bot_api.md)
- [WeCom smart robot official documentation](https://developer.work.weixin.qq.com/document/path/101039)
- [WeCom API error code reference](https://developer.work.weixin.qq.com/document/path/90313)
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples, shell commands, and generated text or Markdown call summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May also create local session, transcript, recording metadata, statistics, and template files when its helper scripts are run.]

## Skill Version(s):

2.5.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
