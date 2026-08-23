## Description:

Turns verified SKU facts and product photos into a coordinated ecommerce image set with hero, feature, detail, lifestyle, size or fit, and packaging or in-box images for marketplaces and product pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Marketplace sellers, ecommerce teams, and agents supporting storefront operations use this skill to plan and generate a coherent image gallery for one verified SKU. It helps organize product facts, source photos, slot prompts, confirmations, task recovery, and delivery details for listing-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad media and account permissions and involves uploading product photos to Beatra.

Mitigation: Review the skill before installing and use it only when those permissions and uploads are acceptable for the product media involved.

Risk: Installed code can silently self-update by default.

Mitigation: Disable automatic updates when explicit review of code changes is required.

Risk: The Beatra credential is stored as a shared local token under ~/.beatra.

Mitigation: Protect the local credential files and disconnect or revoke access when the skill is no longer needed.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/ecommerce-listing-image-set)
- [Beatra skill homepage](https://beatra.ai/skills/ecommerce-listing-image-set)
- [Listing-set workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with command examples and JSON request payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce slot plans, confirmation summaries, task IDs, billing details, and ordered image artifact references when Beatra tasks complete.]

## Skill Version(s):

0.1.2 (source: ClawHub release evidence and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
