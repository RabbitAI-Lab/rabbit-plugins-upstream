## Description:

Zhongcao Cover Maker helps an agent create or refine a vertical 3:4 REDnote (Xiaohongshu) cover from a photo, a confirmed topic, or an accepted draft, with optional paid Xiaohongshu lookup for research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to turn source photos, concrete content topics, or accepted drafts into Xiaohongshu-ready cover images. It can also guide optional Xiaohongshu lookup, paid image generation, result review, and recovery steps around Beatra tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release asks for a shared Beatra device token with spending and multiple media-generation scopes.

Mitigation: Install only when that access is acceptable, keep the token out of chat, logs, argv, and environment variables, and use the bundled authorization and uninstall flows to connect or revoke access.

Risk: The package silently checks for and installs updates during normal use by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when manual review is required before code changes.

Risk: Paid image generation and Xiaohongshu lookups can create duplicate charges if requests are retried with changed inputs.

Mitigation: Require explicit confirmation before each charged call, reuse the same client_request_id only for the identical logical request, and recover lost tasks with task lookup before resubmission.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/zhongcao-cover-maker)
- [Cover routing](references/cover-routing.md)
- [Cover craft](references/cover-craft.md)
- [Workflow](references/workflow.md)
- [Reading Xiaohongshu](references/note-lookup.md)
- [Review and recovery](references/review-and-recovery.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON request examples, task metadata, artifact links, and billing fields.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill normally guides one cover or lookup request at a time and reports task ID, observed dimensions, artifact links, and billing.net_charged_credits when available.]

## Skill Version(s):

0.1.7 (source: evidence.release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
