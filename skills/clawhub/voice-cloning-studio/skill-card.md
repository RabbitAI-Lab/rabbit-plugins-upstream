## Description:

Create a reusable personal or brand voice from a clean audio sample with this AI voice cloning studio and voice cloning software.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to create an authorized reusable personal or brand voice from a clean single-speaker sample, then optionally run a separately approved short test reading. It guides consent checks, sample readiness, pricing review, task submission, recovery, billing reporting, and reuse of the returned voice identifier.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Beatra account authorization and stores a broad bearer token under ~/.beatra.

Mitigation: Install only in environments where local credential storage is acceptable, keep the credentials file private, and use the documented disconnect or uninstall workflow when access is no longer needed.

Risk: Authorized voice samples may be uploaded to Beatra for clone creation.

Mitigation: Confirm the speaker's authorization before upload, avoid unnecessary sensitive sample details, and stop before any paid call when consent is missing.

Risk: The skill sends installation registration telemetry and silently self-updates package code by default.

Mitigation: Review the security guidance before deployment and disable automatic updates with the documented update command in sensitive environments.

Risk: Voice cloning and optional test readings can incur paid Beatra charges.

Mitigation: Require a current price card and explicit user balance or top-up confirmation before each billable operation, then report returned billing facts rather than estimates as final.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra skill homepage](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](references/consent-and-sample-readiness.md)
- [Clone execution and recovery](references/clone-and-proof-workflow.md)
- [Test-reading review and voice reuse](references/review-recovery-and-voice-reuse.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference paid Beatra voice clone and speech synthesis tasks, returned task facts, billing fields, artifact identifiers, and voice identifiers.]

## Skill Version(s):

0.1.9 (source: server release evidence and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
