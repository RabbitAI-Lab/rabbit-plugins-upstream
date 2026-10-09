## Description:

Turns written replies to public TikTok comments into individual spoken audio clips for an operator to import.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Social media operators use the skill to plan spoken replies to public TikTok comments and create a separate audio clip for each reply they have written. It does not post replies to TikTok.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants a broad shared device token that can authorize account operations.

Mitigation: Connect only if this access is acceptable, protect the device credential, and revoke the device from the Beatra Console when finished.

Risk: TikTok comment and reply content, and optional voice samples, are sent to Beatra.

Mitigation: Review content before submission and use cloned voices only with the speaker's authorization and voice rights.

Risk: The generic remote tool caller can bypass local per-operation approval instructions and incur credit charges.

Mitigation: Require a fresh approval card with live pricing before each paid lookup, voice clone, or speech batch; check the Beatra wallet ledger afterward.

Risk: Automatic package updates are installed silently by default.

Mitigation: Disable automatic updates if changes must be reviewed before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/tiktok-comment-reply-voice)
- [Beatra skill homepage](https://beatra.ai/skills/tiktok-comment-reply-voice)
- [TikTok comment reply workflow](references/workflow.md)
- [Comment lookup](references/comment-lookup.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Markdown, Audio files]

**Output Format:** [Labeled reply list and individual MP3 speech clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [One clip per written reply; speech generation requires explicit approval and may consume credits.]

## Skill Version(s):

0.1.7 (source: server release metadata and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
