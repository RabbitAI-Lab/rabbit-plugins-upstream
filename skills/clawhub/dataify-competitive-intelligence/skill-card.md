## Description:

Research and compare competitors, products, pricing, customer feedback, hiring signals, positioning, or a market landscape using current public evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Business users, product marketers, sales enablement teams, and analysts use this skill to turn competitive questions into sourced decision documents, including snapshots, product comparisons, pricing intelligence, review intelligence, market maps, and battlecards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataify requests may spend credits when collection actions succeed.

Mitigation: Use dry-run, checkpoints, mode limits, and max-actions before running larger or deeper research.

Risk: Research runs may store public-web evidence and intermediate reports locally.

Mitigation: Keep generated run directories in an appropriate workspace and review evidence before sharing reports.

Risk: Competitive conclusions can be misleading if evidence is stale, incomplete, or over-interpreted.

Mitigation: Cite material claims, label inferences and unknowns, preserve conflicting evidence, and run the included report verifier before delivery.

Risk: API credentials could be exposed if handled in chat or command arguments.

Mitigation: Keep the Dataify API token in the environment and verify only whether it is present.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dataify-server/skills/dataify-competitive-intelligence)
- [Data Source Routing](references/data-source-routing.md)
- [Evidence and Finding Contract](references/evidence-schema.md)
- [Analysis Frameworks](references/analysis-frameworks.md)
- [Output Templates](references/output-templates.md)
- [Delivery Verification](references/verification-checklist.md)
- [Scope and Cost Control](references/cost-control.md)
- [Failure Recovery](references/failure-recovery.md)
- [Incremental Monitoring](references/monitoring.md)
- [Competitive Battlecard](references/modules/battlecard.md)
- [Competitor Snapshot](references/modules/snapshot.md)
- [Product Comparison](references/modules/product-comparison.md)
- [Pricing Intelligence](references/modules/pricing-intelligence.md)
- [Review Intelligence](references/modules/review-intelligence.md)
- [Hiring Signals](references/modules/hiring-signals.md)
- [Market Landscape](references/modules/market-landscape.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, CSV, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown, JSON, CSV, and shell commands for bounded research runs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local run directories containing state, raw evidence, evidence JSON, and draft reports when helper scripts are used.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
