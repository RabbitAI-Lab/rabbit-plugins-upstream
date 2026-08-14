## Description:

Analyzes feeder or IPC camera images and videos to detect cats and dogs, recognize pet identities, enroll pets in a recognition database, and return structured reports for smart feeding workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External smart-feeder users and agent builders use this skill to submit pet camera media or URLs for cloud-based pet detection, identity recognition, enrollment, and history report lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-camera images, videos, supplied URLs, account-linked report history, and generated identity values may be sent to LifeEmergence-hosted APIs.

Mitigation: Install only when that cloud handling is acceptable, and avoid sensitive signed URLs or private household footage unless the user has approved that processing.

Risk: The skill may silently create or reuse an identity and store service tokens in a local SQLite-backed workspace data directory.

Mitigation: Review and protect the local workspace data directory, rotate or remove cached tokens when no longer needed, and avoid shared workspaces for sensitive pet-camera reports.

Risk: Automated pet detection and identity recognition can be incorrect or incomplete.

Mitigation: Treat results as smart-feeding support only and require human confirmation before using the analysis for safety, health, or feeding decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and JSON-like structured analysis results, with optional saved JSON output files and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report or export links and history tables; output detail can be basic, standard, or json.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
