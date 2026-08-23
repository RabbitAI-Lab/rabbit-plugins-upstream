## Description:

Turn a brand name, industry, or reference image into a professional AI logo, brand mark, or app icon with multi-concept exploration, precise brand colors, and scalable composition.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to plan, generate, transform, refine, review, and deliver logo or brand-mark assets from a brand brief, visual references, or an accepted draft.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reuses a shared Beatra device credential for broad Beatra tool access.

Mitigation: Install only when that trust boundary is acceptable, keep the credential private, and use the documented disconnect flow when access should be revoked.

Risk: Reference images and brand assets may be uploaded to Beatra for remote processing.

Mitigation: Avoid confidential or regulated brand assets unless remote processing by Beatra is acceptable.

Risk: Approved generation requests consume Beatra credits and create asynchronous tasks.

Mitigation: Use the documented confirmation step, keep one stable client_request_id per logical request, and report the returned billing.net_charged_credits.

Risk: The skill silently checks for and installs updates by default.

Mitigation: Review the automatic update behavior before installation and disable auto-updates with the documented command when silent replacement is not acceptable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/beatra-ai/skills/ai-logo-maker)
- [Beatra Skill Homepage](https://beatra.ai/skills/ai-logo-maker)
- [Brand brief and routing](references/brand-brief-and-routing.md)
- [Logo craft](references/logo-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request objects, shell command snippets, task identifiers, billing fields, and artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload user-provided reference assets to Beatra and create paid asynchronous image generation tasks after user confirmation.]

## Skill Version(s):

0.1.4 (source: evidence.release.version and artifact/manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
