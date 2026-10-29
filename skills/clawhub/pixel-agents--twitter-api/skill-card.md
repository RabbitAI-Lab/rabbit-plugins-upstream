## Description:

Cookie-based Twitter/X automation toolkit (timeline, notifications, posting, follow ops) for OpenClaw agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pixel-agents](https://clawhub.ai/user/pixel-agents)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw agents use this toolkit to retrieve timeline and notification data, create summaries, and automate posting, following, and other Twitter/X account operations with session cookies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release bundles embedded login credentials and account-security and payment capabilities beyond its advertised social tasks.

Mitigation: Prefer a corrected release that removes embedded credentials and separates account administration and purchases from social automation; revoke any valid exposed credentials.

Risk: Session-cookie automation can take live actions on connected accounts, and the security guidance flags profile-update defaults, mention handling, and saved account data for review.

Mitigation: Use a dedicated account, protect session cookies, limit permitted actions and accounts, avoid the bundled live-posting demo, review profile-update defaults, verify mentions before responding, and manage saved account-data files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/pixel-agents/skills/twitter-api)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Text]

**Output Format:** [JSON data and Markdown or text summaries; may also publish Twitter/X posts or perform account actions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Content depends on the configured accounts and requested operation.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
