## Description:

Turn user-supplied customer-service macro titles and talk tracks into a four-to-eight still CS macro card set.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams and agents use this skill to turn approved customer-service macro titles and talk tracks into a consistent pack of still service cards, with one image per named macro. It is intended for user-supplied scripts and avoids inventing missing policy language, refund rules, escalation steps, or notices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared full-scope Beatra device token that can spend credits, upload selected files, and store local state under ~/.beatra.

Mitigation: Install only when the Beatra service and account are trusted, protect the local Beatra state directory, and do not expose the device token in chat, logs, command arguments, or environment variables.

Risk: Silent automatic updates can replace package files after installation.

Mitigation: Disable automatic updates before use when reviewed code must remain fixed, and re-review package changes before re-enabling updates.

Risk: Billable image generation can consume credits, and unsafe retries can create duplicate work.

Mitigation: Confirm the live model price and every macro still before generation, keep one client_request_id per frozen request, and retry only identical uncertain requests.

Risk: Selected media uploads become available to Beatra and may contain sensitive material.

Mitigation: Upload only intended reference files, avoid sensitive customer data, and treat uploaded images as visual references rather than sources for missing policy or script text.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/cs-macro-card-set)
- [Beatra skill homepage](https://beatra.ai/skills/cs-macro-card-set)
- [CS macro card pack workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown guidance with inline shell commands and generated image artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one still per approved macro, reports task IDs, resolved models, dimensions, formats, and net charged credits when available.]

## Skill Version(s):

0.1.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
