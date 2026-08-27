## Description:

Turn a written first-week checklist into one new manager week voice clip per labeled cue. This first week voice pack studio records each new manager voice and first week checklist audio from the list the office already wrote, then delivers 8 to 20 new manager week clip files. Use it for manager onboarding voice packs that keep one cue on each clip.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users use this skill to turn an existing first-week manager checklist into a labeled set of onboarding voice clips. It helps plan, authorize, generate, review, and recover Beatra text-to-speech and optional voice-clone tasks while keeping one checklist cue per clip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses broad Beatra account authorization with local credential persistence.

Mitigation: Review the requested Beatra authorization scopes before use and protect the local credential files as sensitive account material.

Risk: The skill can spend wallet-backed credits for speech and voice-clone generation.

Mitigation: Use the documented approval cards, current live pricing, and one opaque client_request_id per paid request before submitting generation.

Risk: The skill can upload clone samples and generate cloned voices.

Mitigation: Use only authorized samples, treat file access as insufficient for consent, and keep a cloned voice_id frozen only after the clone task succeeds.

Risk: The bundled client silently checks for and installs package updates.

Mitigation: Consider disabling automatic updates before use and rely on the documented package verification and rollback controls when updates are enabled.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/new-manager-voice)
- [Beatra skill homepage](https://beatra.ai/skills/new-manager-voice)
- [New manager week voice workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON payload examples and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list and instructions for Beatra speech or clone tasks; generated audio artifacts are returned by the Beatra service.]

## Skill Version(s):

0.1.1 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
