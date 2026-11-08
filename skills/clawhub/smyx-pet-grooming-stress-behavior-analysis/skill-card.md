## Description:

Triggers when a user provides a pet grooming session video URL or file for analysis; supports local video uploads or network URLs to call server-side APIs for stress behavior recognition, detecting struggling, panting, tail tucking and other stress signals during grooming, outputting stress level grading to help groomers intervene promptly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet groomers, veterinary clinics, and pet care teams can use the skill to review grooming-session videos for observable stress signals and receive a graded behavior report. The report is for behavior observation and does not provide a medical diagnosis or behavior modification plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment flags automatic account registration and stored sign-in details for review.

Mitigation: Before installing, clarify remote account creation, credential protection, and deletion controls; use a separate identifier rather than repurposing an API secret.

Risk: The security assessment says the export-only option is broken, and footage retention practices are unconfirmed.

Mitigation: Require and confirm the export-only option before analysis, and confirm LifeEmergence's footage retention practices before sending video.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-pet-grooming-stress-behavior-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Guidance]

**Output Format:** [Structured behavior analysis report with stress-level grading, observations, risk prompts, and report links; JSON or Markdown/text presentation.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports summarize observable behavior signals during grooming and are not medical diagnoses or behavior modification plans.]

## Skill Version(s):

1.0.16 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
