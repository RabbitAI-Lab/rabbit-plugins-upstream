## Description:

Analyzes video inputs for mental-health and psychological behavior signals, then returns structured reports with tendency indicators, suggestions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to submit a local video or public video URL for mental-health analysis, retrieve historical report lists from the cloud service, and receive structured result summaries for non-diagnostic reference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Videos or video URLs may be sent to a remote service, and reports may be stored and queried in the cloud.

Mitigation: Use only with appropriate user consent and data-handling review for sensitive health-related media.

Risk: Mental-health analysis output could be mistaken for medical diagnosis or treatment advice.

Mitigation: Present results as non-diagnostic reference information and direct users with significant concerns to qualified professionals.

Risk: Configuration may include development, private, or HTTP service endpoints that are unsuitable for deployment.

Mitigation: Review and correct endpoint configuration before installation or operational use.

Risk: The skill may create or reuse local identity and token persistence for cloud report association.

Mitigation: Review local identity storage behavior and retention before enabling the skill in shared or regulated environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [smyx_analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown text, JSON analysis payloads, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May save report output to a file when --output is supplied; analysis supports local mp4, avi, and mov files up to 10MB or public video URLs.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact SKILL.md frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
