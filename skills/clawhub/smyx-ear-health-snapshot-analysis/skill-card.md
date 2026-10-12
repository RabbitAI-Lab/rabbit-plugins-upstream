## Description:

Analyzes pet ear images or videos for visible redness, discharge, and earwax, then provides observations, alerts, and recommendations without making a veterinary diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, boarding staff, and veterinary pre-screening teams use this skill to review pet ear footage for visible abnormalities and retrieve prior analysis reports. Results are observational and do not replace veterinary care.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet ear media or URLs are sent to a cloud service for analysis.

Mitigation: Send only media you are comfortable sharing with the configured Life Emergence service.

Risk: The skill silently creates or reuses an internal identity and stores tokens locally.

Mitigation: Review local data retention and cleanup before use with sensitive media or shared machines.

Risk: Broad automatic triggers can retrieve cloud report history.

Mitigation: Confirm the user's intent before fetching prior reports and review service-side report deletion options.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-ear-health-snapshot-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis text or JSON; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include observations, alerts, recommendations, and report links; not a veterinary diagnosis.]

## Skill Version(s):

1.0.12 (source: ClawHub release; bundled SKILL.md says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
