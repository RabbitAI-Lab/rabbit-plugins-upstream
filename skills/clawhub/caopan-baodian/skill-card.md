## Description:

Provides Chinese-language educational guidance on the stock-trading framework from 《股票操盘宝典》, including market phase detection, stock selection, technical buy/sell points, risk and position management, and trading-system discipline.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvjin1983](https://clawhub.ai/user/lvjin1983)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to answer questions about 《股票操盘宝典》 and route China A-share trading education requests into market phase, stock selection, buy/sell point, risk management, and trading-system guidance. It should not be used for deterministic stock predictions, personalized buy/sell/hold recommendations, leveraged trading advice, or treating cycle numerology as reliable forecasting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can produce broad, actionable stock-trading guidance that readers may mistake for personalized financial advice.

Mitigation: Frame outputs as educational discussion of the book's framework and avoid personalized recommendations to buy, sell, hold, short, or add leverage to specific securities.

Risk: The skill may activate on broad stock-market questions beyond the intended book-specific and China A-share education scope.

Mitigation: Use tighter routing and disclaimers so broad market questions are narrowed to the book's methodology or declined when they ask for unsupported predictions or recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/lvjin1983/skills/caopan-baodian)
- [Publisher profile](https://clawhub.ai/user/lvjin1983)
- [Skill routing entrypoint](SKILL.md)
- [Whole-book overview](references/overview.md)
- [Capability index](references/capability-index.md)
- [Decision rules cheatsheet](references/cheatsheet.md)
- [Glossary](references/glossary.md)
- [Market phase detection](references/capabilities/market-phase-detection.md)
- [Stock selection](references/capabilities/stock-selection.md)
- [Buy and sell points](references/capabilities/buy-sell-points.md)
- [Risk and position management](references/capabilities/risk-position-management.md)
- [Trading system discipline](references/capabilities/trading-system.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language Markdown or plain text guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Educational trading-framework responses; no API calls, files, or shell commands are produced by the skill.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
