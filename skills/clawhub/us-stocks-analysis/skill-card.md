## Description:

US stocks analysis by an adversarial investment committee that researches investment theses with sourced evidence, quick data workflows, and read-only SentiSense market data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to brief US equities, compare bull and bear cases, run diligence on tickers, and structure evidence-grounded investment committee analysis. Outputs are informational research only and are not investment advice or trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SentiSense API key and bounded network calls for market research.

Mitigation: Install only where the agent is allowed to use that API key, and keep calls limited to the documented SentiSense, SEC EDGAR, and FRED sources.

Risk: Stock research output could be mistaken for personalized financial advice.

Mitigation: Treat outputs as informational research only, preserve the skill's no-advice framing, and require users to make their own investment decisions.

Risk: The documented CLI path uses npx to execute the sentisense package.

Mitigation: Use the pinned package version shown by the skill or call the documented HTTPS API directly when package execution is not acceptable.

## Reference(s):

- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense app](https://app.sentisense.ai)
- [SEC company tickers](https://www.sec.gov/files/company_tickers.json)
- [SEC XBRL company concepts](https://data.sec.gov/api/xbrl/companyconcept/CIK{10digits}/us-gaap/{Concept}.json)
- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown briefs and structured analysis with inline shell commands and API call guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only stock research output; requires SENTISENSE_API_KEY for SentiSense calls.]

## Skill Version(s):

2.6.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
