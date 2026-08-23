## Description:

Analyzes infant activity images or videos with visual AI to identify high-risk behaviors such as rolling over, mouth/nose obstruction, climbing, fence crossing, and fall risk, then returns warnings, care suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Parents, caregivers, and developers use this skill to analyze infant activity media for possible safety risks and to retrieve cloud report history for prior analyses. It is an assistive monitoring workflow and is not a replacement for real-time supervision or professional care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive infant or home videos and URLs may be sent to a configured cloud service.

Mitigation: Use only with explicit consent, review the configured endpoint and retention terms, and avoid submitting unnecessary or identifying media.

Risk: Report history is associated with an automatically resolved local identity.

Mitigation: Confirm per-user scoping and account isolation before shared or production use.

Risk: Account tokens may be stored in a workspace SQLite database.

Mitigation: Restrict workspace access, rotate credentials when needed, and prefer a release with documented token storage controls.

Risk: The skill provides assistive safety analysis and may miss or misclassify hazards.

Mitigation: Keep caregiver supervision in place and treat reports as supplemental information, not professional care advice.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Infant safety monitoring API documentation](references/api_doc.md)
- [Analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with structured findings, safety warnings, care suggestions, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted history/report links and optional saved report output.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter reports 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
