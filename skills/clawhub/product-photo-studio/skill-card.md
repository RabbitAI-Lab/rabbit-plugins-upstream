## Description:

Transforms a real product photo into studio-quality ecommerce listing, lifestyle, or marketplace hero images while preserving confirmed product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketers, and ecommerce operators use this skill to turn a source product photo into clean-background listings, lifestyle scenes, or refined product-image drafts through Beatra image tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared full-scope Beatra device token for upload, generation, model, and task operations.

Mitigation: Authorize only accounts intended for Beatra use, keep the credential file private, and revoke or rerun authorization when account access should change.

Risk: Product images are uploaded for remote Beatra processing.

Mitigation: Avoid confidential or unreleased product photos unless Beatra's account, retention, and data-handling terms meet the user's requirements.

Risk: Silent package updates are enabled by default.

Mitigation: Use the documented update command to turn automatic updates off when silent replacement is not acceptable, and rely on documented checksum and owned-file checks when updates remain enabled.

Risk: Billable generation requests can create duplicate work if recovery changes the inputs.

Mitigation: Freeze the prompt, references, canvas, model, count, and request ID before submission; retry only unchanged requests with the same request ID after uncertain delivery.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/product-photo-studio)
- [Beatra skill homepage](https://beatra.ai/skills/product-photo-studio)
- [Product routing](references/product-routing.md)
- [Scene craft](references/scene-craft.md)
- [Workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task IDs, artifact links, observed dimensions, and net charged credits after generation.]

## Skill Version(s):

0.1.6 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
