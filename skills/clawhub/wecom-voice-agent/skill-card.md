## Description:

WeCom Voice Agent helps developers deploy a WeCom voice assistant for voice-message callbacks, intent routing, call workflows, and local call record handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WeCom administrators use this skill to test and deploy a WeCom smart robot that accepts voice-message callbacks, converts transcribed speech into office intents, and returns text or voice-style responses. It also supports prototyping outbound call scheduling, IVR-style call handling, voicemail summaries, ticket creation, and local call record workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a public callback service and the scanner describes it as unauthenticated.

Mitigation: Require WeCom signature and encryption validation, serve the callback over HTTPS, add rate limiting, and manage callback secrets outside the skill files before production use.

Risk: The skill stores business voice, transcript, voicemail, ticket, and call metadata locally.

Mitigation: Set explicit retention and deletion controls, restrict filesystem and database access, and confirm callers and users receive appropriate notice and consent.

Risk: Automatic ticketing, voicemail recording, outbound calls, and batch workflows can affect users or customers without sufficient governance.

Mitigation: Disable these workflows until administrators approve them and operational review confirms the intended consent, authorization, and escalation process.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)
- [Step-by-step setup guide](references/step_by_step_setup.md)
- [WeCom bot API reference](references/wecom_bot_api.md)
- [WeCom official smart robot API documentation](https://developer.work.weixin.qq.com/document/path/101039)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include local file paths, HTTP callback configuration, and runnable Python command examples.]

## Skill Version(s):

2.5.1 (source: evidence.json release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
