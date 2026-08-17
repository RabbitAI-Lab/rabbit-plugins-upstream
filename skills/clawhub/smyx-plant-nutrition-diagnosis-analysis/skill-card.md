## Description:

Diagnoses plant nutrient deficiency or excess from leaf imagery using computer vision and plant physiology, and outputs targeted fertilization suggestions for precision nutrient management.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, growers, and agricultural support teams use this skill to analyze plant leaf images or videos for nutrient deficiency or excess indicators and receive structured diagnosis, cause analysis, report links, and fertilization guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images or videos, report metadata, and an internal user identifier may be sent to Life Emergence cloud services for analysis.

Mitigation: Use only with clear user consent for cloud processing, and avoid sensitive farm, facility, or personal imagery unless the deployment has approved data handling terms.

Risk: The skill can silently create or reuse cloud-linked identities and stores identity and token data locally.

Mitigation: Review local account and token storage before deployment, define cleanup procedures, and avoid shared workspaces unless token isolation is confirmed.

Risk: Historical cloud reports can be retrieved without a clear confirmation step.

Mitigation: Require explicit user confirmation before historical report queries and verify that report access is scoped to the intended user or workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrition-diagnosis-analysis)
- [API interface documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, files]

**Output Format:** [Markdown or JSON analysis report with optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include diagnosis summaries, cause analysis, fertilization suggestions, report links, and historical report tables retrieved from cloud services.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
