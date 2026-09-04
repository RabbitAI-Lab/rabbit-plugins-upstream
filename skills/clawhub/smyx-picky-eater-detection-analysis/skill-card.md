## Description:

Analyzes pet feeding-bowl videos or supplied video URLs through a remote API to detect picky-eating behaviors and return structured feeding behavior reports and feeding-adjustment suggestions without disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, smart feeder operators, boarding centers, and veterinary inpatient teams use this skill to submit feeding-area video for picky-eater behavior detection, frequency tracking, and feeding-adjustment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet feeding videos or supplied video URLs, plus an internal user identifier, are sent to the configured remote service.

Mitigation: Install only when this data sharing is acceptable, and review the configured service endpoint before use.

Risk: The package includes non-public HTTP development endpoints in its configuration set.

Mitigation: Review and replace development endpoints with approved production endpoints before deployment.

Risk: The runtime may create local database records containing reusable identity tokens.

Mitigation: Store the workspace data directory securely and clear or rotate local token records when access should no longer persist.

## Reference(s):

- [Skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured text, with optional local file output when requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include report links and historical report listings returned by the configured remote service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.13)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
