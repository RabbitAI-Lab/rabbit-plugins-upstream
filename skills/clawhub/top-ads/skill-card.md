## Description:

Discover winning game and app ad creatives from Denote's weekly Trending, Rising, and New Ads charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[denote-developer](https://clawhub.ai/user/denote-developer)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and creative researchers use this skill to review weekly rankings of game and app ad creatives, find campaign inspiration, and inspect available details for a selected ad.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends DENOTE_API_KEY to the Denote API when retrieving rankings or creative details.

Mitigation: Keep the key in the agent host's secret settings and grant only the top_ads:read scope.

Risk: The security review notes unclear declared tool scope and incomplete evidence, so the benign verdict is not a guarantee of safety.

Mitigation: Review the skill's requested access and behavior before installation, especially its credential-to-network flow.

## Reference(s):

- [Denote Top Ads](https://denote.net/top-ads)
- [Top Ads on ClawHub](https://clawhub.ai/denote-developer/skills/top-ads)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown ranked lists with creative preview links and concise detail summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Weekly Trending, Rising, and New Ads charts with up to ten ranked creatives each; optional details for a selected creative.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
