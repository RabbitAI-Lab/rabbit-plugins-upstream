## Description:

Analyzes facial photos or videos to estimate one of nine TCM constitution types and provide a structured report with personalized wellness suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users use the skill to explore TCM constitution patterns from facial media, receive general wellness suggestions, and retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shared account handling can expose another user's health reports.

Mitigation: Use isolated accounts per user and verify report access controls before deployment.

Risk: Credential safeguards are inadequate, and HTTP debug logging can expose sensitive request data.

Mitigation: Use protected credential storage and disable HTTP debug logging.

Risk: Facial media retention and deletion terms for the provider are unconfirmed.

Mitigation: Confirm the provider's retention and deletion terms before uploading identifiable facial media.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-tcm-constitution-recognition-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance, Markdown]

**Output Format:** [Structured text and JSON reports, with Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes constitution estimates, scores, and general wellness suggestions.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
