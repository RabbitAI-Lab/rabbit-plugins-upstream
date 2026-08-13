## Description:

WeCom Voice Agent helps an agent run an Enterprise WeChat voice assistant for voice-message handling, intent parsing, office task execution, outbound calls, call summaries, scheduling, and weather or time queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and workplace automation teams use this skill to set up, test, and operate a WeCom voice assistant for voice-driven office workflows. It supports webhook setup, simulated voice-message testing, schedule and todo intents, weather and time responses, message sending, outbound call handling, call minutes, and local operational scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes a webhook for WeCom callbacks.

Mitigation: Deploy only on a hardened server and add callback verification, HTTPS, replay protection, and operational monitoring before public exposure.

Risk: Voice transcripts, recordings, sessions, tickets, and call records may contain sensitive personal or business information.

Mitigation: Define retention and deletion rules, keep records local where required, restrict access, and avoid placing CorpID or Secret values in commands, logs, or source files.

Risk: Automatic emotion analysis and ticket creation can affect users without clear expectations.

Mitigation: Enable these features explicitly, disclose them to users, and review generated tickets or escalations before acting on sensitive outcomes.

## Reference(s):

- [Step-by-step WeCom setup guide](references/step_by_step_setup.md)
- [WeCom bot API reference](references/wecom_bot_api.md)
- [WeCom intelligent robot official documentation](https://developer.work.weixin.qq.com/document/path/101039)
- [WeCom API error codes](https://developer.work.weixin.qq.com/document/path/90313)
- [ClawHub skill page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown instructions with JSON examples, Python script references, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes webhook deployment guidance, local Python utilities, JSON strategy templates, and sample session data for testing.]

## Skill Version(s):

2.4.0 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
