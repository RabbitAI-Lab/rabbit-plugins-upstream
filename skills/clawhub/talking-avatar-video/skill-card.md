## Description:

Creates a talking-avatar presenter video from one portrait plus an approved short script or speech track, with narration preparation, Beatra generation steps, and focused review of identity, clarity, lip sync, and motion stability.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agent operators use this skill to create AI spokesperson, presenter, training, course, onboarding, announcement, and product explainer videos from an authorized portrait and narration source. The workflow emphasizes consent, media compatibility checks, paid-stage approvals, task polling, and output review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow sends portraits, voice recordings, scripts, and generated outputs to Beatra.

Mitigation: Use the skill only when the user is comfortable sharing that media with Beatra and has confirmed rights and consent for the likeness and voice.

Risk: The skill stores a broad shared Beatra device token under ~/.beatra.

Mitigation: Review the authorization before installation and use the documented uninstall or disconnect workflow when the shared connection should be removed.

Risk: Package files silently self-update during normal use unless automatic updates are disabled.

Mitigation: Disable silent updates with the documented update --auto off command when automatic package replacement is not acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/talking-avatar-video)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/talking-avatar-video)
- [Beatra MCP endpoint](https://mcp.beatra.ai/mcp)
- [Narration-first presenter workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit Beatra MCP tool calls through bundled scripts and return generated audio/video artifacts, task status, usage, billing, and review notes when the host agent can inspect them.]

## Skill Version(s):

0.1.8 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
