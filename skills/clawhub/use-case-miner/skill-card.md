## Description:

Extracts real customer use cases, constraints, and experience evidence from Amazon reviews and product details; requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, product researchers, and operations teams use this skill to turn Amazon review evidence for a specific ASIN into practical user scenarios, constraints, and experience-backed conclusions. It is not intended for demographic inference, advertising targeting, or unsupported marketing claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled CLI can spend ARI credits after a quote and explicit confirmation.

Mitigation: Review the quoted cost and requestId before confirming; after an interruption, check status with the same requestId instead of rerunning a paid command.

Risk: The skill requires a locally stored ARI API key and contacts ari.funewa.com.

Mitigation: Use only the documented ARI authorization flow, keep the key private, and stop if endpoint or redirect blocking errors appear.

Risk: Security evidence says the CLI can be steered into broader paid ARI operations than the fixed use-case-mining scope describes.

Mitigation: Use the skill only for the documented Amazon use-case-mining workflow and avoid workflow or focus overrides unless broader ARI product-operations behavior is intended.

Risk: Review evidence may be insufficient for reliable product conclusions.

Mitigation: State evidence gaps plainly, keep conclusions tied to available review samples, and avoid demographic inference, advertising targeting, or unsupported marketing claims.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/funewa/skills/use-case-miner)
- [Amazon user scenario extraction README](artifact/README.md)
- [Dedicated operation workflow](artifact/references/operation-workflow.md)
- [ARI API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with review-evidence findings and inline shell commands when setup or ARI operations are needed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Paid ARI operations require quote review, requestId reuse, and explicit confirmation before credits are spent.]

## Skill Version(s):

1.4.11 (source: release evidence, _meta.json, CLI version, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
