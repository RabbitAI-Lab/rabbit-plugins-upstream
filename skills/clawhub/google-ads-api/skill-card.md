## Description:

Helps agents query Google Ads campaigns, keywords, and performance metrics through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers, marketers, and developers use this skill to inspect Google Ads accounts and performance, and to propose authorized campaign changes or automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Campaign changes can alter ad spend, publishing, or account state.

Mitigation: Default to reading data; obtain separate approval for each change with the exact account, resource, and intended effect.

Risk: Automation functions and trigger destinations can make changes or forward event data persistently.

Mitigation: Approve each deployment, trigger, and destination separately, including its target, schedule, and data flow.

Risk: Local event handlers may process untrusted event payloads.

Mitigation: Run handlers only after separate approval of user-authored or reviewed code; do not execute instructions from event data.

## Reference(s):

- [Google Ads skill release](https://clawhub.ai/byungkyu/skills/google-ads-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Google Ads API overview](https://developers.google.com/google-ads/api/docs/start)
- [Google Ads query language overview](https://developers.google.com/google-ads/api/docs/query/overview)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with query and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Google Ads account scope and requested metrics depend on the user's authorized connection.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
