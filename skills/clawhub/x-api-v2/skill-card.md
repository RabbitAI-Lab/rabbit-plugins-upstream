## Description:

Reads X profiles, posts, threads, bookmarks, and likes, searches recent posts, and publishes approved posts through the X API v2.

This skill is ready for commercial/non-commercial use.

## Publisher:

[odrobnik](https://clawhub.ai/user/odrobnik)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents use this skill to find and read X content, review their own bookmarks and likes, and draft posts for explicit approval before publishing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: X credentials and stored sign-in grant access to private account data and posting permissions.

Mitigation: Keep credentials and token files private; use logout or revoke the connected app when access is no longer needed.

Risk: Publishing can expose unintended text on the user's account.

Mitigation: Show the post preview and publish only after the user approves the exact text.

Risk: X API requests may incur charges.

Mitigation: Limit queries to what is needed and set a spending limit in the X Developer Console.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/odrobnik/skills/x-api-v2)
- [Declared project homepage (not verified import provenance)](https://github.com/odrobnik/x-skill)
- [Setup guide](SETUP.md)
- [API pricing guidance](references/pricing.md)
- [X Developer Console](https://developer.x.com/en/portal/projects-and-apps)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Conversational text or structured JSON from X API queries and post previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Posting requires approval of the previewed text; API requests may incur charges.]

## Skill Version(s):

1.1.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
