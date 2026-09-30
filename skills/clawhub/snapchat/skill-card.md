## Description:

Connects an agent to Snapchat advertising through Maton to review performance and manage ad accounts, campaigns, creatives, and audiences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Advertisers and marketing teams use this skill to review Snapchat ad performance and manage campaigns, targeting, creatives, and audiences with user-approved changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Maton grants access to Snapchat advertising data.

Mitigation: Confirm the intended access with the user and start with read-only operations.

Risk: Campaign, ad, and creative writes can change live advertising.

Mitigation: Get explicit approval for each change before submitting it.

Risk: Hosted functions, schedules, and trigger destinations may continue acting or forwarding data after setup.

Mitigation: Review and approve each automation and destination, including its data and persistence, before enabling it; remove it when no longer needed.

Risk: A raw API key can be exposed when the CLI is unavailable.

Mitigation: Prefer CLI authentication; use a raw key only when necessary and never log or persist it.

## Reference(s):

- [ClawHub Snapchat skill](https://clawhub.ai/byungkyu/skills/snapchat)
- [Maton homepage](https://maton.ai)
- [Snapchat Ads API introduction](https://developers.snap.com/api/marketing-api/Ads-API/introduction)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Text]

**Output Format:** [Markdown with command and API response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the user's authorized Snapchat connection; changes and automations require explicit approval.]

## Skill Version(s):

1.2.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
