## Description:

Analyzes feeding and post-feeding enclosure video to record reptile prey attacks, swallowing, feeding refusal, and regurgitation events.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and breeders use feeding videos to document prey attacks, swallowing, refusal, and regurgitation and to flag events for follow-up. The output records visible behavior and does not diagnose illness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos are sent to the configured LifeEmergence service, and its retention and deletion terms are unverified.

Mitigation: Confirm retention and deletion terms before sending private footage.

Risk: The no-analysis option is reported ineffective, and API-key reuse, remote enrollment, and stored-token controls need clarification.

Mitigation: Request fixes and clear enrollment and token controls before use; review the skill before installing.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release](https://clawhub.ai/18072937735/skills/smyx-reptile-feeding-refusal-vomiting-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance, Report links]

**Output Format:** [Structured JSON or Markdown analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Behavior observations and alerts based on supplied video; not a veterinary diagnosis.]

## Skill Version(s):

1.0.14 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
