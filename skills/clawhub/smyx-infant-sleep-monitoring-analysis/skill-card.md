## Description:

Identifies infant sleep states such as deep sleep, light sleep, waking, and restlessness, then generates sleep reports and schedule analysis to help caregivers understand sleep patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and agents use this skill to analyze infant sleep monitoring media, classify sleep states, generate structured daily reports, and retrieve prior sleep analysis reports. It is for parenting insight and does not replace pediatric medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Infant room media and derived sleep reports are sent to a configured cloud service.

Mitigation: Use only media you are authorized to process, confirm the service's retention and access controls, and avoid real family data unless those controls meet your requirements.

Risk: The skill can silently create or reuse identity records and store tokens locally.

Mitigation: Review local data storage, token handling, and report-history isolation before deployment, especially on shared agent workspaces.

Risk: Sleep analysis can be mistaken for medical guidance.

Mitigation: Treat outputs as parenting reference material only and consult a pediatric clinician for abnormal sleep behavior or health concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, files, guidance]

**Output Format:** [Structured text or JSON; historical report lists may be presented as Markdown; optional output files contain the returned report text.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or public media URLs; documented local formats are mp4, avi, and mov with a 10 MB size limit.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
