## Description:

Builds a labeled set of phone-tree voice prompts in one consistent brand voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Call-center teams and developers use this skill to prepare and generate labeled welcome, menu, hold, transfer, after-hours, and error audio prompts for a phone tree.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Authorization grants Beatra a shared, persistent device token with broad access to media, tasks, artifacts, voices, and wallet operations.

Mitigation: Review the account's device authorization and revocation options before installing; revoke the device in the Beatra Console when access is no longer needed.

Risk: The bundled client can update package files automatically during normal use without separate confirmation.

Mitigation: Disable automatic updates with `python3 scripts/mcp_client.py update --auto off` if you need to review releases before installing them.

## Reference(s):

- [IVR Voice Pack release](https://clawhub.ai/beatra-ai/skills/ivr-voice-pack)
- [IVR voice-pack workflow](artifact/references/workflow.md)
- [Installation and authentication](artifact/references/installation-and-auth.md)
- [Automatic updates and safety](artifact/references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Audio files]

**Output Format:** [Labeled prompt ledger and MP3 clip links or artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes slot IDs, duration, MIME type, resolved model, and charged credits for each clip.]

## Skill Version(s):

0.1.8 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
