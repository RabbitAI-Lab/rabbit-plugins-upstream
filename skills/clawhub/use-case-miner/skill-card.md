## Description:

Extracts real user use cases, constraints, and experience evidence from Amazon reviews and product details; it requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn Amazon review and product-detail evidence into concise product use-case insights, constraints, and evidence-backed conclusions. It is intended for scenario insight, not demographic inference, advertising targeting, or unsupported marketing claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and uses an ARI API key and contacts the ARI service.

Mitigation: Configure the key only for trusted users and review access before installation or execution.

Risk: The skill can spend credits after confirmation, and security evidence notes that the packaged CLI can override the promised fixed workflow for chargeable product operations.

Mitigation: Run only the documented product/use_cases flow, require quote review and explicit confirmation before paid actions, and monitor credit usage.

Risk: Outputs may be misleading if review coverage is insufficient or if users ask for unsupported demographic, advertising, inventory, order, profit, or real-time store claims.

Mitigation: Limit conclusions to collected review and product-detail evidence, disclose gaps, and reject unsupported claims.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/funewa/skills/use-case-miner)
- [Amazon User Scenario Operation Workflow](references/operation-workflow.md)
- [Amazon User Scenario API Reference](references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown with concise findings, evidence notes, and inline shell commands when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results are based on collected review samples and should identify evidence gaps instead of filling missing data with unsupported conclusions.]

## Skill Version(s):

1.4.13 (source: server evidence, _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
