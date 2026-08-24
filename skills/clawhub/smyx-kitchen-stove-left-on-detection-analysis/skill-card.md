## Description:

Analyzes fixed kitchen-camera video for human activity and stove flame or heat-source signals to detect unattended stove-left-on conditions and produce alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External caregivers, home-safety operators, and elder-care providers use this skill to analyze kitchen camera images or videos and identify unattended active-stove scenarios that may need alerting or valve-shutdown follow-up.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Household kitchen video may be sent to configured backend services.

Mitigation: Confirm production endpoint destinations before use, disable dev or private HTTP endpoints, and obtain informed consent for video processing and retention.

Risk: The skill can silently create or reuse user identities and query cloud report history.

Mitigation: Require deployment approval for identity and history access, isolate identities per installation, and document who can view retained reports.

Risk: Tokens may be stored in a shared local SQLite database.

Mitigation: Store tokens in a proper secret store, restrict local file permissions, and avoid shared-machine identity reuse.

Risk: A stove-left-on alert or valve-shutdown hint may be safety-critical and can be wrong if video coverage or model interpretation is poor.

Mitigation: Use clear stove-area camera coverage, validate alert behavior before deployment, and require human or approved device-side safeguards for emergency action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-kitchen-stove-left-on-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown text with JSON-style structured analysis and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can print current analysis results, historical report lists, and optionally write output text to a file.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
