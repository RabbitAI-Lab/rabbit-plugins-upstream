## Description:

Product Page Audit reviews a single Amazon product page for gaps between listing claims, page assets, bullet points, and real buyer review signals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators, listing reviewers, and ecommerce teams use this skill to audit one Amazon product page and identify mismatches between page messaging and customer review evidence. It is not intended for two-ASIN competitor comparisons, ad bidding, or automatic page changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Server security evidence says the bundled CLI can run broader paid product-operation workflows than the single-page audit description promises.

Mitigation: Review the bundled CLI and command allowlist before installation, keep use to the documented audit/page workflow, and require the quote requestId plus explicit user confirmation before paid operations.

Risk: The skill stores and uses an ARI API key and makes network requests to the ARI service.

Mitigation: Configure it only with the intended account, treat the ARI key as a secret, and verify requests remain limited to the documented https://ari.funewa.com endpoint.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/product-page-audit)
- [Amazon Product Page Audit Operation Workflow](artifact/references/operation-workflow.md)
- [Amazon Product Page Audit API Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown audit summary with inline bash commands for setup, quote, run, and status checks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and explicit user confirmation before paid analysis or collection commands.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG.md, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
