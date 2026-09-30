## Description:

Helps agents query Google Ads campaigns, ad groups, keywords, and performance metrics with GAQL through Maton-managed account access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and marketing teams use this skill to inspect Google Ads performance and manage approved account actions, with optional user-approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorizing the wrong Google Ads account or making unintended changes through connected access.

Mitigation: Confirm the account before authorization, favor read-only queries, and obtain explicit approval for writes and new connections.

Risk: Hosted functions and triggers can continue acting on connected accounts or process events from other sources.

Mitigation: Approve each function, trigger, destination, and non-Google event source separately; remove automations when no longer needed.

## Reference(s):

- [Google Ads skill release](https://clawhub.ai/byungkyu/skills/google-ads-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Google Ads API overview](https://developers.google.com/google-ads/api/docs/start)
- [Google Ads query language reference](https://developers.google.com/google-ads/api/docs/query/overview)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with GAQL queries and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Account-scoped responses; writes and automations require user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
