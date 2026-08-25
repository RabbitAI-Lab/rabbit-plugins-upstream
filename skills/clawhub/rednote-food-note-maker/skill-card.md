## Description:

Turns a dish photo, restaurant visit theme, or dining-atmosphere reference into a coordinated vertical 3:4 REDnote food note with a cover, supporting restaurant-story images, title ideas, caption beats, and tags.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, restaurant operators, and social content teams use this skill to plan and generate REDnote/Xiaohongshu food-post image sequences from a supplied dish photo, dining concept, or restaurant atmosphere reference. It also prepares the post angle, title ideas, caption beats, tags, and delivery details after paid Beatra generation completes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared Beatra device token with broad media/tool scopes and paid-service spending authority.

Mitigation: Install only when that access is acceptable, use a dedicated Beatra account or environment for stronger separation, and keep the token in the private credential file rather than chat, logs, arguments, or environment variables.

Risk: The bundled client silently updates package files by default.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` when change control is required, and use `python3 scripts/mcp_client.py update --check` for manual review.

Risk: Generation consumes Beatra credits and duplicate submissions can create extra paid work.

Mitigation: Require explicit confirmation before paid calls, preserve the approved request identity and returned task ID, and recover uncertain responses with task lookup before replaying any request.

## Reference(s):

- [ClawHub listing](https://clawhub.ai/beatra-ai/skills/rednote-food-note-maker)
- [Beatra skill homepage](https://beatra.ai/skills/rednote-food-note-maker)
- [Food-note planning](artifact/references/food-note-planning.md)
- [REDnote Food Note workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Image artifacts, Markdown, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown response with ordered image artifact links, slide roles, caption plan, tags, task details, and inline shell commands when setup or recovery is needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paid generation requires explicit user confirmation and may include Beatra task IDs, resolved model details, artifact dimensions, file formats, and net charged credits.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
