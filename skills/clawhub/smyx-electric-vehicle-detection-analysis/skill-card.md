## Description:

Analyzes video and images to detect electric bikes and motorcycles in restricted areas, count suspected parking or driving violations, and provide alerts and management guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security and facility teams use it to review video or images from parks, communities, campuses, parking areas, and restricted roads for suspected electric bike or motorcycle violations. It returns counts, violation levels, alerts, and management suggestions for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Video and image inputs are uploaded to a cloud analysis service; provider retention and account-isolation practices are not established by the supplied evidence.

Mitigation: Avoid sensitive footage until those practices are reviewed, and use only media you are authorized to share.

Risk: The supplied security guidance flags credential handling, automatic account registration and token storage, and an unresolved no-analysis option for review.

Mitigation: Do not use valuable credentials or rely on the no-analysis option until credential destination restrictions and that option are verified; isolate the workspace and avoid development HTTP endpoints.

Risk: Detection quality can depend on camera coverage and viewpoint, so automated counts may not establish that a violation occurred.

Mitigation: Have a person review the footage and report before taking enforcement or other consequential action.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-electric-vehicle-detection-analysis)
- [API documentation](references/api_doc.md)
- [Skill API specification](skills/smyx_analysis/references/api_doc.md)
- [Skill introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, JSON, Markdown]

**Output Format:** [Structured JSON or formatted text reports, including Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports can include detection counts, violation levels, alerts, and management suggestions; human review is recommended before acting on findings.]

## Skill Version(s):

9.9.21 (source: server-resolved release; artifact frontmatter lists 1.0.26)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
