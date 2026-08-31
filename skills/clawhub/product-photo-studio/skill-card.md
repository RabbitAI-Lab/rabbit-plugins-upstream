## Description:

Transform a real product photo into a studio-quality ecommerce image, lifestyle scene, or marketplace-ready hero shot with clean backgrounds, professional lighting, and composition guided by confirmed product details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, ecommerce teams, and agent users use this skill to turn a source product photo into marketplace listing images, lifestyle scenes, and polished hero shots while preserving confirmed product details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects a Beatra account and stores a broad shared Device Token under ~/.beatra.

Mitigation: Review before installing, protect the local credential file, never expose the token in chat or logs, and revoke or disconnect access when it is no longer needed.

Risk: Product photos are uploaded to Beatra for remote image generation.

Mitigation: Use only approved product images, avoid sensitive content, and review generated images for product fidelity before publishing.

Risk: Paid image-generation calls consume credits and retries with changed inputs can create new billable work.

Mitigation: Freeze the prompt and parameters before confirmation, use one client_request_id per logical request, and recover uncertain submissions only with the same unchanged arguments.

Risk: The packaged client can silently self-update package-owned files unless automatic updates are disabled.

Mitigation: Rely on the documented source and checksum verification, or disable silent checks with scripts/mcp_client.py update --auto off when manual review is required before updates.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/product-photo-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/product-photo-studio)
- [Product routing](references/product-routing.md)
- [Scene craft](references/scene-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON, Files]

**Output Format:** [Markdown guidance with shell commands and JSON MCP tool arguments; delivered results include image artifact links, task IDs, dimensions, and billing details.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the source product photo as the visual anchor, confirms paid generation parameters before execution, and defaults to one generated image unless the user chooses otherwise.]

## Skill Version(s):

0.1.9 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
