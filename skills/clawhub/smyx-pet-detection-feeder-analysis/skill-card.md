## Description:

Based on computer vision, this skill detects and recognizes cats and dogs in feeder or IPC camera images and videos, supports pet identity recognition and enrollment, and returns structured reports for smart feeding scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and smart-feeding operators use this skill to analyze feeder or IPC camera media for cat and dog detection, pet identity recognition, pet enrollment, and historical report lookup. It is intended to support pet identification management and feeding decisions, with results treated as reference material that may require human confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends pet-camera images, videos, URLs, identity values, and authentication tokens to backend services.

Mitigation: Install only when the publisher and backend service are trusted, and disclose or limit media uploads according to the deployment's privacy requirements.

Risk: The packaged default environment can use insecure HTTP development endpoints for private media and credentials.

Mitigation: Switch configuration to HTTPS production endpoints before operational use and review endpoint settings during deployment.

Risk: The skill silently handles reusable identity and service tokens and may persist identity-related data in the workspace database.

Mitigation: Restrict workspace access, rotate service credentials as appropriate, and review local persistence practices before installation.

Risk: Pet recognition and feeding recommendations can be incorrect or incomplete.

Mitigation: Use results as smart-feeding reference material and require human confirmation for consequential care or feeding decisions.

## Reference(s):

- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-detection-feeder-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON structured analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include pet detection or enrollment results, historical report tables, recommendations, and report links.]

## Skill Version(s):

1.0.11 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
