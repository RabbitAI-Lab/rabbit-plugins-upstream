## Description:

Helps an agent write, create, check, preview, and schedule LinkedIn posts for personal profiles and company Pages using the user's own material and voice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[social-media-skills](https://clawhub.ai/user/social-media-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and teams use the skill to turn their own experience and source material into LinkedIn posts and media, check content against platform constraints, preview it, and schedule approved posts for personal profiles or company Pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security guidance reports private-network request and unclear tool-scope concerns.

Mitigation: Review the requested tools and network behavior before connecting accounts, and proceed only when the access scope is acceptable.

Risk: Drafts and media may be transferred to WoopSocial before a post is scheduled.

Mitigation: Connect only when ready to share the relevant material, and review drafts and media before sending or scheduling them.

Risk: File cleanup may affect existing data.

Mitigation: Keep backups and review target paths before running cleanup operations.

Risk: Security guidance recommends reviewing how API keys are handled.

Mitigation: Check the key handling and required tools before connecting, and use only credentials appropriate for the approved account scope.

## Reference(s):

- [LinkedIn Skill release](https://clawhub.ai/social-media-skills/skills/linkedin-skill)
- [WoopSocial LinkedIn MCP](https://woopsocial.com/social-media-mcp/linkedin-mcp?utm_source=linkedin-skill&utm_medium=skill)
- [LinkedIn platform specifications](references/linkedin-specs.md)
- [Writing guidance](references/writing.md)
- [Plan format](references/plan-json.md)
- [WoopSocial setup and scheduling guidance](references/woopsocial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON configuration, Shell commands, Images, Video]

**Output Format:** [Markdown drafts, JSON plans and requests, shell commands, and media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and media are based on user-provided material; scheduling requires the user's approval.]

## Skill Version(s):

1.0.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
