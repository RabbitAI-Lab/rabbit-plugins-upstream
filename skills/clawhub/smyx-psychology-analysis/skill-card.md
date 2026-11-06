## Description:

Analyzes videos for mental health and behavioral patterns, then provides structured reports and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users can submit a video file or URL for a structured mental health and behavior report, or retrieve previous reports from the service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive video may be uploaded for analysis despite the no-analysis option.

Mitigation: Wait for the no-analysis behavior to be fixed; confirm recorded subjects' authorization, the processor, and retention and deletion options before submitting footage.

Risk: API-address override and credential handling can put private footage or account separation at risk.

Mitigation: Wait for the API override and credential handling fixes before using private footage, protect locally cached tokens, keep accounts separate, and avoid shared workspaces for personal reports.

Risk: Provider privacy practices and diagnostic accuracy cannot be established from the supplied evidence.

Mitigation: Review the provider's privacy practices and treat reports as informational; they do not replace professional diagnosis or treatment.

## Reference(s):

- [API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured text or JSON reports; historical reports can be presented as a Markdown table.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are for mental health reference and do not replace professional diagnosis or treatment.]

## Skill Version(s):

1.0.24 (source: server-resolved release metadata; SKILL.md lists 1.0.23)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
