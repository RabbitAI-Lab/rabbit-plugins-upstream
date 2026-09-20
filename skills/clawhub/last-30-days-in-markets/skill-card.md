## Description:

Produces an auditable 30-day US equity market recap from SentiSense market mood, story cluster, signal, summary, and earnings API data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and market research agents use this skill to generate a grounded monthly market brief, including market mood, high-impact story clusters, ticker and sector themes, current signals, and upcoming earnings. It is for research and education, with no trading, purchasing, write, wallet, or local file operations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Use requires providing a SentiSense API key and sending market-research requests to SentiSense over HTTPS.

Mitigation: Install only when the user is comfortable using the SentiSense service; use the key only for read-only data calls with no trading or write scope.

Risk: A full monthly brief can make multiple API calls and may consume quota or encounter rate limits.

Mitigation: Fetch only the required layers, page story data serially, honor rate-limit responses, and state any missing layers in the coverage line.

Risk: Generated market recaps can be mistaken for investment advice or overstate what the data supports.

Mitigation: Keep claims tied to fetched responses, include dates and coverage windows, preserve the research and education disclaimer, and avoid trading recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/last-30-days-in-markets)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key signup](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown research brief with dated coverage, API-derived figures, attribution, coverage notes, and disclaimer text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Every substantive market claim should trace to fetched SentiSense API responses; the skill does not perform trades, purchases, write operations, wallet access, persistence, or local file access.]

## Skill Version(s):

1.2.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
