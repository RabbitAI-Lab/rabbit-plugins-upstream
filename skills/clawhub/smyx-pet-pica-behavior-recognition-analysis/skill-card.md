## Description:

Analyzes indoor pet videos for prolonged contact with hazardous non-food items and returns behavior alerts, risk information, and report links without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and home-monitoring operators use this skill to review indoor camera footage for potentially hazardous chewing or ingestion behavior and consult current or historical safety reports. Results are monitoring aids, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Indoor camera footage or video URLs are sent to the publisher's remote services and may reveal private home activity.

Mitigation: Request explicit confirmation before analysis; avoid private footage unless the publisher's privacy and retention terms are acceptable.

Risk: Analysis and history queries can create or reuse an internal account identity and persist authentication and history state locally.

Mitigation: Confirm before analysis or history queries, and restrict access to stored account and report data.

Risk: Behavior alerts may be mistaken for a veterinary diagnosis or a guarantee of safety.

Mitigation: Treat results as monitoring guidance, not a diagnosis; seek veterinary advice for suspected ingestion or injury.

## Reference(s):

- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-pet-pica-behavior-recognition-analysis)
- [Pet pica analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis results and Markdown report tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior warnings, risk levels, intervention suggestions, and report links]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
