## Description:

Identifies enrolled acquaintances in images and videos through face comparison and provides recognition reports with locations and identities.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home and office users can compare faces in images or videos against an enrolled database, review recognition results, and retrieve historical reports. Recognition results are not suitable for legal identity verification.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face images, videos, or camera URLs are sent to the configured Lifeemergence service.

Mitigation: Obtain consent from people shown and review the service's retention and access policies before sending biometric media.

Risk: The skill can silently create or reuse an identity and persist login tokens and local database data.

Mitigation: Review identity and credential handling before installation and restrict access to locally stored data.

Risk: Submitting a private or internal camera URL can expose it to the remote service.

Mitigation: Avoid private or internal camera URLs unless their transmission and the service's access policies are explicitly approved.

## Reference(s):

- [Recognition API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured recognition reports or Markdown tables of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links or be saved to a local file.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; bundled frontmatter states 1.0.22)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
