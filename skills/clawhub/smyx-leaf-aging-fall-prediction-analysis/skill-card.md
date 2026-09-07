## Description:

Analyzes fixed-angle indoor houseplant leaf image sequences to detect aging signals and predict a 3-7 day leaf-fall risk window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, plant-care operators, and developers use this skill to analyze indoor plant photos or videos, monitor leaf aging, and receive structured reports with fall-risk windows and care suggestions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, and identity-linked report data may be sent to the publisher's cloud service.

Mitigation: Use only with data the user is comfortable sharing, and require clear documentation of remote destinations, retention behavior, and report access controls before deployment.

Risk: The authoritative security review flags silent identity handling, token storage, and insecure or overbroad network paths.

Mitigation: Review installation before use, remove development HTTP configuration, and require scoped token storage before approving the skill for managed environments.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Leaf Aging Fall Prediction API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with JSON-style structured analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes leaf aging indicators, predicted fall window, at-risk leaf identifiers, cause hints, care suggestions, and optional report export links.]

## Skill Version(s):

1.0.14 (source: evidence.release.version and target metadata; artifact SKILL.md frontmatter says 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
