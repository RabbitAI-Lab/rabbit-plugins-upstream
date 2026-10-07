## Description:

Prepare a referral handoff digest.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination staff use this skill to turn a supplied referral form into a concise handoff digest with a normalized urgency band.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral forms may contain sensitive personal information.

Mitigation: Supply only the fields needed for the digest and handle the input and output according to your privacy requirements.

Risk: The README contains an outdated note about output directories that could mislead operators.

Mitigation: Follow the current skill instructions for this digest-only operation instead of relying on the README note.

## Reference(s):

- [ClawHub release: Referral Handoff Reader](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referral_digest includes referral ID, specialty, urgency band, and requested window; no business artifact is saved.]

## Skill Version(s):

1.1.1 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
