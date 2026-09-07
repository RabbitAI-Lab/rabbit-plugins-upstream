## Description:

Create a Douyin shopping video, Douyin UGC ad, or AI creator product pitch from a product photo, product details, and an on-camera direction.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and commerce teams use this skill to plan and generate short vertical Douyin-style product videos from an inspectable product photo, merchant-approved claims, and a creator direction. It supports creator-style reviews, demonstrations, unboxings, product recommendations, and paid social creative.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags silent self-updates of executable skill files as a supply-chain risk.

Mitigation: Review the package before installing and use the documented update controls to turn automatic updates off when fixed code review is required.

Risk: The security review flags broad shared Beatra account permissions and a shared local account token as an account risk.

Mitigation: Review credential handling before installation, keep the local credential private, and disconnect or revoke access when the skill is no longer needed.

Risk: The skill uploads selected media to Beatra and sends device/platform registration metadata.

Mitigation: Use only media the user has approved for upload and avoid submitting sensitive or unlicensed product, creator, or campaign material.

## Reference(s):

- [Douyin UGC ad workflow](references/workflow.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and generated media task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides staged paid media generation and reports returned task, media, and billing details when available.]

## Skill Version(s):

0.1.8 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
