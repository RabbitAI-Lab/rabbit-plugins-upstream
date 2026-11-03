## Description:

Analyzes care video and optional audio for signs of confusion or disorientation in people with dementia and can trigger orientation-soothing actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Care teams and care-platform operators use the skill to request analysis of submitted camera footage for behavioral signs of confusion or disorientation and to retrieve structured results or prior reports. It can also initiate orientation prompts or caregiver notifications, so deployment should be consent-based and its configured actions should be reviewed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the documented export-only mode can still upload care recordings.

Mitigation: Do not use real care recordings in export-only mode until the behavior is corrected and verified; confirm what is sent before processing recordings.

Risk: Ordinary requests may silently create service accounts, and the account that will own reports may be unclear.

Mitigation: Confirm the service account and report owner before use, and review token storage and account creation with the service operator.

Risk: Cloud processing, deletion and retention behavior, and any enabled speaker, lighting, or notification actions are not verified in the security evidence.

Mitigation: Verify data processing and deletion terms and review or disable intervention actions until their safeguards are understood; obtain required care-recipient or representative consent before deployment.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-dementia-confusion-orientation-analysis)
- [API interface notes](artifact/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis results and report links; history listings can be presented as Markdown tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results may include behavioral observations, orientation-soothing actions, and links to reports.]

## Skill Version(s):

1.0.12 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
