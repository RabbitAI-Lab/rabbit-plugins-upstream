## Description:

Analyzes driver videos or video URLs to identify unsafe driving behaviors and produce structured safety reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to submit driver footage or video URLs for safety behavior analysis, then review structured findings, recommendations, report links, or historical report lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Driver videos, video URLs, or related analysis data may be sent to the configured remote service.

Mitigation: Review the configured service destination, obtain appropriate consent, and avoid submitting private footage unless the service retention and access controls are acceptable.

Risk: The skill can query cloud history for the current identity.

Mitigation: Use the skill only with approved account contexts and review expected report visibility before enabling history queries.

Risk: The skill may create or reuse local identities and persist identity or service tokens in the local workspace database.

Mitigation: Protect the workspace, restrict use on shared systems, and remove or rotate persisted tokens when they are no longer needed.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-drive-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Markdown or JSON driving behavior analysis reports; optional saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety findings, recommendations, report links, and historical report tables returned by the configured service.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
