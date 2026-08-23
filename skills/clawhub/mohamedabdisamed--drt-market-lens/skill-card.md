## Description:

DRT/ICT market analysis framework for 1h klines, premium/discount zones, and daily bias across indices, forex, metals, and crypto, designed for local analysis without network calls or API keys.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mohamedabdisamed](https://clawhub.ai/user/mohamedabdisamed)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent workflows can use this skill to frame local market-analysis tasks around DRT/ICT concepts, including bias, premium/discount zones, SMA trend filters, and dealing-range context. Trading outputs should be treated as informational only.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact does not include executable market-analysis code, so functionality may be limited unless a compatible local script or CSV workflow is supplied separately.

Mitigation: Confirm the local script and input data format before relying on the workflow, and test it with non-sensitive sample data first.

Risk: Market-analysis output may be incorrect or misleading if treated as trading advice.

Mitigation: Use the output as informational context only and keep human review outside the agent before making financial decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/mohamedabdisamed/skills/drt-market-lens)
- [Publisher profile](https://clawhub.ai/user/mohamedabdisamed)

## Skill Output:

**Output Type(s):** [guidance, analysis, shell commands, markdown]

**Output Format:** [Markdown guidance with inline shell command examples and tabular analysis descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires local market data and a compatible local CSV workflow or market_lens.py script supplied separately; does not execute trades.]

## Skill Version(s):

1.0.12 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
