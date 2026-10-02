## Description:

Guides developers through monitoring X accounts with RSSHub and Miniflux, sending updates to Feishu groups, and preparing material for an agent-written daily report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jes614753-sketch](https://clawhub.ai/user/jes614753-sketch)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to deploy an X-to-Feishu RSS pipeline, configure Feishu messaging and daily-report triggers, and troubleshoot feed delivery or account authorization.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unauthenticated, publicly exposed relay can spoof Feishu posts and trigger daily reporting.

Mitigation: Keep the relay on a private network or require real webhook authentication; remove public exposure of port 7070 before deployment.

Risk: X login tokens and Feishu and Miniflux credentials can expose accounts or messages if shared.

Mitigation: Use a dedicated low-privilege X account, protect tokens as secrets, and do not share .env or feishu.env files.

Risk: The OAuth helper is not ready to rely on for safe user-token storage.

Mitigation: Fix the OAuth helper before using or storing Feishu user tokens.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/jes614753-sketch/skills/x-rss-feishu-daily)
- [Follow Builders optional feed source](https://github.com/zarazhangrui/follow-builders)

## Skill Output:

**Output Type(s):** [Guidance, Configuration instructions, Shell commands, Code]

**Output Format:** [Markdown with configuration and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes deployment, maintenance, and troubleshooting guidance for the bundled scripts.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
