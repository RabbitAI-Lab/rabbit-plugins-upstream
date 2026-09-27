## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels appearing in the target area, with support for video streams and image detection in general security surveillance scenarios.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security operations users can use this skill to analyze surveillance images or video for common object classes such as people, vehicles, pets, and parcels. It can return structured detection results, report links, and cloud history report listings for security-monitoring workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images, videos, and remote media URLs may be sent to configured lifeemergence.com APIs.

Mitigation: Use the skill only for media that is approved for external API processing, and confirm data-handling requirements before deployment.

Risk: The skill can create or reuse an internal identity, store tokens locally, and retrieve cloud report history tied to that identity.

Mitigation: Run it in a controlled environment, review stored identity and token handling, and clear local credentials or history when they are no longer needed.

Risk: Cloud report history may expose prior detection report metadata or links associated with the resolved identity.

Mitigation: Limit access to users authorized to view that identity's reports and review report links before sharing output.

## Reference(s):

- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, json, files]

**Output Format:** [Markdown reports, JSON detection results, and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud history tables associated with the internally resolved user identity.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter reports 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
