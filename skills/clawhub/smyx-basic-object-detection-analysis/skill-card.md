## Description:

Detects people, vehicles, non-motorized vehicles, pets, and parcels in uploaded images or video streams for security-surveillance review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and security operators use this skill to submit surveillance images or video streams for object detection reports and to retrieve prior reports from the configured cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Surveillance images or videos and identity metadata may be sent to configured lifeemergence.com services.

Mitigation: Use only approved media, confirm the publisher's data handling and deletion process, and avoid sensitive footage unless that process is acceptable.

Risk: The skill can create or reuse a local identity and store account or session tokens in the workspace data directory.

Mitigation: Run in a controlled workspace, restrict access to local data files, and clear local tokens when the skill is no longer needed.

Risk: History queries can retrieve cloud-hosted report records associated with the resolved identity.

Mitigation: Confirm the identity context before querying history and avoid using shared workspaces for sensitive report access.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-basic-object-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Documentation](references/api_doc.md)
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration]

**Output Format:** [Markdown text with structured JSON report content and optional saved result files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report export links and cloud history query results.]

## Skill Version(s):

1.0.12 (source: evidence release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
