## Description:

Evidence-led pricing research for products, services, and other offerings. Use when someone needs to investigate a pricing decision, pricing structure, value metric, or customer evidence. Supports configurable business models, units, segments, and methods; outputs hypotheses and validation plans, not guaranteed prices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[c-kapsalis](https://clawhub.ai/user/c-kapsalis)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to scope evidence-led pricing research, compare suitable research methods, and prepare conditional pricing hypotheses and validation plans for a configured product or service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The crawler may reach private services.

Mitigation: Prefer supplied documents until crawler protections are fixed; otherwise enforce public-only network access externally and avoid browser mode.

Risk: External model prompts may contain personal or confidential study data.

Mitigation: Minimize sensitive data and inspect prompts before sending them to Anthropic.

Risk: Missing feature values or population weights can affect analysis results.

Mitigation: Check these inputs before relying on the results.

## Reference(s):

- [Intake and study design](artifact/references/1-intake.md)
- [Buyer research and simulated panels](artifact/references/5-panel.md)
- [Bayesian demand price elasticity](artifact/references/9-demand-elasticity.md)
- [Validation and handover](artifact/references/8-validation.md)
- [Output contract](artifact/references/output-contract.md)
- [Value Pricing on ClawHub](https://clawhub.ai/c-kapsalis/skills/value-pricing)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, JSON, CSV, Configuration]

**Output Format:** [Markdown reports, JSON and CSV analysis outputs, and study configuration files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Methods and outputs depend on the supplied evidence and configured study; conclusions are conditional hypotheses, not guaranteed prices.]

## Skill Version(s):

0.1.2 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
