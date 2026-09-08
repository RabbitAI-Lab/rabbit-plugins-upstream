## Description:

Tracks Wall Street analyst coverage, price targets, upgrades, downgrades, analyst call history, Street-versus-crowd comparisons, and post-earnings rating moves through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and financial research agents use this skill to retrieve and interpret analyst ratings, price targets, rating changes, analyst call history, and related SentiSense sentiment for supported US equities. The skill is for informational research context and does not provide personalized investment advice or execute trades.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Financial outputs may be mistaken for personalized investment advice.

Mitigation: Present analyst ratings, targets, and sentiment as informational research context, avoid buy or sell recommendations, and state that the skill cannot trade or modify accounts.

Risk: Use of SENTISENSE_API_KEY can consume API quota or encourage a paid PRO tier.

Mitigation: Confirm the API key is intended for this use, monitor quota and rate limits, and disclose preview or PRO-only limits when results are truncated.

Risk: Free-tier preview limits can hide the full analyst book or call history.

Mitigation: Report preview status, denominators, and freshness fields from the API, and avoid conclusions that depend on omitted rows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/analyst-ratings-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense application and API host](https://app.sentisense.ai)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with REST endpoint examples, optional curl snippets, and concise financial research summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY; uses read-only HTTPS requests; free-tier preview limits and API quotas may affect completeness.]

## Skill Version(s):

1.1.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
