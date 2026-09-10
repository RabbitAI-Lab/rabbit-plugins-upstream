## Description:

Turns a written first-week checklist into 8 to 20 labeled voice clips for manager onboarding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External workplace teams and managers use this skill to convert an existing first-week checklist into labeled onboarding audio clips. It supports catalog voices or authorized staff voice cloning, with separate confirmation before billable clone or speech work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a shared bearer credential with broad media, wallet, task, artifact, and voice scopes.

Mitigation: Install only for an account where those Beatra scopes and spending access are acceptable, keep the credential in the documented local file, and never expose it in chat, logs, command arguments, or environment variables.

Risk: Billable clone and speech calls can spend Beatra credits.

Mitigation: Show the clone or speech confirmation card before each paid stage, use one opaque client_request_id per logical request, and do not retry changed work under the same request identity.

Risk: Automatic updates are enabled by default and can replace package-owned files without separate confirmation.

Mitigation: Use the documented update command to disable automatic checks when review-before-update is required.

Risk: Voice cloning can misuse staff likeness if file access is treated as consent.

Mitigation: Clone only when the user provides an authorized sample and explicit likeness or voice rights, and skip cloning when consent is missing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/beatra-ai/skills/new-manager-voice)
- [Publisher profile](https://clawhub.ai/user/beatra-ai)
- [Beatra skill homepage](https://beatra.ai/skills/new-manager-voice)
- [New manager week voice workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Installation registration](artifact/references/installation-registration.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with JSON payload examples and generated MP3 audio file references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces a labeled slot list before paid work, then 8 to 20 voice clip files after confirmed Beatra speech generation.]

## Skill Version(s):

0.1.2 (source: server release evidence and package manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
