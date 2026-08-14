## Description:

Identifies sleep states like deep sleep, light sleep, waking, and restlessness, then generates daily sleep reports and schedule analysis to help parents understand a baby's sleep patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and agents assisting them use this skill to analyze infant sleep-monitoring video or video URLs, classify sleep states, and retrieve structured daily reports or historical report lists. The output is for parenting reference and should not replace professional medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles highly sensitive infant sleep videos or video URLs through lifeemergence.com cloud services.

Mitigation: Use only videos the user is authorized to analyze, avoid unnecessary identifying context, and confirm the provider's retention, deletion, account-linkage, and access-control practices before use.

Risk: The skill silently creates or reuses a locally persisted backend identity and may link report history to that identity.

Mitigation: Use separate trusted workspaces for different families or accounts, clear persisted identity data when appropriate, and avoid shared machines unless account-linkage behavior is acceptable.

Risk: Sleep-state analysis can be mistaken for medical assessment.

Mitigation: Treat generated reports as parenting reference only and consult a pediatric clinician for sleep abnormalities or health concerns.

## Reference(s):

- [ClawHub skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-sleep-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON text with structured sleep-analysis results, historical report lists, and report export links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-generated report links; local file inputs are limited to mp4, avi, or mov videos up to 10 MB.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
