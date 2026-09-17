## Description:

Detects flames and smoke in image or video inputs and returns structured fire-warning analysis for environments such as industrial parks, forests, and warehouses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security or operations teams use this skill to submit fire-risk images, videos, or media URLs to a cloud analysis service and receive structured flame and smoke findings, severity information, recommendations, report links, or history tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted media, media URLs, identity fields, and report history may be sent to Life Emergence APIs and linked to a persistent local or cloud identity.

Mitigation: Review the provider and data-handling expectations before installation, and avoid submitting private media, sensitive identity data, or internal URLs.

Risk: The security scan reports silent identity creation and shared plaintext token storage behavior.

Mitigation: Do not place real API secrets in data/smyx-api-key.txt; prefer a release that removes silent registration and shared plaintext token storage.

Risk: The security scan reports unsafe default HTTP configuration.

Mitigation: Require HTTPS production configuration before use and avoid deployments that route analysis or report traffic over plain HTTP.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis)
- [API interface documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, guidance]

**Output Format:** [Markdown or JSON text with structured analysis results, recommendations, report links, and history tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud-hosted report export links; input evidence indicates support for jpg, jpeg, png, mp4, avi, and mov media up to 10 MB.]

## Skill Version(s):

1.0.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
