## Description:

Digest referral handoffs and build referral packet records.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Care coordination staff use this skill to prepare referral handoff digests from referral form data and create referral packet records for scheduling and routing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referral data can contain sensitive care coordination information.

Mitigation: Provide only referral data intended for agent processing and keep use limited to the prepare_referral_digest and create_referral_packet stages.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wxt-ai/skills/referral-coordination-desk)

## Skill Output:

**Output Type(s):** [text, structured data, guidance]

**Output Format:** [Text with structured object fields]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces either referral_digest or referral_packet_id for the requested stage; no credentials or private-file access are required.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
