## Description:

Screens livestock and poultry imagery for possible fever or low body temperature and reports early warnings.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators and animal-health teams use thermal or visible-light images and videos to screen herds and flocks for possible temperature anomalies and review past reports. Results are screening alerts, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A hidden identity override may allow requests under another account identity, including report access.

Mitigation: Do not deploy until the publisher protects or removes the identity override and confirms server-side authorization for report access.

Risk: Media and report queries go to external services, and account tokens may remain in a local workspace database.

Mitigation: Avoid shared workspaces and sensitive imagery until token retention and access controls are documented and verified.

## Reference(s):

- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis results or a Markdown table of historical reports; JSON output is available]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include estimated temperature ranges, anomaly levels, affected animals, and report links]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled frontmatter lists 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
