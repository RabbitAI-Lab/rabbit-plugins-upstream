## Description: <br>
Send push notifications to your phone via Pushover (pushover.net). Use when you want reliable out-of-band alerts from OpenClaw: reminders, monitoring alerts, cron/heartbeat summaries, or 'notify me when X happens' workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[digitallyborn](https://clawhub.ai/user/digitallyborn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to send out-of-band Pushover notifications for reminders, monitoring alerts, cron summaries, and notify-me workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Notification contents and optional URLs are sent to Pushover. <br>
Mitigation: Avoid sending sensitive message text or URLs unless sharing that data with Pushover is acceptable. <br>
Risk: Pushover app tokens and user keys can be exposed if passed directly on shared command lines. <br>
Mitigation: Use environment variables or a secret store for credentials and avoid embedding real credentials in scripts, logs, or shell history. <br>
Risk: Automated alert workflows can create spam or disclose sensitive operational details. <br>
Mitigation: Review recurring alert rules before deployment and keep message text minimal for automated notifications. <br>


## Reference(s): <br>
- [Pushover API quick reference](references/pushover-api.md) <br>
- [Pushover API documentation](https://pushover.net/api) <br>
- [Create a Pushover application token](https://pushover.net/apps/build) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration] <br>
**Output Format:** [Markdown instructions with command-line examples; the bundled script returns compact JSON on successful sends.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Pushover app token and user key at runtime; emergency priority notifications require retry and expire values.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
