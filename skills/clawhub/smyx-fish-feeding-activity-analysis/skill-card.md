## Description:

Through built-in cameras of smart feeders or fixed cameras on aquariums, the system captures fish feeding videos after feeding, uses AI object detection and motion analysis to estimate fish gathering, feeding intensity, remaining feed, and a 0-100 feeding activity score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, aquarium operators, aquaculture teams, and developers use this skill to analyze post-feeding aquarium or feeder-camera media, generate structured feeding activity reports, and review cloud-stored report history. The skill supports appetite-decline alerts and next-feeding suggestions, but its outputs should be reviewed before operational action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends aquarium media and report-history queries to cloud services and stores account-related tokens or user identity data locally.

Mitigation: Install only after confirming the service account or open-id associated with reports, how local data and cloud reports can be deleted, and whether cloud processing is acceptable for the deployment.

Risk: Feeding analysis can produce misleading appetite or health-related guidance if media quality, feeding-window timing, water clarity, or fish species baseline is unsuitable.

Mitigation: Review results before acting, require clear post-feeding media, treat unreliable signals as a reason to re-record, and avoid using the output as a disease diagnosis or medication plan.

Risk: The artifact references possible feeder or companion-service actions that could affect animal care if enabled without approval.

Mitigation: Confirm that any feeder adjustment or related device action is disabled unless explicitly approved by the user or site operator.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-feeding-activity-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Markdown text containing structured JSON report content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding activity score, composite scene, alert level, recommended actions, next-feeding suggestion, disclaimer, and cloud report export URL.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
