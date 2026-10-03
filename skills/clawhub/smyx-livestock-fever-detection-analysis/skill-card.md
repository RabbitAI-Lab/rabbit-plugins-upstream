## Description:

Analyzes livestock and poultry thermal or visible-light images and videos for possible fever or hypothermia warnings and provides access to analysis reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock keepers and animal-health teams use the skill to screen herd or flock imagery for possible temperature abnormalities and review associated reports. Results are screening aids, not veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local livestock images or videos are uploaded to lifeemergence.com services for analysis.

Mitigation: Use only media approved for transfer to that service and review the skill before installation.

Risk: The skill creates or reuses an account identity and may automatically query account-linked cloud report history.

Mitigation: Use it only where cloud account linkage and retrieval of report history are acceptable.

Risk: Account tokens are retained in a local workspace database.

Mitigation: Restrict access to the workspace and review local token storage before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results or Markdown report-history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormality warnings, report links, and an optional saved result file.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
