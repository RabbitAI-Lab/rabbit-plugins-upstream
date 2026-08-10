## Description:

Identifies weed species and coverage density from field top-view images or videos and returns structured heatmap and report data for precision weeding decisions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural operators, agronomists, and developers use this skill to submit field images, videos, or URLs for weed species, coverage density, distribution, and historical report analysis that supports precision weeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Field images, videos, or URLs are sent to a configured cloud service for analysis.

Mitigation: Install only when this data sharing is acceptable, and avoid submitting sensitive or unrelated imagery.

Risk: The skill may create or reuse an internal account identity and store service tokens in the workspace data database.

Mitigation: Use a separate workspace for testing and clear data/smyx-common-claw.db when token or identity reuse is not desired.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-farmland-weed-identification-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Farmland weed API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown and JSON-like structured text with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video files or public media URLs; listed file formats and cloud API behavior are governed by the skill scripts and service configuration.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
