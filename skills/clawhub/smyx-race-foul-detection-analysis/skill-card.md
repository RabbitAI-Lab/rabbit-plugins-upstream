## Description:

Analyzes pet race start or finish footage to identify start timing, lane assignment, finish order, false starts, lane crossings, and evidence useful for referee review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and event operators use this skill to submit pet race video files or URLs for foul detection and structured referee-assistance results. It can also retrieve cloud-hosted history records for prior race-foul reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Race footage or video URLs are sent to the LifeEmergence cloud service for analysis.

Mitigation: Use only footage approved for cloud processing, and review retention, deletion, and account-linking expectations before using sensitive event media.

Risk: The skill can create or reuse a local identity and store authentication tokens or report history in the workspace data directory.

Mitigation: Use an isolated workspace on shared machines, restrict filesystem access to the workspace data directory, and clear local identity or token data when access should end.

Risk: The security scan verdict is suspicious because cloud service contact and local identity handling require review before installation.

Mitigation: Review the security summary and guidance before deployment, and install only when the cloud-service and local-storage behavior matches the intended environment.

Risk: Video-based foul detection is referee assistance and may be affected by footage quality, frame rate, or event-specific thresholds.

Mitigation: Treat outputs as decision support, use clear supported-format footage, and keep final rulings with the responsible human official.

## Reference(s):

- [API Interface Documentation](references/api_doc.md)
- [SMYX Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands]

**Output Format:** [Markdown or JSON text with structured analysis results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files or video URLs, optional report-history listing, and optional file output.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
