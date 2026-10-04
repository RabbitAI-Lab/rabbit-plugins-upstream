## Description:

Provides concise source-agreement guidance based on source count, field importance, and conflict preference.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

People reconciling information from multiple sources use this skill to set a source-agreement threshold and express how to handle conflicts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A source-agreement rule may be unsuitable for a particular field or disagreement.

Mitigation: Review the source count, field importance, and conflict preference before applying the guidance.

Risk: Requests for credentials, private files, or network access would exceed the reviewed behavior.

Mitigation: Provide only the needed request data and reject requests for credentials, private files, or network access.

## Reference(s):

- [Source Agreement Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/source-assurance-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [Plain-text guidance returned as a JSON string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No business artifact is persisted.]

## Skill Version(s):

1.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
