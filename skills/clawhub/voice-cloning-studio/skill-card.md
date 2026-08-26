## Description:

Create a reusable personal or brand voice from a clean audio sample with this AI voice cloning studio and voice cloning software.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, brand teams, and developers use this skill to create an authorized reusable personal or brand voice from a clean single-speaker audio sample, then optionally request a short paid test reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill connects a Beatra account with broad media-generation and wallet-spend capability.

Mitigation: Install only when that account access is acceptable, confirm consent before upload or paid calls, and review returned billing facts after each task.

Risk: The bundled client silently checks for and installs package updates by default.

Mitigation: Use `python3 scripts/mcp_client.py update --auto off` when automatic replacement is not acceptable, and rely on the documented checksum and rollback controls for updates.

Risk: Voice cloning can misuse a third-party voice or overstate what a short proof reading demonstrates.

Mitigation: Require explicit authorization for third-party voices, stop before upload when authorization is missing, and report only the actual returned voice, task, usage, and billing facts.

## Reference(s):

- [AI Voice Cloning Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra skill page](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](references/consent-and-sample-readiness.md)
- [Clone execution and recovery](references/clone-and-proof-workflow.md)
- [Test-reading review and voice reuse](references/review-recovery-and-voice-reuse.md)
- [Installation and authentication](references/installation-and-auth.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Beatra task identifiers, voice identifiers, billing facts, and provider-returned links.]

## Skill Version(s):

0.1.8 (source: server evidence release.version and artifact manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
