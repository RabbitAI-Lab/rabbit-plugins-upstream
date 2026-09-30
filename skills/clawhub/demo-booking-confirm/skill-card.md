## Description:

Creates labeled booking confirmation, rescheduling, and cancellation voice lines and generates one audio clip per approved notice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Shop staff and sellers use this skill to prepare labeled booking notices from confirmed facts and generate a consistent voice clip for each approved notice, with an optional authorized voice clone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared device credential grants broad access beyond booking audio and persists between sessions.

Mitigation: Connect only if you trust Beatra with account-level media and tool access; protect and revoke the credential when no longer needed.

Risk: Voice cloning and speech requests may incur charges.

Mitigation: Check current prices and explicitly approve each paid stage and its request count before submission.

Risk: Silent automatic package updates are enabled by default.

Mitigation: Disable automatic updates if you need to review new versions before installing them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/beatra-ai/skills/demo-booking-confirm)
- [Booking confirmation workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Audio clips, Guidance]

**Output Format:** [Labeled text slot list and generated audio artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 8–20 clips; voice cloning and speech generation require separate approval and may consume credits.]

## Skill Version(s):

0.1.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
