## Description:

Compares recorded Amazon product-page price snapshots for a primary ASIN and authorized competitor pages, then explains relative price position, timing, and evidence gaps without claiming real-time prices or supporting automated repricing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to check Amazon competitor price positioning from previously collected product-page snapshots. It is intended for evidence-bounded comparison and gap reporting, not live pricing, sales, profit, inventory, order, or advertising decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI operations can spend credits and require an ARI API key.

Mitigation: Run profile and quote checks first, protect the ari_live_* key, and execute paid collection or analysis only after explicit user confirmation.

Risk: Security evidence reports a Review verdict because the paid operations CLI can override the documented fixed price-comparison workflow.

Mitigation: Review or hard-disable --workflow and --focus overrides for this specialized package; otherwise use only the documented page_compare/price workflow unless broader ARI product operations are intentional.

Risk: Price conclusions are based on recorded page snapshots, not live market data.

Mitigation: Report snapshot timing and evidence gaps clearly, and do not use the output for automatic repricing, sales, profit, inventory, order, or advertising-budget decisions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/competitor-price)
- [README](README.md)
- [Operation workflow reference](references/operation-workflow.md)
- [API reference](references/reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and service-response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis runs.]

## Skill Version(s):

1.4.11 (source: server release, artifact metadata, changelog, and script constant)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
