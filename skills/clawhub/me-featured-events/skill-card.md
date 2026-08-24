## Description:

Configure and run ME Event activity subscriptions from api.me.news for browsing upcoming AI and Web3 events, filtering by region, and creating recurring event reminders.

This skill is ready for commercial/non-commercial use.

## Publisher:

[me-news](https://clawhub.ai/user/me-news)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to browse ME News AI and Web3 events, initialize filtered subscriptions, and receive daily or near-real-time event reminders through an agent-supported scheduler.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Recurring reminders could be sent to an unintended channel if subscription settings are not confirmed.

Mitigation: Confirm event filters, delivery channel, target, and schedule before creating or changing recurring reminders.

Risk: Channel credentials or gateway tokens could be exposed if stored with the skill or subscription state.

Mitigation: Keep channel credentials outside the skill directory and state file.

Risk: Incremental event delivery can duplicate notifications when delivery succeeds but the success feedback is not recorded.

Mitigation: Use a scheduler or wrapper that records explicit delivery success or failure with record-delivery.mjs after publishing non-empty poll output.

Risk: Failed API calls or invalid responses could otherwise cause missed events if local cursors are advanced.

Mitigation: Treat HTTP errors, invalid JSON, and non-200 API responses as failures and do not advance local cursor state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/me-news/skills/me-featured-events)
- [ME Featured Events API](references/api.md)
- [Agent compatibility](references/agent-compatibility.md)
- [ME Featured Events output format](format.md)
- [ME Featured Events sources](sources.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown and plain text event messages with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Non-empty stdout is delivered as event reminder text; local JSON state tracks filters, cursor, and pending delivery.]

## Skill Version(s):

1.1.0 (source: server release metadata and bundled script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
