## Description:

Prepare a concise referral handoff digest from a supplied referral form.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordinators use the skill to turn a supplied referral form into a concise handoff digest with the referral ID, specialty, urgency band, and requested window.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral forms may contain more personal data than the digest needs.

Mitigation: Limit supplied referral data to the fields needed for the digest.

Risk: Running local Python over referral data requires trusting the installed package.

Mitigation: Review the skill before executing it with real referral data.

## Reference(s):

- [Referral Handoff Reader on ClawHub](https://clawhub.ai/wxt-ai/skills/referral-handoff-packet-identifier)

## Skill Output:

**Output Type(s):** [Text]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The referral_digest object contains referral_id, specialty, urgency_band, and requested_window; no business artifact is persisted.]

## Skill Version(s):

1.1.0 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
