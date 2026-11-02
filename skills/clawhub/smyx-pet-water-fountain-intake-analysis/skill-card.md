## Description:

Analyzes pet water fountain videos to estimate drinking frequency, session duration, and daily intake, compare results with historical baselines, and flag unusual changes for follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and operators of smart fountains can use the skill to review drinking behavior from fountain-area videos, track changes over time, and identify patterns that may warrant veterinary follow-up. Its estimates are for health monitoring and do not provide a diagnosis or treatment recommendation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only behavior may still upload selected videos or URLs to LifeEmergence.

Mitigation: Have that behavior corrected before relying on it. For analysis, submit only footage intended to be shared with the service.

Risk: Shared account credentials may associate reports or submitted media with another user's service identity.

Mitigation: Avoid shared workspaces containing other users' service identities, and clarify account isolation and data retention before submitting private recordings.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Sample](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis report with estimated drinking metrics, alerts, and report links; JSON or Markdown presentation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Intake is estimated from video behavior rather than directly measured; results are for reference and are not a veterinary diagnosis.]

## Skill Version(s):

1.0.13 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
