## Description:

Turn final manuscript or course text into ordered chapter audio with one narrator, a representative sample, clear pricing, and focused refinements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn final manuscript or course text into chaptered audiobook audio through Beatra voice selection, pilot review, paid synthesis, task recovery, and ordered delivery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device authorization.

Mitigation: Install only if you trust Beatra, keep the Device Token private, and revoke or disconnect the credential when access is no longer needed.

Risk: Automatic updates are enabled by default and can replace package-owned code silently.

Mitigation: Review the update behavior before routine use and disable automatic updates with the documented update command when automatic replacement is not acceptable.

Risk: Manuscripts, narrator samples, and uploaded files may be sent to Beatra-controlled workflows.

Mitigation: Upload only files intentionally meant for Beatra processing and avoid exposing sensitive prompts, credentials, or private input content in chat or logs.

Risk: Paid voice cloning, speech synthesis, and image generation can consume credits or duplicate work if retried incorrectly.

Mitigation: Require explicit current-card approval for each paid operation and replay a request identity only when the original outcome is genuinely uncertain and the arguments are unchanged.

## Reference(s):

- [AI Audiobook Narration on ClawHub](https://clawhub.ai/beatra-ai/skills/ai-audiobook-narration)
- [Beatra AI Audiobook Narration](https://beatra.ai/skills/ai-audiobook-narration)
- [Chapter production](references/chapter-production.md)
- [Performance, cost, and quality](references/performance-and-quality.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Delivery and recovery](references/delivery-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API Calls]

**Output Format:** [Markdown guidance with inline shell commands and JSON tool arguments]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task IDs, audio artifact links, billing facts, and recovery steps after approved paid operations.]

## Skill Version(s):

0.2.1 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
