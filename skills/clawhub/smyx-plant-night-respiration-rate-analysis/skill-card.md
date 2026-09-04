## Description:

Estimates relative nighttime plant respiration intensity from canopy thermal imagery and optional ambient CO2 data, then returns structured analysis, level assessment, risk notes, recommendations, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can use this skill to submit nighttime plant canopy thermal media for cloud-based respiration intensity estimation and to query prior analysis reports. It is aimed at plant factories, artificial climate chambers, and closed greenhouse monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant media and report queries are sent to a vendor service.

Mitigation: Use non-sensitive plant media and avoid private network URLs unless the publisher clarifies data handling, consent, and deletion behavior.

Risk: The skill may silently create or reuse a local workspace identity and persist returned account tokens locally.

Mitigation: Review the installation in an isolated workspace and confirm token retention and cleanup expectations before using it with production accounts.

Risk: Respiration estimates and health notes may be inaccurate or incomplete.

Mitigation: Treat the output as operational guidance only and validate important plant-health or environmental-control decisions with appropriate agricultural instruments or expert review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Plant night respiration API reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance]

**Output Format:** [Structured text, Markdown tables for report lists, and JSON-level analysis output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a respiration intensity index, level assessment, abnormality notes, environment-control recommendations, and report links.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
