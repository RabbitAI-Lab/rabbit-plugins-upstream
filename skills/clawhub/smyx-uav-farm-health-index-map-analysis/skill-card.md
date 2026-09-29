## Description:

Analyzes agricultural UAV imagery to produce vegetation-index assessments, farm health maps, and reports identifying areas of possible crop stress.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, agricultural cooperatives, and UAV service providers use this skill to review aerial field imagery, locate areas of possible crop stress, and retrieve past analysis reports. Results support field inspection rather than replacing it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Farm imagery, videos, URLs, and identity-linked report queries are sent to external lifeemergence.com services.

Mitigation: Review the publisher and service terms, and obtain authorization before sending sensitive farm, location, or business data.

Risk: The skill may create or reuse a local user database that stores API tokens and links activity to cloud report history.

Mitigation: Use a controlled workspace, limit access to stored credentials, and review retained user and report data before deployment.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-uav-farm-health-index-map-analysis)
- [Farm health analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include vegetation-index assessments, affected-area details, and links to cloud reports.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; bundled SKILL.md states 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
