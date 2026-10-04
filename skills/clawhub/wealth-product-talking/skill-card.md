## Description:

Creates short talking clips from advisor-supplied wealth product factsheets and authorized still images, with one clip per still.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Wealth advisors and educators use the skill to turn their supplied product factsheet points and authorized stills into short, separate narrated clips without adding unsupported product claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting Beatra grants a persistent authorization shared across Beatra skills.

Mitigation: Connect only if that shared access is acceptable; review the authorization before approving and disconnect when no longer needed.

Risk: Supplied product factsheets, stills, or voice samples may include sensitive or regulated material sent to Beatra.

Mitigation: Confirm Beatra is approved for the material and obtain likeness and voice rights before submitting it.

Risk: The bundled package installs verified updates automatically by default without separate confirmation.

Mitigation: Review this update behavior before installation and disable automatic updates with the documented update setting if required.

Risk: Generated wealth product clips may imply unsupported product claims or recommendations.

Mitigation: Check every spoken line against the supplied factsheet and review the final clips before use; do not invent yields, rankings, or buy recommendations.

Risk: Voice cloning, speech synthesis, and video creation consume credits.

Mitigation: Present the live price and seek separate approval for each paid stage before submitting requests.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/wealth-product-talking)
- [Beatra skill homepage](https://beatra.ai/skills/wealth-product-talking)
- [Factsheet talking-clip workflow](references/workflow.md)
- [Installation and authentication](references/installation-and-auth.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)
- [Billing, errors, and recovery](references/billing-errors-and-recovery.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Audio, Video clips]

**Output Format:** [Labeled slot list and separate narrated audio and video clips]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Typically 2–8 separate clips, 2–15 seconds each; no stitching. Reports available media details and net charged credits.]

## Skill Version(s):

0.1.8 (source: server-resolved release and manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
