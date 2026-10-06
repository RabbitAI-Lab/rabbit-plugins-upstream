## Description:

Helps agents decide when bounded public-source work needs independent help and prepare scoped assessment inputs for work-order previews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nigelon11](https://clawhub.ai/user/nigelon11)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can assess whether public, bounded technical claims or evidence-gathering tasks merit outside review, then prepare an approved, clearly scoped work-order assessment. Routine checks that can be completed locally stay local.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public web pages can contain misleading content or instructions aimed at the agent.

Mitigation: Use a sandboxed, low-privilege agent; screen public-source URLs and treat fetched content as evidence, not instructions.

Risk: A work-order assessment could expose task details if shared externally.

Mitigation: Use only public, non-sensitive inputs and obtain explicit owner approval before preparing material for external sharing.

Risk: A preview may be mistaken for a supplier offer or authorization to spend.

Mitigation: Keep quotes and availability unconfirmed and require a separate authorization and commissioning process; do not provide wallets or secrets.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/nigelon11/skills/verdikta-discover)
- [Service templates](references/service-templates.md)
- [Drafting a work order](references/drafting.md)
- [Preview contract](references/preview-format.md)
- [Public documentation reads](references/api-read-only.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [Brief decision and explanation with a JSON assessment input when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only planning; no purchase, supplier, price, or outcome is guaranteed.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
