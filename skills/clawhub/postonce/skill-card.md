## Description:

Publish or schedule social posts, inspect delivery, and manage automatic crossposting through a connected PostOnce MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[niyonx](https://clawhub.ai/user/niyonx)

### License/Terms of Use:

MIT-0

## Use Case:

People managing connected social accounts use this skill to save drafts, publish or schedule posts, check delivery, and configure automatic crossposting through PostOnce.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected API key can authorize publishing, and credentials remain active after removing the skill.

Mitigation: Use a dedicated key with only needed scopes, keep it private, and revoke it or the authorized app separately when no longer needed.

Risk: Published posts and uploaded media can become public, including through recurring crossposting.

Mitigation: Confirm destinations and obtain user approval before publishing or enabling future-content workflows; review post and workflow status afterward.

Risk: Platform limits may silently trim text, hashtags, or extra media.

Mitigation: Check destination capabilities and tailor each post to its platform before submission.

## Reference(s):

- [PostOnce skill on ClawHub](https://clawhub.ai/niyonx/skills/postonce)
- [PostOnce OpenClaw integration](https://postonce.to/integrations/openclaw)
- [PostOnce API documentation](https://docs.postonce.to)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can report draft or post IDs, delivery status by destination, and saved workflow settings.]

## Skill Version(s):

0.2.0 (source: frontmatter and release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
