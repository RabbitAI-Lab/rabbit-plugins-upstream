## Description:

Market Scout helps an agent turn business ideas or market observations into evidence-backed opportunity reports, validation plans, scoring, MVP guidance, and go-to-market actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kio831](https://clawhub.ai/user/kio831)

### License/Terms of Use:

MIT License

## Use Case:

External users and agent operators use this skill to research markets, validate demand and payment signals, score opportunities, decide whether to build or stop, and plan the first practical customer-acquisition steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Saved context can contain confidential business plans, customer notes, or validation results.

Mitigation: Do not place secrets or confidential business plans in saved context files, and review where saved context is stored or shared.

Risk: Market recommendations can be weak when web search is unavailable or evidence is incomplete.

Mitigation: Use web search when available, label assumptions and Unknowns, and validate key demand or payment claims with real-world evidence before building.

Risk: Developer package verification is only appropriate for trusted packages.

Mitigation: Run the ZIP verification tool only on packages from a trusted source and inspect package origin before execution.

## Reference(s):

- [Server-resolved source repository](https://github.com/kio831/market-scout)
- [ClawHub skill page](https://clawhub.ai/kio831/skills/market-scout)
- [V5 Orchestrator Architecture](orchestrator/architecture.md)
- [Routing Engine](orchestrator/routing.md)
- [Market Research Reference](references/market-research.md)
- [Evidence Chain Reference](references/evidence-chain.md)
- [Opportunity Scoring Reference](references/v3-scoring.md)
- [Validation Engine Reference](references/v4-validation.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown reports, cards, checklists, scoring tables, and validation plans]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include evidence labels, confidence, coverage, hard-gate notes, and explicit Unknown markers.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact documents Market Scout v5.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
