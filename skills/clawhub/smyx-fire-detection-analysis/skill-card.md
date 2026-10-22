## Description:

Analyzes images and videos for flames and smoke to support fire early warning in monitored locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security operators and developers use this skill to check local or linked camera images and videos for possible fire or smoke, review detection reports, and retrieve historical reports. Results support early warning and require professional confirmation before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or supplied URLs are sent to the configured LifeEmergence cloud service.

Mitigation: Use only approved media and explicit inputs; avoid sensitive camera footage unless its transfer is authorized.

Risk: The skill can silently create or reuse an identity and store authentication tokens in a local workspace database.

Mitigation: Review this behavior before installation and remove local workspace data and tokens when uninstalling or rotating access.

Risk: A detection report could be mistaken for a confirmed fire or an all-clear.

Mitigation: Treat results as preliminary alerts and have trained personnel confirm suspected incidents and follow emergency procedures.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [Fire detection API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis reports and Markdown historical-report lists; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, recommendations, and report links; results are advisory, not a substitute for emergency response.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
