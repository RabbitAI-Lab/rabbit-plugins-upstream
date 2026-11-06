## Description:

Deploy and manage hosted OpenClaw or Hermes bots on OpenClaw Launch, including bot setup, chat, Telegram connection, and lifecycle controls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zackchewa](https://clawhub.ai/user/zackchewa)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to deploy and operate hosted OpenClaw or Hermes bots through OpenClaw Launch, including chatting with bots and connecting them to Telegram.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API key can use the account's balance, plan limits, and model funding.

Mitigation: Use a dedicated, revocable key and review current charges and auto-reload settings before creating bots. Keep the key out of chat and logs.

Risk: Creating a bot can incur charges; stopping a bot may leave hosting billing active, while deletion permanently erases its data.

Mitigation: Confirm the bot details and billing before creation. Check current rates, and confirm the named bot before deletion.

Risk: Chat content and any Telegram token supplied are shared with the hosting provider; Telegram group mentions can receive replies.

Mitigation: Only share content and tokens intended for the provider, and consider where the bot is added and who can mention it in groups.

Risk: Provider-side permission enforcement was not tested.

Mitigation: Review provider access controls and limit bot use to the audiences and data appropriate for your deployment.

## Reference(s):

- [OpenClaw Launch Build & Resell](https://openclawlaunch.com/build-and-resell)
- [OpenClaw Launch Developer Portal](https://openclawlaunch.com/developer)
- [OpenClaw Launch ClawHub Release](https://clawhub.ai/zackchewa/skills/openclawlaunch)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Natural-language responses with inline shell command examples and bot/API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires OPENCLAW_LAUNCH_API_KEY; TELEGRAM_BOT_TOKEN is optional for Telegram connection.]

## Skill Version(s):

1.0.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
