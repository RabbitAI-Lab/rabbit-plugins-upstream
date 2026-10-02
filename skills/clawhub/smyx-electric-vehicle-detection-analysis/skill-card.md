## Description:

Analyzes surveillance images and videos for e-bikes and electric motorcycles in restricted areas, reporting suspected violations and safety-management recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security teams and facility managers use the skill to review surveillance media for electric vehicles in restricted areas, assess potential parking or driving violations, and consult historical detection reports. Findings should be checked by a person before enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images or videos are sent to the configured lifeemergence.com cloud service.

Mitigation: Review the provider's retention practices and applicable privacy obligations before submitting monitored-area media.

Risk: The skill can silently create or reuse an identity, register or sign in remotely, and retain service tokens locally.

Mitigation: Obtain approval for account creation and protect the workspace data directory and SQLite database as sensitive.

Risk: Automated detection may be mistaken for a confirmed violation.

Mitigation: Have a person review footage and findings before taking enforcement action.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [Electric-vehicle detection API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [JSON detection reports or readable text; Markdown tables for historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes vehicle counts, violation levels, management recommendations, and optional report links.]

## Skill Version(s):

9.9.18 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
