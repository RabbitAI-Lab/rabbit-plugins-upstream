## Description:

Analyzes pet carrier videos or video URLs through external Life Emergence services to estimate resting respiratory rate, flag rates above 40 breaths per minute, and return non-diagnostic monitoring guidance for pet air transport.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, pet transport staff, and agent operators use this skill to submit pet carrier video for respiratory-rate monitoring during air or long-distance transport. The skill is intended for health-risk awareness and alerting, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded videos, supplied URLs, and analysis requests are sent to external Life Emergence services for processing.

Mitigation: Install and run the skill only where external processing is acceptable, and avoid submitting sensitive or regulated media unless the service relationship has been reviewed.

Risk: The skill can silently create or reuse an internal user identity and store account tokens in a local SQLite database.

Mitigation: Run it in an isolated workspace, review local data storage policies, and clear or rotate stored identity and token state when the workspace changes hands.

Risk: History-list commands query cloud report history associated with the resolved internal identity.

Mitigation: Use history retrieval only when account-scoped cloud report lookup is intended, and validate that the resolved identity matches the expected user context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-carrier-respiratory-rate-analysis)
- [Pet carrier respiratory rate API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Life Emergence skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text with respiratory-rate analysis results, warnings, report links, or history records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include externally hosted report export links and cloud report-history records returned by the service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
