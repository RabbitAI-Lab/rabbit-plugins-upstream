## Description:

Generates JoinQuant backtest strategy code using a six-part strategy skeleton, cross-sectional multi-factor stock selection, time-series technical timing, and factor recommendation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenxyzcyxpp](https://clawhub.ai/user/chenxyzcyxpp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and quantitative strategy authors use this skill to draft JoinQuant-compatible Python backtest strategies, including multi-factor stock selection, technical timing, factor lookup guidance, and platform-specific API usage notes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated JoinQuant strategies include buy and sell order functions that could affect real funds if adapted for live trading without review.

Mitigation: Use generated code in backtest or simulation first, and review strategy logic, position sizing, and account mode before any live deployment.

Risk: JoinQuant documentation and factor library pages may not be directly accessible from automated tools, so generated API or factor guidance can need platform validation.

Mitigation: Validate generated code inside the JoinQuant platform and supplement with user-provided documentation or factor data when current platform behavior matters.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/chenxyzcyxpp/skills/joinquant-strategy-backtest)
- [JoinQuant factor library](https://www.joinquant.com/view/factorlib/list)
- [JoinQuant API help](https://www.joinquant.com/help/api/help)
- [JQData API documentation](https://www.joinquant.com/help/api/doc?name=JQDatadoc)
- [JoinQuant API access pitfalls](references/joinquant-api-access-pitfalls.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown with Python code blocks and concise implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated trading strategy code should be reviewed and tested in JoinQuant backtest or simulation before any live use.]

## Skill Version(s):

0.2.0 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
