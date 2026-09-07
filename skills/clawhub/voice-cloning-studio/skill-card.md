## Description:

Create a reusable personal or brand voice from a clean audio sample, give the custom voice a memorable name, and optionally prepare a short paid test reading before using the voice for narration or brand content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creators use this skill to create an authorized reusable voice clone from a clean single-speaker sample, review live pricing before paid submission, and preserve the returned voice ID for later text-to-speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Voice cloning can misuse a person's voice or rely on samples the user is not authorized to clone.

Mitigation: Require explicit authorization before upload or paid cloning, and stop before submission when authorization is missing.

Risk: The skill grants broad Beatra account authority and stores a bearer credential under ~/.beatra.

Mitigation: Review the requested access before installing, keep credentials out of prompts, command arguments, logs, and chat, and use the documented disconnect or revocation flow when access is no longer needed.

Risk: Local audio is sent to Beatra and may create a reusable voice with retention, deletion, and billing implications.

Mitigation: Verify Beatra retention, deletion, and billing terms before creating a reusable voice, and report only returned billing and task facts.

Risk: Silent package updates are enabled by default and can replace package-owned executable files.

Mitigation: Review update behavior before use, consider disabling automatic updates with the documented control, and rely on the package's manifest and checksum verification when updates are allowed.

## Reference(s):

- [AI Voice Cloning Studio on ClawHub](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra Skill Homepage](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](references/consent-and-sample-readiness.md)
- [Clone execution and recovery](references/clone-and-proof-workflow.md)
- [Test-reading review and voice reuse](references/review-recovery-and-voice-reuse.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beatra task, billing, asset, and voice ID facts when the agent follows the workflow.]

## Skill Version(s):

0.2.0 (source: server evidence release.version and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
