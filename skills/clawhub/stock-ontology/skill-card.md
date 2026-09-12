## Description:

Stock Ontology helps agents resolve companies, people, products, organizations, and topics around tickers, then compare SentiSense Score readings over a shared window using read-only SentiSense API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External agents and financial research workflows use this skill to resolve stock-related entity handles, compare SentiSense Score movement for supplied tickers or names, and present informational context without trading actions or advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the user's SentiSense API key to app.sentisense.ai and consumes the account's request quota.

Mitigation: Use a dedicated SentiSense key, monitor quota usage, and keep calls scoped to the user's requested ticker or entity.

Risk: Financial sentiment outputs could be mistaken for trading advice.

Mitigation: Present results as informational context only and preserve the skill's no-trading and no-buy-or-sell-recommendation posture.

Risk: Broad automated enumeration can create excessive API usage and unsupported coverage claims.

Mitigation: Use user-supplied tickers or names, avoid sweeping short-prefix searches, and report partial or unavailable coverage plainly.

## Reference(s):

- [SentiSense](https://sentisense.ai)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/stock-ontology)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables and concise prose with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only SentiSense API responses; no files, trades, purchases, or wallet operations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
