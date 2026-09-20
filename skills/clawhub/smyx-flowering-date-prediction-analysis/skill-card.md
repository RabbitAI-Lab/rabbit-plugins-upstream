## Description:

Predicts likely full-bloom dates for ornamental or cut-flower plants from bud images or videos, optional temperature and light data, and cloud analysis results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, greenhouse operators, botanical gardens, and flower-tourism teams use this skill to estimate near-term flowering windows, review structured reports, and query historical analysis records for production planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release advertises flowering-date prediction but includes generic cloud media-analysis and pet-health API remnants.

Mitigation: Review the code and documentation before deployment, and align endpoints, labels, scene codes, and examples to the flowering use case.

Risk: The skill can automatically create or reuse local account identity and send media, credentials, and report queries to remote services.

Mitigation: Require explicit user or organization consent for account linkage, minimize locally stored tokens, and protect any credentials used by the runtime.

Risk: Development HTTP configuration and non-HTTPS service URLs are present in artifact configuration.

Mitigation: Disable development configurations in releases and require HTTPS-only production endpoints.

Risk: Bloom-date predictions are planning aids and may be inaccurate for production scheduling.

Mitigation: Use predictions with confidence intervals as advisory output and confirm final scheduling with manual inspection and local growing history.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown text with JSON-formatted analysis content, structured report summaries, report links, and optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image or video paths and public media URLs; documented media size limit is 10 MB.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
