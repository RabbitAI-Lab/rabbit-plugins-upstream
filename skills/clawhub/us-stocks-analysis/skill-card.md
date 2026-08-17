## Description:

US stocks analysis by an adversarial investment committee that combines quick market-data workflows with structured, evidence-led bull and bear debate for US equity research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to produce sourced US equity research briefs, thesis reviews, due diligence, and adversarial investment-committee verdicts. The skill is read-only and is intended for educational research rather than personalized financial advice or trading instructions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Outputs may be mistaken for personalized investment advice or trading instructions.

Mitigation: Present results as educational research, preserve the no-advice framing, and require users to make their own investment decisions.

Risk: The skill requires a SentiSense API key and outbound requests to market-data and public financial-data sources.

Mitigation: Provide the API key only through the SENTISENSE_API_KEY environment variable and allow outbound access only to the documented research sources needed for the workflow.

Risk: Financial conclusions can be misleading when required market, sentiment, SEC, or macro evidence is missing or stale.

Mitigation: Keep every numeric claim tied to an evidence ledger row, mark unavailable data explicitly, and lower confidence when decisive evidence is absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/us-stocks-analysis)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)
- [SentiSense website](https://sentisense.ai)
- [SentiSense API reference](https://sentisense.ai/skill.md)
- [SentiSense API key page](https://app.sentisense.ai/get-api-key)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, shell commands, guidance]

**Output Format:** [Markdown with cited evidence tables, concise briefs, verdict summaries, and optional curl examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for SentiSense endpoints; uses read-only market-data and public financial-data sources.]

## Skill Version(s):

2.5.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
