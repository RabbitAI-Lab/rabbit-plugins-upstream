## Description:

Analyzes resting pet videos for respiratory rate abnormalities and returns monitoring reports with alerts and suggested follow-up.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, veterinary teams, and boarding staff can review resting pet videos for changes in breathing rate and access monitoring reports. Results are informational and do not replace veterinary assessment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos and provided video URLs are sent to a cloud service for analysis and reports may be retained there.

Mitigation: Review the publisher's privacy terms and avoid submitting sensitive household footage or private/internal URLs unless cloud processing and retention are acceptable.

Risk: The skill silently creates or reuses a local identity and stores reusable authentication tokens.

Mitigation: Review local identity and token storage before use, and limit access to the device and its stored credentials.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-respiratory-rate-abnormal-detect-analysis)
- [Respiratory monitoring API documentation](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured monitoring report or Markdown history table, with report links when available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis results to a JSON file.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; artifact frontmatter says 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
