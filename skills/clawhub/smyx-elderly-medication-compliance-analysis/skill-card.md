## Description:

Analyzes fixed-camera medication-area images or videos to detect pick-up, to-mouth, and swallow steps, judge medication compliance, and return structured results or report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, family members, and elderly-care operators use this skill to review medication-area footage for visual evidence that an elder picked up medication, brought it to the mouth, and swallowed. The result is an auxiliary compliance signal and should be manually verified before any health or care decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes private home medication videos through external services.

Mitigation: Install and use only with informed consent and acceptable privacy, retention, authorization, and deletion controls from the publisher.

Risk: The skill may retrieve historical health-related reports from the cloud.

Mitigation: Confirm that report access is authorized for the user and that cloud report retention and deletion practices meet the deployment's requirements.

Risk: The skill silently creates or reuses an identity and stores returned tokens locally.

Mitigation: Review local token storage before deployment and limit execution to environments where workspace data is protected.

Risk: Medication-compliance judgments can be incomplete or incorrect.

Mitigation: Treat outputs as auxiliary visual confirmation and manually verify incomplete or concerning results before care decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-medication-compliance-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration]

**Output Format:** [Markdown or JSON structured analysis report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detected medication steps, compliance status, missed step, confidence, event time, snapshot URL, alert text, and report links when returned by the service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
