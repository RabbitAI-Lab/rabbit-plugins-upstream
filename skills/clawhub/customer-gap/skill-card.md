## Description:

Compares Amazon product-page promises with collected customer review evidence to identify expectation gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to audit an Amazon listing by comparing product-detail claims against existing review samples. It returns evidence-based expectation-gap findings after checking service capability, quote details, and explicit user confirmation for paid work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI can run broader paid product-operation workflows than the fixed promise-audit purpose it advertises.

Mitigation: Use only the documented audit/promise flow, avoid custom workflow or focus values, and confirm quoted credit charges deliberately before running paid work.

Risk: The skill stores an ARI API key locally and sends authenticated requests to the ARI service.

Mitigation: Run setup or configuration only in trusted environments, protect local credentials, and rotate or revoke the ARI key if it may have been exposed.

Risk: Expectation-gap conclusions can be limited by collected review samples and do not cover legal compliance, Amazon policy compliance, or real-time price, sales, inventory, or advertising data.

Mitigation: Treat the output as review-evidence analysis, disclose data gaps, and use separate authoritative checks for compliance and real-time commercial data.

## Reference(s):

- [ClawHub customer-gap release page](https://clawhub.ai/funewa/skills/customer-gap)
- [Amazon Customer Expectation Gap API Reference](artifact/references/reference.md)
- [Amazon Customer Expectation Gap Operation Workflow](artifact/references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with concise evidence summaries and inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis should run only after quote review and explicit user confirmation.]

## Skill Version(s):

1.4.13 (source: server release metadata, _meta.json, scripts/ari.py, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
