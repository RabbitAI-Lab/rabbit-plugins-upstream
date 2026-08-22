## Description:

Crypto Sentiment Pulse provides local crypto Fear & Greed index and market sentiment guidance before an agent takes a position.

This skill is ready for commercial/non-commercial use.

## Publisher:

[northcap-group](https://clawhub.ai/user/northcap-group)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent builders use this skill to summarize crypto market mood as a Fear & Greed score and label before considering trading entries. It is informational guidance and should be paired with independent market checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is informational and the evidence does not provide a verifiable current crypto sentiment data source.

Mitigation: Use the output only as a market-mood signal and verify current sentiment data, prices, and trading assumptions independently before any financial decision.

Risk: The artifact describes buy-zone and correction-risk guidance that could be over-weighted in trading workflows.

Mitigation: Require human review and combine the signal with independent risk controls before using it in trading-related agent behavior.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown or plain text sentiment summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns a Fear & Greed score from 0 to 100 with a sentiment label.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
