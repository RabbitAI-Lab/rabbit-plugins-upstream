## Description:

Analyzes images and video for signs of distress in children and provides reports and caregiver alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and childcare staff can use images or video to review possible signs of distress in children and consult historical analysis reports. Results are advisory and do not replace direct adult supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive images and video of children are sent to a cloud service.

Mitigation: Obtain appropriate consent and confirm the provider's retention, access-control, and report-sharing practices before use.

Risk: The skill can silently create or reuse an identity, making reports accessible without clear user control.

Mitigation: Use a dedicated account, avoid shared workspaces, and verify identity handling and token-storage practices.

Risk: Emotion assessments may be mistaken for a substitute for direct care.

Mitigation: Treat results as advisory; maintain adult supervision and respond to urgent situations in person.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis)
- [Child emotion analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; historical report lists as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a report link and optionally save results to a file.]

## Skill Version(s):

1.0.32 (source: server-resolved ClawHub release; skill frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
