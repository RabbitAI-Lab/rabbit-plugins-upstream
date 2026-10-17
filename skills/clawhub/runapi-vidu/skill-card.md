## Description:

Generate Vidu Q4 videos from a first-frame image or reference images and optional audio through RunAPI, using the CLI for one-off requests or an SDK for application integration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to generate Vidu Q4 videos from image inputs and optional reference audio, either as one-off RunAPI tasks or through an SDK in applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: RunAPI authentication may expose an API key if handled insecurely.

Mitigation: Prefer environment-based API-key authentication or saved CLI configuration; do not disclose credentials in output.

Risk: Generation uploads selected media to RunAPI/Vidu and may incur charges.

Mitigation: Use only media the user intends to upload, review RunAPI pricing, and obtain authorization before submitting another paid task.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/runapi-ai/skills/runapi-vidu)
- [Vidu model overview and pricing](https://runapi.ai/models/vidu.md)
- [Vidu provider overview](https://runapi.ai/providers/vidu.md)
- [Vidu SDK integration](https://github.com/runapi-ai/vidu-sdk)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, JSON task results, Video files]

**Output Format:** [Markdown guidance with CLI or SDK instructions; JSON responses and downloaded video deliverables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation requires RunAPI authentication; generated media must be downloaded and verified before completion.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
