## Description:

Analyzes orchid images or videos to detect new shoots, flower spikes, root color and root condition, then returns a growth-status assessment and care-oriented guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External orchid hobbyists, greenhouse staff, and horticulture studios use this skill to evaluate orchid vitality from plant and transparent-pot root media. It supports growth-status analysis, structured reports, report links, and cloud report history lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Orchid images, videos, or supplied media URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Use only media that is appropriate to share with that service, and avoid sensitive personal media or private/internal URLs unless the service and retention practices are trusted.

Risk: Report history is associated with an internal identity that the skill creates or reuses automatically.

Mitigation: Review workspace identity handling before installation and avoid using the history feature where identity-linked report records are not acceptable.

Risk: Account tokens and profile data may be stored in the workspace data directory.

Mitigation: Protect the workspace data directory, restrict access to shared workspaces, and remove stored credentials when the skill is no longer needed.

## Reference(s):

- [Orchid Growth Status Detection API Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-orchid-growth-status-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, Files, API Calls, Guidance]

**Output Format:** [Markdown text containing structured JSON-style analysis results and report links; optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports jpg, png, mp4, avi, and mov inputs up to 10 MB; history queries return cloud report records.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter states 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
