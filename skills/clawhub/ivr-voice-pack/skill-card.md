## Description:

Creates a labeled set of phone-tree voice prompts in a consistent brand voice, including welcome, menu, hold, transfer, after-hours, and error messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Customer-service teams and hotline operators use this skill to plan and generate a consistent set of labeled audio prompts for an IVR phone tree.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared Beatra credential allows broader media and spending activity than IVR voice-pack creation alone.

Mitigation: Review the permissions before installation, authorize only an appropriate account, and keep local Beatra credentials private.

Risk: Automatic updates can replace package files without separate confirmation.

Mitigation: If unattended updates are unsuitable, turn them off using the documented update command and review updates before enabling them.

Risk: Voice synthesis and optional voice cloning incur charges; cloning also requires speaker permission.

Mitigation: Confirm the live cost estimate before paid generation and obtain explicit speaker consent before any cloning.

## Reference(s):

- [IVR Voice Pack on ClawHub](https://clawhub.ai/beatra-ai/skills/ivr-voice-pack)
- [IVR voice-pack workflow](references/workflow.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Audio files, Text]

**Output Format:** [Labeled MP3 clips with a text prompt ledger and clip details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per prompt, with slot ID, duration, MIME type, and billed credits.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
