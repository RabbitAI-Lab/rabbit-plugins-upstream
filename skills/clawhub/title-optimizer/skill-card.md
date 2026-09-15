## Description:

Provides Amazon title optimization recommendations from product-detail fields and review evidence, limited to title diagnosis and suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace operators and agents use this skill to check Amazon product fields and review evidence, quote any paid ARI analysis, and generate title-focused optimization guidance after explicit user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ARI API key and contacts ari.funewa.com for product data, quotes, and paid analysis.

Mitigation: Use a dedicated, revocable API key; store it only in the local user configuration or environment; revoke it if the key may have been exposed.

Risk: Confirmed operations can spend ARI credits.

Mitigation: Review the quote, requestId, product, site, and cost before adding --confirm; after interruptions, query status instead of rerunning a confirmed operation.

Risk: The security evidence notes paid operation overrides in this specialized title skill.

Mitigation: Use the built-in listing/title defaults and review commands for unexpected workflow or focus overrides before execution.

Risk: The security evidence notes a local API-key file creation weakness.

Mitigation: Keep the user configuration directory private and ensure the key file path is a trusted regular file; publisher-side hardening should block symlink-based key file writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/title-optimizer)
- [Publisher profile](https://clawhub.ai/user/funewa)
- [ARI API reference](references/reference.md)
- [Operation workflow](references/operation-workflow.md)
- [README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON command output with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the fixed listing/title workflow and ops_listing output template; paid operations require a quote and explicit confirmation.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
