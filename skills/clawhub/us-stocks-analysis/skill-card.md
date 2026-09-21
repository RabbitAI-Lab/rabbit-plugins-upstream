## Description:

US Stocks Analysis helps agents produce read-only U.S. equity research briefs and adversarial investment-committee analysis using SentiSense market, sentiment, smart-money, analyst, and fundamentals data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill to answer U.S. stock research questions, compare bull and bear cases, run ticker due diligence, and generate concise market-data briefs. The skill is informational and read-only, with no trading, purchase, wallet, file-write, or persistence behavior evidenced.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends stock-analysis requests to app.sentisense.ai using a SentiSense API key, which may consume API quota.

Mitigation: Use the required SENTISENSE_API_KEY only in the agent environment, monitor quota use, and avoid unnecessary repeated calls.

Risk: The SentiSense API key is a secret credential.

Mitigation: Keep the key out of chats, logs, committed files, and generated reports.

Risk: Outputs may be mistaken for personalized financial advice.

Mitigation: Present results as educational research and require users to make their own investment decisions.

## Reference(s):

- [SentiSense Website](https://sentisense.ai)
- [SentiSense API Reference](https://sentisense.ai/skill.md)
- [SentiSense API Key](https://app.sentisense.ai/get-api-key)
- [ClawHub Skill Page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [Publisher Profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown responses with optional inline shell commands and structured analysis tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces informational stock research only; not investment advice, trading instructions, or a solicitation to buy or sell securities.]

## Skill Version(s):

2.8.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
