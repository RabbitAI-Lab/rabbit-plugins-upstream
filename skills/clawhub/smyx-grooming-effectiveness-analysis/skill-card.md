## Description:

Analyzes pet grooming images or videos to report visible matting, shed hair, grooming effectiveness, and an estimated hairball risk level.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and care providers use this skill to review grooming images or videos, assess visible coat condition and shed hair, and receive grooming guidance and estimated hairball risk. Results are care guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or supplied URLs are sent to a cloud service for analysis.

Mitigation: Use only media and URLs you are comfortable sharing with lifeemergence.com; avoid private media and internal URLs.

Risk: The skill automatically creates or reuses a backend identity and stores tokens locally.

Mitigation: Review the service and local workspace storage before installation; use only if you trust the provider with identity and token information.

Risk: Historical reports and estimated health-related risk may be mistaken for definitive findings.

Mitigation: Treat reports as grooming guidance rather than veterinary diagnosis, and consider whether cloud report history is appropriate for the media supplied.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-grooming-effectiveness-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text with report links; Markdown for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a local file; shed-hair estimates are visual approximations, not measurements or diagnoses.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release; bundled SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
