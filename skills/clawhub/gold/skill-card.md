## Description:

Queries JisuAPI gold price endpoints for Shanghai, futures, Hong Kong, bank, London, jewelry-store, and historical gold market reference prices, with returned movement fields used as market-data commentary rather than investment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jisuapi](https://clawhub.ai/user/jisuapi)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer current and historical gold price questions across exchange, bank, London, Hong Kong, and retail jewelry-store sources. Agents can summarize returned prices, highs, lows, closing values, and movement fields while avoiding unsupported forecasts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a JisuAPI key and sends it to JisuAPI gold endpoints.

Mitigation: Use a key scoped to the needed API product where possible, store it in JISU_API_KEY, and avoid logging full request URLs or command output that could expose credentials.

Risk: Gold price and trend summaries may be mistaken for investment advice.

Mitigation: Treat outputs as market data commentary, cite returned timestamps and movement fields, and avoid forecasts or recommendations not present in the API response.

Risk: API errors, quota limits, expired keys, or unavailable records can return incomplete or error-shaped data.

Mitigation: Check for documented error responses before summarizing results and tell the user when data is unavailable or the request needs a valid key, permission, or narrower query.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/jisuapi/skills/gold)
- [JisuAPI](https://www.jisuapi.com/)
- [JisuAPI Gold Price API](https://www.jisuapi.com/api/gold/)
- [JisuAPI Gold endpoint](https://api.jisuapi.com/gold)

## Skill Output:

**Output Type(s):** [json, text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON returned by Python command-line calls, typically summarized by the agent as concise Markdown or text guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and a JISU_API_KEY environment variable; storegold accepts an optional date, and history requires market, startdate, enddate, and type.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
