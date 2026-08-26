## Description:

Assesses medicinal-herb leaf images or videos for visual indicators of active-ingredient accumulation and returns a Low, Medium, High, or Peak trend level with harvest-timing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External herb growers, GAP planting bases, cooperatives, and pharmaceutical raw-material teams use this skill to assess visual trends in medicinal-herb active-ingredient accumulation from uploaded images, videos, or URLs. It can also query account-linked historical analysis reports from the backend service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded plant images, videos, URLs, and report history are sent to a backend service.

Mitigation: Use only when the publisher and backend data handling are acceptable; avoid sensitive cultivation or operational media unless retention and access expectations are clear.

Risk: The skill silently resolves or creates an account-linked identity and can store authentication tokens locally.

Mitigation: Run in an isolated workspace, inspect local data storage before and after use, and avoid sharing workspace data directories across trust boundaries.

Risk: Security evidence reports mismatched pet-analysis backend artifacts in the release.

Mitigation: Review backend endpoints and returned report content before relying on results for harvesting or quality decisions.

Risk: The analysis is based on visual indicators and is not a formal chemical assay.

Mitigation: Treat outputs as decision support and confirm quality-critical decisions with HPLC, pharmacopeial, or other professional testing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-chinese-herbal-ingredient-trend-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text with structured JSON-like analysis content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write the returned report text to a user-specified output file.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
