## Description:

US stocks analysis by an adversarial investment committee. Legendary-investor personas independently research a thesis, attack each other's cases against a shared evidence ledger (sentiment, smart money, SEC fundamentals), and reconcile into a verdict with recorded dissents. Structured rubrics keep every number sourced, on any model. Includes five quick data workflows. Use for stock research, investment thesis, bull case vs bear case, due diligence on a ticker, should I buy this stock, deep dive on a company. Read-only. No trading, no purchases, no write operations, no wallet access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to produce read-only US equity research, quick stock-data briefs, and structured bull-versus-bear investment thesis analysis. It is intended for informational stock research and due diligence, not trading execution or personalized investment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default workflow can run an external npm CLI locally.

Mitigation: Prefer the documented REST calls where possible, or run the CLI in a restricted environment with only SENTISENSE_API_KEY exposed.

Risk: The skill is for informational stock analysis and could be mistaken for personalized investment advice.

Mitigation: Keep outputs framed as educational research, preserve source citations and disclaimers, and require users to make their own investment decisions.

Risk: External financial-data calls can expose broader network or credential access if run without controls.

Mitigation: Limit filesystem access, avoid passing unrelated secrets, and restrict outbound access to the documented SentiSense, SEC EDGAR, FRED, and relevant issuer sources.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API Terms of Service](https://sentisense.ai/agreement/API-Terms-of-Service.pdf)
- [SentiSense Terms of Service](https://sentisense.ai/agreement/Terms-of-Service.pdf)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with sourced analysis, tables, checklists, and inline shell or REST examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only stock-analysis outputs may include external API calls through SentiSense, SEC EDGAR, and FRED, with required SENTISENSE_API_KEY authentication for SentiSense endpoints.]

## Skill Version(s):

2.7.1 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
