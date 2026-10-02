## Description:

Creates a named, reusable personal or brand voice from an authorized speech sample, with an optional separately approved test reading.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams create a reusable voice for authorized narration, courses, product stories, and brand content. They can review the estimated cost and optionally request a separately priced test reading.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The shared Beatra device token grants broader media-generation and spending-related authority than voice cloning alone.

Mitigation: Grant access only if that account-wide authority is acceptable; keep the token private and review pricing before approving paid work.

Risk: Automatic updates can replace installed package code without a separate confirmation.

Mitigation: Review the update behavior and disable automatic updates with the documented update --auto off command when version stability or administrator review is required.

Risk: Cloning a voice without the speaker's permission can enable impersonation.

Mitigation: Require the user's own voice or explicit speaker authorization before uploading a sample or requesting a clone.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/beatra-ai/skills/voice-cloning-studio)
- [Beatra skill homepage](https://beatra.ai/skills/voice-cloning-studio)
- [Consent and sample readiness](references/consent-and-sample-readiness.md)
- [Automatic updates and safety](references/automatic-updates-and-safety.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with inline commands and result links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include the returned voice ID, task status, usage, billing, and test-audio link.]

## Skill Version(s):

0.2.4 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
