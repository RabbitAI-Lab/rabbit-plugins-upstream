## Description:

Generates structured Markdown daily market recap reports from public akshare data for A-shares, Hong Kong, U.S., Asia-Pacific, European indices, northbound capital flow, sector boards, limit-up stocks, and Dragon-Tiger Board activity without API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tangbinbinm](https://clawhub.ai/user/tangbinbinm)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate factual daily global market review reports from public market data without account setup or API keys. It is intended for market data summarization, not trading recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Market recap output may be mistaken for investment advice.

Mitigation: Keep generated reports limited to factual market data and include the documented disclaimer that the output is not investment advice.

Risk: Broad market questions may activate the skill when a user only wanted a general discussion.

Mitigation: Use explicit prompts such as "生成A股复盘报告" when the user wants a generated market recap.

Risk: Public market data sources may be unavailable, incomplete, or delayed.

Mitigation: Report unavailable sections clearly and do not fabricate missing market values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tangbinbinm/skills/a-share-daily-review)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Structured Markdown report with supporting JSON data from a local Python script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python, akshare, pandas, and network access to public market data sources; output includes a disclaimer that it is not investment advice.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
