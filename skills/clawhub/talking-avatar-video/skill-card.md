## Description:

Create a talking avatar from one portrait and a short script or speech track. This AI presenter and digital human video workflow can prepare narration with a selected voice or use a supplied recording, then direct a stable talking-head clip with restrained expression, natural movement, clear delivery, and focused lip-sync review. Use it for AI spokesperson videos, product explainers, training, course lessons, announcements, onboarding, social talking-head content, and photo-to-talking-video messages, with narration-driven facial motion and a focused review of identity, clarity, lip sync, and motion stability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create a single talking-avatar presenter video from an authorized portrait and either an approved speech recording or a short script with a selected voice. It supports explainers, product messages, training clips, lessons, announcements, onboarding, and social talking-head content while guiding review of identity, speech clarity, lip sync, and motion stability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a broad shared Beatra device token for paid media-generation operations.

Mitigation: Install only when the publisher is trusted, review the Beatra approval page carefully, and avoid exposing the local credential in prompts, logs, command arguments, or environment variables.

Risk: Paid narration and video requests can spend account credits and may be duplicated if retried with changed request data.

Mitigation: Require explicit approval before each paid stage, keep a stable request identity for uncertain retries, and report final charges only from terminal task billing fields.

Risk: Silent automatic updates are enabled by default and can replace local package files.

Mitigation: Use the documented auto-update controls when ordinary use should avoid silent replacement, and rely on the package's checksum and manifest verification for accepted updates.

Risk: Talking-avatar generation can misuse a person's likeness or voice.

Mitigation: Confirm rights to the presenter likeness and narration voice before paid synthesis or animation, and stop before generation when authorization is missing.

## Reference(s):

- [ClawHub Skill Listing](https://clawhub.ai/beatra-ai/skills/talking-avatar-video)
- [Beatra Skill Homepage](https://beatra.ai/skills/talking-avatar-video)
- [Narration-first presenter workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Markdown, Files]

**Output Format:** [Markdown guidance with inline shell commands and returned Beatra task, artifact, usage, and billing details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated audio or video artifact links; paid generation details should be reported from terminal task responses.]

## Skill Version(s):

0.1.9 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
