## Description:

Analyzes rehabilitation-session video for signs of frustration or disengagement and provides encouragement-oriented reports and progress feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Rehabilitation teams and home-care users can review training-session footage for possible frustration, interrupted exercise, and changes in progress, then receive encouragement suggestions and historical reports. This is not a medical diagnosis or a substitute for clinician judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive patient video and rehabilitation history are processed through cloud services.

Mitigation: Obtain explicit patient or guardian consent and confirm the publisher's data retention and deletion practices before use.

Risk: The skill may silently create or reuse a persistent patient identity when retrieving reports.

Mitigation: Confirm identity-binding and account/token handling practices with the publisher before home or clinical deployment.

## Reference(s):

- [Skill API documentation](references/api_doc.md)
- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-rehab-motivation-encouragement-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis text or JSON; Markdown table for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links, progress comparisons, and encouragement suggestions.]

## Skill Version(s):

1.0.12 (source: server-resolved release; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
