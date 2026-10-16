## Description:

Analyzes face photos or videos for nine traditional Chinese medicine constitution types and offers personalized wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and wellness practitioners use face photos or videos to request TCM constitution assessments, personalized lifestyle suggestions, and past report lists. Results are for wellness reference, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Face photos or videos and health-style report history are sent to the lifeemergence.com cloud service.

Mitigation: Obtain informed consent before use and review the service's data retention and deletion practices.

Risk: The skill may silently create or reuse a local identity and store authentication tokens in the workspace data directory.

Mitigation: Review account creation and token storage before installation; restrict access to the workspace data directory.

Risk: Constitution assessments may be mistaken for a medical diagnosis.

Mitigation: Present results as wellness guidance only and direct health concerns to a qualified clinician.

## Reference(s):

- [Skill listing on ClawHub](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can optionally be saved to a file.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
