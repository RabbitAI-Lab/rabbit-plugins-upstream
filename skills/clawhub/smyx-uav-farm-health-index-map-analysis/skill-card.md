## Description:

Submits UAV imagery or video for farm-health analysis and returns structured reports, report links, or cloud report history.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Farm managers and agricultural analysts use the skill to request UAV-based crop-health assessments and review past reports. Validate any indicated problem areas in the field before making operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs are sent to lifeemergence.com services and cloud report history may be retrieved automatically.

Mitigation: Review data-sharing requirements and obtain approval before submitting imagery or retrieving reports.

Risk: The skill may silently create or reuse a local identity and store account or session tokens in a workspace SQLite database.

Mitigation: Use an isolated workspace with restricted access; review and remove stored identity and tokens when no longer needed.

Risk: The generic video and common-AI implementation does not fully match the advertised farm-health mapping workflow.

Mitigation: Verify report contents, vegetation indices, and any map output independently before relying on results.

## Reference(s):

- [Farm-health API reference](references/api_doc.md)
- [Analysis service API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured text or JSON reports, with Markdown links for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May provide report links and cloud report-history entries; a farm-health image is not guaranteed by the supplied implementation.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata; artifact frontmatter says 1.0.15)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
