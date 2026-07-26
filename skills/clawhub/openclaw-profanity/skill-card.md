## Description: <br>
Content moderation plugin for OpenClaw/Moltbot AI agents. Use when building chatbots that need profanity filtering, moderating user messages in Discord/Slack/Telegram bots, or adding content moderation to OpenClaw agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thegdsks](https://clawhub.ai/user/thegdsks) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers building OpenClaw or Moltbot chat agents use this skill to add profanity detection, filtering, warning, blocking, logging, and custom moderation handling for platforms such as Discord, Slack, and Telegram. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic moderation actions such as message deletion, moderator notifications, logging, or bans can affect users unfairly if deployed without review rules. <br>
Mitigation: Define review, retention, redaction, notification, and appeal policies before enabling logging, deletion, notification, or ban workflows. <br>
Risk: The skill depends on an npm package and linked source repository that should be verified before installation. <br>
Mitigation: Confirm the npm package and linked repository are the intended ones, pin the dependency version, and deploy the bot with least-privilege moderation permissions. <br>


## Reference(s): <br>
- [OpenClaw Profanity Plugin on ClawHub](https://clawhub.ai/thegdsks/skills/openclaw-profanity) <br>
- [openclaw-profanity on npm](https://www.npmjs.com/package/openclaw-profanity) <br>
- [GitHub source package path](https://github.com/GLINCKER/glin-profanity/tree/release/packages/openclaw) <br>
- [Core library docs](https://www.typeweaver.com/docs/glin-profanity) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with bash and JavaScript code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes npm installation guidance, OpenClaw plugin configuration examples, moderation action choices, and platform-specific examples.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
