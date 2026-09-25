## Description:

Analyzes pet drying-box video for possible heat-stress signals and returns a risk assessment with safety recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, groomers, and veterinary staff can submit drying-box video to review possible heat-stress signals and decide whether to cool the enclosure or stop drying. They can also retrieve prior analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or video URLs are sent to external lifeemergence.com services for analysis.

Mitigation: Share only footage you are authorized to upload and review the service's data-handling terms before use.

Risk: The skill creates or reuses a cloud identity, stores API tokens in a local workspace database, and can retrieve reports associated with that identity.

Mitigation: Review identity and token storage before installation, restrict workspace access, and use report history only when authorized.

Risk: Heat-stress assessments may be mistaken for veterinary diagnosis or a replacement for supervising drying equipment.

Mitigation: Supervise the pet directly, stop drying and cool the enclosure when distress is suspected, and seek veterinary advice as needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-drying-box-heat-stress-analysis)
- [API documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured analysis report with a report link; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results may be saved to a user-specified file.]

## Skill Version(s):

1.0.11 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
