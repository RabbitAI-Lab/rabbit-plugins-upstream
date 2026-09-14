## Description:

Amazon ASIN operations audit skill that uses product detail and review evidence to produce issues, supporting evidence, and operational priorities for a single ASIN.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External operators and agents use this skill to audit one Amazon ASIN, combining listing details and review evidence into prioritized operational guidance. It is not intended for advertising bidding, inventory planning, profit accounting, or order analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The scanner flags broader paid operation parameters than the advertised fixed single-ASIN audit scope.

Mitigation: Use the documented audit/full workflow and avoid undocumented --workflow, --focus, or --competitor arguments unless the broader operation is intentional and the credit cost is understood.

Risk: Collection and analysis can consume ARI credits after confirmation.

Mitigation: Run the quote step first, reuse the returned requestId, and proceed only after explicit user confirmation.

Risk: The skill stores and uses an ARI API key for authenticated service calls.

Mitigation: Authorize only through the documented setup/configure flow, keep the key private, and use the fixed official ARI endpoint.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/asin-audit)
- [Amazon ASIN operations workflow](references/operation-workflow.md)
- [Amazon ASIN audit API reference](references/reference.md)
- [ARI service endpoint](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown-style diagnostic guidance with quoted shell commands for setup, quote, status, and confirmed runs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid collection and analysis flows require a quote and explicit user confirmation before execution.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, artifact/_meta.json, artifact/scripts/ari.py, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
