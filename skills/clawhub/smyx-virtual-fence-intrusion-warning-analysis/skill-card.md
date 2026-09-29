## Description:

Analyzes infant-monitoring videos for crossings of defined safety zones and provides warning reports and historical report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Caregivers and other users can submit infant-monitoring footage or a video URL to check for virtual-fence crossings and review warning reports or report history. Results are supplementary safety information, not a substitute for direct supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant and home footage or video URLs may be sent to cloud services and retained in report history without clear consent or retention terms.

Mitigation: Obtain informed consent before submitting footage; verify service endpoints and retention and deletion terms before use.

Risk: The skill can silently create or reuse a linked account and store authentication tokens locally.

Mitigation: Review account linkage and local token storage, and restrict access to the workspace and cloud account.

Risk: Missed or incorrect warnings could leave an infant exposed to danger.

Mitigation: Keep direct adult supervision and physical safety protections in place; treat reports as supplemental alerts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-virtual-fence-intrusion-warning-analysis)
- [API interface reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured warning report or historical report list, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save a report to a user-specified file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
