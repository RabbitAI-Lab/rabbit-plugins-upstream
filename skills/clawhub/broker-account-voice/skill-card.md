## Description:

Turns written account-opening steps into one spoken voice clip per labeled cue, producing 8 to 20 brokerage onboarding audio files from steps the desk already supplied.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Brokerage onboarding teams use this skill to turn approved account-opening step lists into labeled voice clips for teller guidance, KYC steps, and related customer onboarding prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Beatra account powers and paid remote operations can spend credits or access media capabilities.

Mitigation: Review requested scopes before installation, show a cost card before paid clone or speech calls, use client_request_id idempotency, and check wallet or ledger data for balances and charges.

Risk: The Beatra Device Token is stored under ~/.beatra and may be shared across Beatra packages.

Mitigation: Keep credential files user-only, never expose tokens in chat, logs, command arguments, or diffs, and reauthorize only when needed.

Risk: Authorized voice samples may contain sensitive personal or biometric data.

Mitigation: Use only samples the user can authorize, inspect local samples before upload, upload through the bundled client, and do not treat file access as voice-clone consent.

Risk: Default silent package updates may change reviewed code before use.

Mitigation: Disable automatic updates before use when deterministic reviewed code is required; otherwise rely on the package updater's official-source and checksum verification.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/broker-account-voice)
- [Beatra skill homepage](https://beatra.ai/skills/broker-account-voice)
- [Account opening voice workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Tasks and results](references/tasks-and-results.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [MCP connection](references/mcp-connection.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, Guidance, Files]

**Output Format:** [Markdown guidance with JSON payloads, shell commands, and Beatra-generated MP3 audio task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Usually produces 8 to 20 labeled account-opening clips, one clip per cue, after user confirmation for paid clone or speech stages.]

## Skill Version(s):

0.1.2 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
