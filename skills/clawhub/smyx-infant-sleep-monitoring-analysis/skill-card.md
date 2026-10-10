## Description:

Analyzes infant sleep media to identify sleep states and provide sleep reports and routine insights for caregivers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents and caregivers use this skill to analyze infant sleep recordings, review sleep-state summaries and daily reports, and examine past reports. Results are for parenting reference, not a substitute for pediatric advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private infant sleep recordings are uploaded to lifeemergence.com services for analysis.

Mitigation: Review the service's data handling and use only recordings you are comfortable uploading.

Risk: A persistent local/cloud identity can be created or reused without explicit per-use notice.

Mitigation: Confirm which identity is used before processing family media; remove local data or tokens after testing with private recordings.

Risk: History queries can retrieve cloud reports without clear per-use control.

Mitigation: Avoid history queries until you understand which account or default identity they access.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Skill API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured report or Markdown table with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save results to a local file; reports are for parenting reference, not medical advice.]

## Skill Version(s):

1.0.14 (source: ClawHub release; bundled SKILL.md says 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
