## Description:

Analyzes aquarium plant images or videos to identify visible leaf color and morphology issues, produce health assessments, and suggest care directions for aquarium owners, aquascapers, and aquarium shops.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and aquarium operators use this skill to submit aquarium plant images, videos, or URLs for visual health assessment, likely symptom identification, care-direction suggestions, report links, and cloud history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media files, media URLs, and cloud report queries may be sent to backend services.

Mitigation: Use the skill only with aquarium media and report data that are approved for the configured backend.

Risk: The skill can create or reuse a local account identity and store service tokens in workspace data.

Mitigation: Run it in an isolated workspace, inspect local data storage after use, and remove stored identity or token files when they are no longer needed.

Risk: The configured backend may resolve to a development or private service.

Mitigation: Review the bundled configuration before installation or execution and confirm the service endpoints are intended for the deployment environment.

Risk: Visual plant-health symptoms can be ambiguous and may not support precise water-chemistry conclusions.

Mitigation: Treat results as care-direction guidance and confirm significant aquarium changes with water testing or expert review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-aquarium-plant-health-monitor-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown text with structured analysis content, JSON-formatted result details where available, and report links; optional file output when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local media files and media URLs; artifact documentation states jpg, png, mp4, avi, and mov inputs up to 10 MB.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
