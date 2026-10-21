## Description:

Analyzes outdoor images and videos to detect people, motor vehicles, non-motorized vehicles, and pets, and provides monitoring reports for yards, orchards, and farms.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Homeowners, farm operators, and security teams use this skill to check outdoor images or videos for people, vehicles, and pets, review risk indications, and retrieve past monitoring reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive outdoor surveillance images or videos are sent to the Lifeemergence cloud service.

Mitigation: Use the skill only when cloud processing of the footage is acceptable.

Risk: Report history is associated with an automatically managed identity, and authentication tokens persist locally.

Mitigation: Review or clear the workspace data directory after use if you do not want local identity and token material retained.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-outdoor-monitoring-analysis)
- [API documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown or JSON report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Detection findings, risk indications, recommendations, report links, and optional saved report file.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata; bundled frontmatter states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
