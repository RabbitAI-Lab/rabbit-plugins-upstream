## Description:

Analyzes pet photos and videos for body-condition and visible health concerns, then provides a report or retrieves prior reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners use the skill to review photos or videos for potential body-condition, skin, injury, or activity concerns and access previous analysis reports. Results are for reference and do not replace veterinary diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet photos, videos, or URLs are sent to the LifeEmergence cloud service and may contain sensitive household footage.

Mitigation: Obtain consent before sending media; avoid sensitive footage until the publisher clarifies retention and consent practices.

Risk: The skill can silently create or reuse a cloud-linked identity and retrieve associated report history.

Mitigation: Confirm the user's intent before accessing history and clarify account separation with the publisher before shared use.

Risk: Service tokens are stored in a local workspace SQLite database.

Mitigation: Restrict access to the workspace and confirm token storage controls with the publisher before installation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-body-health-analysis)
- [Pet health analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis report or Markdown history table, with optional JSON file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include assessment details, suggestions, and report links]

## Skill Version(s):

1.0.17 (source: ClawHub release metadata; bundled frontmatter says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
