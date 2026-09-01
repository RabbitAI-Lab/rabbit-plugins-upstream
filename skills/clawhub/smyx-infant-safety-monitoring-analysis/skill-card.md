## Description:

Monitors infant behavior via visual AI, automatically identifying high-risk actions like rolling over, mouth/nose obstruction, climbing, or falling from bed, and triggers instant safety warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze infant activity videos or URLs for safety-related behaviors, warnings, care suggestions, structured reports, and history queries. Results are advisory and should not replace real-time caregiver supervision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may send sensitive infant or home videos to the publisher's cloud service.

Mitigation: Use only media approved for upload, review the publisher's retention and deletion practices, and avoid real family footage until those practices are acceptable.

Risk: The skill creates or reuses a local identity and token database for report history.

Mitigation: Review local token storage and access controls before deployment, and clear local identity data when the skill is no longer needed.

Risk: Safety reports are advisory and may be incomplete or delayed.

Mitigation: Do not rely on the skill as real-time child safety monitoring; maintain caregiver supervision and use professional judgment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-safety-monitoring-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Infant Safety Monitoring API Documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown or JSON analysis reports with warnings, suggestions, report links, and optional history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or public video URLs; cloud analysis and report-history queries may involve infant or home media and local identity/token state.]

## Skill Version(s):

1.0.13 (source: server release metadata; artifact frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
