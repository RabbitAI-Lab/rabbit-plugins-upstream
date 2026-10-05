## Description:

Identifies cat and dog breeds and distinguishes individual pets in images and videos for multi-pet households.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and developers use this skill to analyze pet images or videos, distinguish cats and dogs by breed and individual, and view account-linked analysis reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images or videos, remote media URLs, and an internal user identifier are sent to lifeemergence.com services.

Mitigation: Use only media you are comfortable sharing with the service and review the vendor's data retention and account controls first.

Risk: The skill may silently create or reuse a platform identity and store authentication tokens in a local workspace database.

Mitigation: Review local credential storage and account access controls before use, especially on shared workspaces.

Risk: Account-linked historical reports can be retrieved with limited user control.

Mitigation: Limit access to the workspace and confirm the vendor's report retention and deletion options before analyzing sensitive household footage.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-pet-breed-individual-recognition-analysis)
- [Pet analysis API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Text analysis with report links; Markdown table for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis results can be saved to a local file.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.18)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
