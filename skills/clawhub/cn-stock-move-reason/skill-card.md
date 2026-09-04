## Description:

Analyzes why a single A-share stock moved sharply using public quote, announcement, Eastmoney Guba/news, sector, breadth, and emotion-cycle evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tsetsugekka](https://clawhub.ai/user/tsetsugekka)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to investigate sharp moves in one A-share stock at a time, separating confirmed catalysts from market imagination and placing the move in stock, sector, broad-market, and emotion-cycle context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs public-market web requests and a local Python collector.

Mitigation: Install and run it only where public-market data collection is acceptable, and review collected evidence before relying on the analysis.

Risk: The skill can persist reusable learning changes to local skill files.

Mitigation: Require explicit user confirmation before writing experience or reference updates.

Risk: The skill can coordinate with optional private RAG, self-selected-stock, or simulated-account integrations.

Mitigation: Enable private or account-related integrations only when the user specifically intends to use those data sources.

## Reference(s):

- [Server-resolved source provenance](https://github.com/tsetsugekka/codex-market-skills/tree/main/skills/cn-stock-move-reason)
- [ClawHub skill release page](https://clawhub.ai/tsetsugekka/skills/cn-stock-move-reason)
- [CN Stock Analysis Experience](references/experience.md)
- [Eastmoney](https://www.eastmoney.com/)
- [Eastmoney Guba Topics](https://gubatopic.eastmoney.com/)
- [Eastmoney Quote API](https://push2delay.eastmoney.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One-stock analysis output, usually in Chinese, with catalyst ranking, market/sector resonance, emotion-cycle position, confidence, and caveats.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
