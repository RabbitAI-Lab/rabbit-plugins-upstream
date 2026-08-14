## Description:

Analyzes fish feeding videos from smart feeder or aquarium cameras to estimate feeding activity, gathering behavior, feeding intensity, residual feed, alert level, and recommended next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and aquarium or aquaculture operators use this skill to analyze post-feeding camera footage, generate structured feeding activity reports, and review historical feeding reports. It supports appetite decline alerts and handling guidance without making disease diagnoses or medication recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium camera media and history requests are processed by the lifeemergence.com backend and may be linked to a silently created or reused local identity.

Mitigation: Install and run the skill only in workspaces where identity-linked cloud processing of this media and report history is acceptable.

Risk: Reusable tokens may be stored in a workspace SQLite database.

Mitigation: Use a workspace with appropriate access controls, and review or rotate local credentials according to the deployment owner's policy.

## Reference(s):

- [API Documentation](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and JSON reports from fish feeding activity analysis or historical report queries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include feeding activity score, key submetrics, alert level, recommended actions, next-feeding suggestion, disclaimer, and report links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
