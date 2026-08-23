## Description:

Analyzes newborn face images or short videos to return a visual jaundice risk hint and recommended next step for caregiver or clinical follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, healthcare staff, and product teams use the skill to submit newborn face images or short videos for visual jaundice pre-screening, receive low, medium, high, or inconclusive risk hints, and decide whether to observe, retake the image, or seek clinical bilirubin testing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive newborn images, videos, medical-risk results, and report history are routed through configured remote services.

Mitigation: Use only after confirming the backend is the intended production HTTPS service and that guardian consent, data retention, and access controls are handled outside the skill.

Risk: The skill silently creates or reuses identities and stores tokens or profile data locally.

Mitigation: Review whether local workspace token/profile storage is acceptable before deployment and clear or isolate the workspace data store when handling real infant health records.

Risk: Visual jaundice screening can be misleading because lighting, filters, occlusion, or skin-color artifacts can affect color analysis.

Mitigation: Treat outputs as pre-screening only, retake images in natural white light when quality is poor, and require professional bilirubin measurement for medium or high risk results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON structured report with risk level, confidence, observed visual features, recommended action, alert text, and optional report link.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save reports to a local file when an output path is provided and may list historical reports from the configured cloud API.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
