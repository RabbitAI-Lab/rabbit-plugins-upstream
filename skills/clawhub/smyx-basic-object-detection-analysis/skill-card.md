## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels appearing in the target area, with support for video stream and image detection in general security surveillance scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security operations teams, and ClawHub users use this skill to run basic object detection on surveillance images, videos, local files, or media URLs and receive structured detection reports or report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends surveillance images, videos, media URLs, report queries, and identity-linked metadata to LifeEmergence cloud services.

Mitigation: Use only approved media and URLs, avoid sensitive camera feeds unless authorized, and review the cloud service's handling of uploads and report history before installation.

Risk: The skill can silently create or reuse a cloud identity and store local tokens.

Mitigation: Review account creation, token storage, retention, and deletion behavior before deployment, and run the skill only in an environment where those behaviors are acceptable.

Risk: Detection results are intended for security management reference and may not be sufficient for final response decisions.

Mitigation: Keep human review in the workflow for operational decisions and follow the deploying organization's procedures for incident handling.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, files]

**Output Format:** [Markdown or JSON text, with optional saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs can include object counts, category-level detection details, history records, and report export links.]

## Skill Version(s):

1.0.14 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
