## Description:

Poster Design Studio helps agents turn topic briefs, product or scene photos, brand references, or accepted drafts into event posters, promotional banners, flyers, and social graphics using Beatra image tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative operators use this skill to plan, confirm, generate, refine, and deliver one poster, flyer, banner, or social media graphic through Beatra image generation, transformation, and editing tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared local Beatra device token for MCP access.

Mitigation: Install only if that credential posture is acceptable, keep the token in the local credential file, and avoid exposing it in chat, logs, command arguments, environment variables, or other files.

Risk: Installed code silently checks for and applies package updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when manual change control is required; the bundled updater verifies discovery data, archives, file sizes, and SHA-256 checksums before replacement.

Risk: Poster generation can upload selected source images to Beatra and consume Beatra credits.

Mitigation: Confirm the final prompt, ordered references, canvas, model, count, and controls before any paid call, upload only intended source images, and use one stable `client_request_id` to avoid duplicate charges during recovery.

Risk: A failed connection, authorization problem, or slow task could otherwise lead to duplicate paid work.

Mitigation: Recover only the original task or retry the identical request with the same `client_request_id`; do not submit replacement work unless the user approves changed generation inputs.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/poster-design-studio)
- [Beatra skill homepage](https://beatra.ai/skills/poster-design-studio)
- [Poster routing](references/poster-routing.md)
- [Poster craft](references/poster-craft.md)
- [Workflow](references/workflow.md)
- [Review and recovery](references/review-and-recovery.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, JSON, API calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one planned Beatra image task at a time after explicit paid-call confirmation; delivered results include artifact links, observed dimensions, task ID, and net charged credits when returned by Beatra.]

## Skill Version(s):

0.1.2 (source: release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
