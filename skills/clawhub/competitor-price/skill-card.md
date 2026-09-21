## Description:

Compares a main ASIN with authorized competitor product page price snapshots to explain relative price position, timestamp context, and evidence gaps; it does not claim real-time prices or support sales, profit, inventory, order, ad, or automated repricing decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and their agents use this skill to compare Amazon product page snapshot prices for a main ASIN and competitor ASINs. It helps summarize relative price position, data scope, evidence gaps, and the need for explicit confirmation before credit-consuming ARI collection or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and can make confirmed, credit-consuming ARI collection or analysis requests.

Mitigation: Configure only the intended ARI key, run profile and quote steps before execution, and approve a run only after reviewing the cost and scope.

Risk: Security evidence says the CLI can override the advertised fixed price workflow.

Mitigation: Keep usage to the documented page_compare/price workflow and do not approve runs that include unexpected workflow or focus values.

Risk: The analysis is based on stored product page snapshots and may not reflect current Amazon prices.

Mitigation: Present results as snapshot-based, include timestamp and evidence-gap context, and do not use the output for automated repricing or inventory, order, profit, ad, or sales decisions.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/funewa/skills/competitor-price)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [Amazon competitor price operation workflow](artifact/references/operation-workflow.md)
- [Amazon competitor price API reference](artifact/references/reference.md)
- [README](artifact/README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with inline shell commands and snapshot-based analysis summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before credit-consuming runs.]

## Skill Version(s):

1.4.13 (source: evidence release, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
