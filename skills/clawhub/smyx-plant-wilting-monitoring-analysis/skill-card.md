## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, capturing early signs before visible symptoms and providing early warnings for precision irrigation and disease control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze plant images, videos, or submitted URLs for early wilting indicators, likely cause categories, severity estimates, recommendations, report links, and cloud report-history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or submitted URLs may be sent to the publisher's service.

Mitigation: Use the skill only when that data sharing is acceptable, and request explicit retention and deletion controls from the publisher before production use.

Risk: The skill silently manages identity, stores reusable identity tokens locally, and queries cloud report history.

Mitigation: Review the automatic account-linkage behavior before installation, avoid sensitive identifiers, and ask the publisher for a way to reset or disable the local identity database.

Risk: The release is bundled with a dev HTTP/private-network service configuration.

Mitigation: Require a production HTTPS-only configuration before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Markdown or JSON analysis reports with optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can output structured analysis results, recommendations, report links, and Markdown tables for cloud history queries.]

## Skill Version(s):

1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
