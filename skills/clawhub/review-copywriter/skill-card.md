## Description:

Organizes Amazon review evidence into complete Listing optimization directions and an evidence checklist for page copy planning; it does not perform freeform copy generation, ad operations, or automatic publishing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers and ecommerce operators use this skill to turn existing Amazon product-review language into evidence-based Listing copy optimization recommendations. The skill checks product data and quotes paid ARI operations before running analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid ARI credits may be consumed by collect or operations run commands.

Mitigation: Review the quote first and approve paid actions only after explicit confirmation.

Risk: The scanner reports that the skill can run broader paid ARI product-operation workflows than the fixed Listing-copywriting purpose promises.

Mitigation: Use only the documented listing/full workflow, avoid custom --workflow or --focus values, and review updates for hard-locking to listing/full.

Risk: The skill stores an ARI API key locally for future runs.

Mitigation: Use a key with appropriate account permissions, keep it secret, and rotate or remove the stored key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-copywriter)
- [Amazon review copywriting operation workflow](artifact/references/operation-workflow.md)
- [Amazon review copywriting API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command snippets and ARI operation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid collection or analysis should run only after quote review and explicit user confirmation.]

## Skill Version(s):

1.4.11 (source: server release metadata, _meta.json, scripts/ari.py, CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
