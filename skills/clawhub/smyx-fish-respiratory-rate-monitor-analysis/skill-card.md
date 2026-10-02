## Description:

Analyzes aquarium fish gill-cover video to estimate breathing rate and provide abnormal-rate alerts and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarium keepers, aquaculture operators, and developers use fish gill-cover recordings or video URLs to estimate respiratory rate, review possible abnormalities, and retrieve past reports. Results are monitoring guidance, not a veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Aquarium media or video URLs may be sent to the configured cloud service.

Mitigation: Use only media and URLs you are comfortable sharing with that service, and review the publisher before installation.

Risk: The skill may create or reuse an identity and persist authentication tokens for report access.

Mitigation: Review the identity and token-storage behavior before running it in a shared or sensitive workspace.

Risk: History-related requests may automatically retrieve cloud reports.

Mitigation: Confirm that cloud report access is appropriate before requesting historical records.

## Reference(s):

- [Fish respiratory rate monitoring API documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-respiratory-rate-monitor-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured analysis report or Markdown history table; optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include breathing rate, alerts, recommendations, and links to cloud reports.]

## Skill Version(s):

1.0.10 (source: ClawHub release metadata; bundled frontmatter states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
