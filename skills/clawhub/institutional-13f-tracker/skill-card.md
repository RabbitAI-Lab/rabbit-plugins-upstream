## Description:

Tracks quarterly SEC 13F institutional holdings by ticker or manager, including top holders, quarter-over-quarter changes, aggregate flows, and activist positions through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and financial research agents use this skill to answer questions about institutional ownership, manager portfolios, 13F holdings changes, aggregate accumulation or distribution, and activist positions. Outputs are informational research context and should not be treated as personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SENTISENSE_API_KEY for authenticated read-only API requests.

Mitigation: Keep the key in the environment and do not expose it in prompts, URLs, logs, or user-facing output.

Risk: 13F data is quarterly, lagged, and not a real-time view of institutional positioning.

Mitigation: State the report date, explain the filing lag, and avoid presenting results as live market activity.

Risk: Financial research output can be mistaken for personalized investment advice.

Mitigation: Frame responses as informational context and avoid buy, sell, order-entry, or portfolio-management recommendations.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/institutional-13f-tracker)
- [SentiSense](https://sentisense.ai)
- [SentiSense App](https://app.sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples and financial research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY and returns read-only informational 13F research, not investment advice.]

## Skill Version(s):

1.1.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
