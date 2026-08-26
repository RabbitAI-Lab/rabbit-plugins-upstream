## Description:

Turn a photo, a topic idea, or an accepted draft into a scroll-stopping REDnote (Xiaohongshu) cover and post image.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators and social media operators use this skill to turn a photo, topic idea, or accepted draft into a vertical 3:4 REDnote cover or post image with platform-appropriate composition and text-safe space.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra Device Token with permissions beyond image-cover generation.

Mitigation: Install only when broad Beatra access is acceptable, keep the token in ~/.beatra as documented, and revoke or disconnect the Beatra authorization when the skill is no longer needed.

Risk: Selected source images are uploaded to Beatra for transform and edit workflows.

Mitigation: Upload only images the user is comfortable sending to Beatra, avoid sensitive media, and disclose that upload makes the image bytes available to the remote tool.

Risk: Approved image generation consumes Beatra credits and transport uncertainty can otherwise lead to duplicate paid work.

Mitigation: Require one final approval before the paid call, use a stable client_request_id for recovery, and avoid resubmission unless the exact same request identity and arguments are being recovered.

Risk: The package sends limited package and platform registration metadata.

Mitigation: Tell users this registration occurs on first use and install only when that telemetry is acceptable.

Risk: Silent package updates are enabled by default.

Mitigation: Use the documented `python3 scripts/mcp_client.py update --auto off` command when review is required before code changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/rednote-cover-maker)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-cover-maker)
- [Cover routing](references/cover-routing.md)
- [Cover craft](references/cover-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON MCP arguments, task identifiers, billing fields, and generated image artifact links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill normally asks for one approval before a paid image operation, uses count=1 by default, and reports task and billing results after completion.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
