## Description:

Organizes Amazon product fields and review evidence for a primary ASIN and authorized competitors into a comparable feature matrix, while flagging data gaps and experience differences.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon marketplace operators and analysts use this skill to compare a primary ASIN with authorized competitor ASINs and produce an evidence-backed feature matrix. It is intended for static feature comparison and gap review, not sales, inventory, advertising, order, or return-rate inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends ASINs, workflow parameters, account checks, credit balance checks, and ARI API key usage to the ARI service.

Mitigation: Install only if the user trusts the ARI service with this information and protect the local ARI API key configuration.

Risk: Paid collection or analysis actions can consume credits if the quoted operation is confirmed.

Mitigation: Review each quote and confirm only when the ASIN, site, requested workflow, and expected charge match the user's intent.

Risk: Security evidence flags broader billable remote workflow controls than the fixed feature-matrix description promises.

Mitigation: Use the documented fixed feature-matrix workflow and avoid custom workflow or focus values.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-features)
- [Operation Workflow](artifact/references/operation-workflow.md)
- [API Reference](artifact/references/reference.md)
- [ARI Service](https://ari.funewa.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown feature matrix with evidence notes, data-gap statements, and inline shell commands when setup or execution is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid actions.]

## Skill Version(s):

1.4.11 (source: server release evidence, artifact changelog, and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
