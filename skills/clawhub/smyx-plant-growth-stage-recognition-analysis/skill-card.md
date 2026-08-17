## Description:

Accurately identifies key growth stages of plants from germination to fruiting based on computer vision and deep learning, and provides structured data for precision agriculture decision support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Agricultural producers, agronomists, and agent developers use this skill to submit plant images, videos, or URLs for growth-stage analysis and to retrieve cloud-hosted historical reports for precision-agriculture decision support.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, URLs, and historical-report queries may be sent to lifeemergence.com cloud services.

Mitigation: Use only non-sensitive media and public URLs, and confirm that cloud processing is acceptable for the deployment context.

Risk: The skill may reuse workspace identity values and store tokens in a local SQLite database.

Mitigation: Review the workspace data directory before and after use, and clear stored identity state when it should not persist.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-recognition-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-like structured analysis text, with optional saved output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include growth-stage results, monitoring findings, recommendations, report links, and historical-report tables.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter and changelog mention 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
