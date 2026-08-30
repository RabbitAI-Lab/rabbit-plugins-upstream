## Description:

Position size calculator for stocks and ETFs that creates a self-contained HTML calculator pre-filled with a SentiSense last price, 14-session average true range, and SentiSense Score, then reports share count, position value, percent deployed, dollar risk, and optional R multiple from the user's own account, entry, stop, and target inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thesentitrader](https://clawhub.ai/user/thesentitrader)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to generate a local, offline-rendering position size calculator for a selected stock or ETF. The calculator helps them inspect the arithmetic consequences of their own account size, risk percentage, entry, stop, and optional target without placing trades or making recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may mistake calculated position size for investment advice or a recommendation.

Mitigation: Present output as arithmetic on user-supplied inputs only; state that the skill does not choose securities, entries, stops, targets, or trade amounts.

Risk: A stop price may not be honored in real trading because of gaps, fast markets, slippage, or unplaced stops.

Mitigation: Explain that planned dollar risk is not a guaranteed loss cap and that costs, slippage, financing, tax, and execution quality are not modeled.

Risk: Changing the SentiSense endpoint can expose the API key or data flow to an untrusted service.

Mitigation: Use the default SentiSense endpoint unless the operator deliberately trusts the alternative endpoint.

Risk: The skill writes a local HTML file that may be mistaken for a live data surface after creation.

Mitigation: Make clear that market data is bound at build time, prices are delayed, and the finished artifact renders offline with no live calls at view time.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thesentitrader/skills/position-size-calculator)
- [SentiSense homepage](https://sentisense.ai)
- [SentiSense API key](https://app.sentisense.ai/get-api-key)
- [Publisher profile](https://clawhub.ai/user/thesentitrader)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell commands, JSON data, and a self-contained HTML file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SENTISENSE_API_KEY for build-time read-only data access; the rendered HTML artifact works offline after data is bound.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
