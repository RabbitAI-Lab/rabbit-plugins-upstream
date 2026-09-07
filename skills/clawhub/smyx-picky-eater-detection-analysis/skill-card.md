## Description:

Analyzes pet feeding-bowl videos or URLs through server-side APIs to identify selective eating behaviors, record frequency, and return feeding-adjustment suggestions without providing disease diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, smart-feeder operators, boarding centers, and pet hospital staff use this skill to analyze feeding-bowl media for selective refusal patterns such as pushing kibble aside, eating only treats, or sniffing and leaving. It can also retrieve cloud-hosted history reports for the associated user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet media and identity-linked report data are sent to configured Life Emergence/Open API services.

Mitigation: Use the skill only with media and report data approved for that remote service, and review endpoint configuration before deployment.

Risk: The skill may create or reuse a local account record and persist service tokens in the workspace SQLite database.

Mitigation: Run it in an isolated workspace, avoid shared environments, and clear local account or token storage according to the operator's retention policy.

Risk: Feeding behavior analysis can be mistaken for medical diagnosis.

Mitigation: Treat outputs as feeding-behavior guidance only and route health concerns to qualified veterinary review.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet picky eater detection API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown text with JSON-style analysis content and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include feeding behavior findings, frequency summaries, feeding-adjustment suggestions, and cloud report export links.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
