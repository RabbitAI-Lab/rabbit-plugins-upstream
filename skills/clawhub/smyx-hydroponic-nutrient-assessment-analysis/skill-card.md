## Description:

This skill analyzes hydroponic root and leaf images or videos to qualitatively assess nutrient concentration status and provide directionally appropriate adjustment advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Hydroponic growers, plant-factory operators, home gardeners, and developers integrating ClawHub skills use this agent to review root and leaf media for visual signs of overly concentrated or overly dilute nutrient solution. It returns qualitative findings, adjustment guidance, report links, and history-list output for follow-up review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Hydroponic media inputs or URLs are sent to a lifeemergence.com cloud service for analysis and report retrieval.

Mitigation: Use only intended hydroponic images, videos, or public URLs, and review the cloud-service data handling expectations before installation.

Risk: The skill can create or reuse a local/cloud identity and store authentication tokens for report history.

Mitigation: Check the workspace data directory for retained smyx user or token database files when removing the skill, and avoid sharing workspaces that may contain those files.

Risk: Visual-only nutrient assessment may be incomplete for operational decisions.

Mitigation: Treat results as qualitative growing guidance, and verify severe concentration concerns with direct observation or measurement before making high-impact changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-hydroponic-nutrient-assessment-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Hydroponic nutrient assessment API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured report text or JSON with qualitative nutrient status, visual findings, adjustment advice, and report links; history queries can be formatted as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local file paths or public media URLs for jpg, png, mp4, avi, and mov inputs up to 10 MB; output can optionally be written to a file.]

## Skill Version(s):

1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
