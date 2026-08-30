## Description:

Turn written game UI lines into one game voiceover clip per labeled cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External game studios and developers use this skill to convert already-written game UI copy into 8 to 20 labeled voiceover audio cues for buttons, wins, failures, and similar interface events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package requests broad Beatra device authorization, including media generation, voice, wallet spend, task, and artifact scopes.

Mitigation: Install only in environments where those scopes are acceptable, keep the local Beatra credential private, and avoid shared account credentials.

Risk: The bundled client performs silent package update checks by default.

Mitigation: Review the documented update behavior and disable automatic updates with the provided command when silent updates are not acceptable.

Risk: Paid speech or clone requests can be duplicated if transport failures are retried with changed arguments or new identities.

Mitigation: Use one opaque client_request_id per paid request, retry only byte-identical arguments, and verify task status before resubmitting.

Risk: Voice cloning can misuse a sample when likeness and voice rights are not established.

Mitigation: Require explicit voice rights, inspect the authorized sample, and do not treat file access as consent.

## Reference(s):

- [Game UI voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Installation registration](references/installation-registration.md)
- [Tasks and results](references/tasks-and-results.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [MCP connection](references/mcp-connection.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Files]

**Output Format:** [Markdown with labeled cue lists, JSON payload examples, shell commands, and audio task or file references]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates 8 to 20 labeled MP3 game UI voice clips through Beatra speech tools; cloned voice use requires explicit consent.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
