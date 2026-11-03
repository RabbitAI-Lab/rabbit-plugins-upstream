## Description:

Analyzes tomato and strawberry images or videos to estimate fruit color, colored area, gloss, and relative size, then assigns a ripeness grade and harvest guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Fruit growers, greenhouse operators, and cooperatives use the skill to assess tomato or strawberry ripeness from images or videos and inform harvest timing. Results are visual estimates and commercial grading should be checked against the applicable standards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images or videos may be uploaded to LifeEmergence, while account creation, credential storage, and stored-data removal controls are unclear.

Mitigation: Before use, confirm the service and its data handling are acceptable, avoid sensitive images, and ask the publisher to clarify credential destinations and data removal.

Risk: The --export-env-only option does not prevent media uploads.

Mitigation: Do not treat this option as an offline or privacy mode; confirm media handling before relying on it.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fruit-ripeness-grading-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured ripeness analysis with per-fruit grades, observations, harvest guidance, and report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Visual estimates; results are for harvest decision support and do not provide post-harvest storage or preservation advice.]

## Skill Version(s):

1.0.12 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
