## Description:

Turn a serialized web novel into chapter-by-chapter webnovel audiobook audio with one consistent narrator.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, publishers, and production agents use this skill to turn finalized serialized web novel chapters into narrated audio, keeping chapter order, pronunciation, billing, and narrator continuity clear across releases.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a shared Beatra device token with broad media, artifact, task, voice, and wallet capabilities.

Mitigation: Install only when the publisher and Beatra account boundary are trusted, keep the token in the private credential file, and disconnect or revoke access when the package is no longer needed.

Risk: Silent package updates are enabled by default.

Mitigation: Review the automatic-update behavior before installation and disable it with scripts/mcp_client.py update --auto off when change control is required.

Risk: Voice cloning can create consent and billing risk if started before authorization and cost checks are complete.

Mitigation: Require explicit speaker consent, present the live clone admission and cost estimate, and submit each paid request exactly once with a stable client_request_id.

## Reference(s):

- [Webnovel serial-audio workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Bundled MCP Client diagnostics](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON payload examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces chapter ledgers, Beatra tool-call payloads, polling and recovery steps, billing summaries, and labeled audio-delivery guidance.]

## Skill Version(s):

0.1.2 (source: server release evidence and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
