## Description:

Analyzes fixed-camera videos of feeders and waterers to quantify livestock feeding duration, feeding bouts and drinking frequency, comparing them against individual baselines to raise behavior anomaly alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External farm operators, livestock managers, and developers use this skill to analyze feeder or waterer camera footage, generate structured feeding and drinking behavior reports, and review cloud-hosted historical reports for the current identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media or supplied media URLs are sent to a cloud service for analysis.

Mitigation: Use only footage that is approved for the configured cloud service and account, and avoid uploading media that contains unnecessary sensitive information.

Risk: The skill can create or reuse backend identity state and query identity-linked historical reports.

Mitigation: Install only where this identity behavior is expected, and review account isolation before using historical report queries.

Risk: Authentication tokens may be stored in a local workspace database.

Mitigation: Protect the workspace, rotate credentials if the workspace is shared or exposed, and remove local state when decommissioning the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [Skill API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and tables, JSON responses, and optional saved text files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding duration, feeding bout counts, drinking frequency, baseline comparison, anomaly level, timestamps, and report links.]

## Skill Version(s):

1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
