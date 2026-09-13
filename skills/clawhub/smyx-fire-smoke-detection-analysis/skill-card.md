## Description:

Detects fire and smoke in video scenes, supports video stream and image analysis, and is intended for early fire-warning scenarios such as security surveillance, forest fire prevention, and industrial parks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operators can use this skill to submit video or image inputs for fire and smoke detection, then receive structured detection results, risk indicators, recommendations, and report links. It also supports querying cloud-hosted historical detection reports for the resolved internal user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Media inputs and report history are handled by remote cloud services.

Mitigation: Do not use sensitive footage until the publisher documents account behavior, data retention, and production endpoint handling.

Risk: Security evidence reports plaintext development HTTP endpoints for media and credential traffic.

Mitigation: Replace development endpoints with HTTPS production endpoints before commercial or sensitive use.

Risk: The skill silently creates or reuses an internal identity and stores backend tokens locally.

Mitigation: Install in an isolated workspace, review local token storage, and remove stored identity data when the skill is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-smoke-detection-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)
- [Shared API interface notes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown text with structured JSON content and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write an optional output file when requested; supports basic, standard, and json detail modes.]

## Skill Version(s):

1.0.14 (source: server release evidence; artifact frontmatter says 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
