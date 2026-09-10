## Description:

Turns a written credit-card benefits table into one labeled credit-rights voice clip per cue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Finance desk users and agents use this skill to turn prewritten credit-card benefits tables into labeled speech slots and generated voice clips. It supports live model and price checks, clone-consent handling, billing recovery, and task-result review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The package uses a broad shared Beatra bearer token for media, task, wallet, and account operations.

Mitigation: Review the grant before installing, keep the token only in the protected local credential file, and prefer a package-specific least-privilege credential in stricter environments.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Disable automatic updates before use in stricter environments, or rely on the documented fixed Beatra discovery/CDN paths and checksum verification when updates remain enabled.

Risk: Voice cloning can upload selected local voice samples and may create likeness-rights exposure.

Mitigation: Use cloned voices only after confirming rights and consent; inspect the sample first and upload only through the bundled client.

Risk: Paid clone or speech calls can consume credits, and unsafe retries may duplicate work.

Mitigation: Show the paid-stage card, submit each paid task once with an opaque request identity, and recover uncertain transport results only with the same unchanged request identity.

## Reference(s):

- [Credit Rights Voice Pack on ClawHub](https://clawhub.ai/beatra-ai/skills/credit-rights-voice)
- [Credit Rights Voice Pack Homepage](https://beatra.ai/skills/credit-rights-voice)
- [Credit rights voice workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Billing, errors, and recovery](artifact/references/billing-errors-and-recovery.md)
- [Tasks and results](artifact/references/tasks-and-results.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)
- [MCP connection](artifact/references/mcp-connection.md)
- [Uninstall and disconnect](artifact/references/uninstall-and-disconnect.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, JSON payloads, Guidance, Audio files]

**Output Format:** [Markdown guidance with shell commands, JSON MCP payloads, task results, and generated MP3 audio clips.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normally plans and produces 8 to 20 labeled clips, with one request identity per paid clone or speech task.]

## Skill Version(s):

0.1.2 (source: evidence release and artifact manifest)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
