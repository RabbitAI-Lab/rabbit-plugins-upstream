## Description:

Performs an Amazon ASIN operations audit by combining product-detail and review evidence into prioritized findings and recommended actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, sellers, and agents use this skill to audit a single Amazon ASIN, check product details and review evidence, obtain a quote, and produce an operations-focused diagnosis after explicit confirmation. It is not intended for advertising bidding, inventory, profit, or order accounting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime exposes broader paid operations workflow controls than the fixed ASIN audit purpose promises.

Mitigation: Use only the documented audit/full operations flow, review command arguments before execution, and require the quoted requestId plus explicit user confirmation before running paid actions.

Risk: The skill stores and uses an ARI API key and makes network calls to the ARI service.

Mitigation: Use the documented setup or configure flow, keep the key private, and stop if endpoint or redirect blocking errors occur instead of bypassing the official-domain checks.

## Reference(s):

- [Amazon ASIN Operations Workflow](artifact/references/operation-workflow.md)
- [Amazon ASIN Audit API Reference](artifact/references/reference.md)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-audit)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with inline shell commands and service responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid collection or analysis actions.]

## Skill Version(s):

1.4.13 (source: evidence.json release, artifact _meta.json, CHANGELOG.md, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
