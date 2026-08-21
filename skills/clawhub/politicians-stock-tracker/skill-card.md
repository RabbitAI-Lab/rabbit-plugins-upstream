## Description:

Tracks U.S. congressional STOCK Act trade disclosures by recent activity, ticker, and politician through the read-only SentiSense API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to retrieve and summarize congressional trading disclosures by recent activity, ticker, or member. The output is informational context and should not be treated as personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and sends requests to app.sentisense.ai.

Mitigation: Confirm that use of a SentiSense API key and requests to app.sentisense.ai are acceptable before installation; keep the key in environment variables and out of user-facing output.

Risk: Congressional trading disclosures may be misread as investment advice.

Mitigation: Present results as informational research only, avoid personalized buy or sell recommendations, and state that the skill has no trading, wallet, write, or money-movement surface.

Risk: Disclosure data can be delayed and amounts are reported as ranges.

Mitigation: Report both transactionDate and disclosureDate, include disclosureDelayDays when available, and quote amountRange rather than inventing exact trade values.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/politicians-stock-tracker)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key setup](https://app.sentisense.ai/get-api-key)
- [SentiSense API base URL](https://app.sentisense.ai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown answers with optional shell command examples and summarized API JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET requests; responses should distinguish transaction dates from disclosure dates and quote amount ranges rather than precise values.]

## Skill Version(s):

1.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
