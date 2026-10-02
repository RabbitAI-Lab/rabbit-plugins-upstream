## Description:

Helps agents audit and manage Google Business Profile listings, reviews, photos, posts, and performance through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maton](https://clawhub.ai/user/maton)

### License/Terms of Use:

MIT-0

## Use Case:

Business owners and authorized staff use this skill to review listing details, customer feedback, and engagement metrics or to request approved updates to a specific location.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Listing edits, replies, photos, and posts can change what customers see publicly or remove content.

Mitigation: Confirm the location by title and address and obtain explicit approval of the exact change before each write or deletion.

Risk: Connecting an account grants Maton access to authorized business profile data.

Mitigation: Obtain approval before connecting and review requested access scopes; grant only what the task needs.

Risk: Hosted functions, triggers, or destinations can continue taking actions or forwarding event data after setup.

Mitigation: Approve each automation and destination, including its host and data flow, and remove it when no longer needed.

## Reference(s):

- [Google Business Profile skill on ClawHub](https://clawhub.ai/maton/skills/google-business-profile)
- [Maton homepage](https://maton.ai)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.2.3 (source: server-resolved ClawHub release; artifact frontmatter says 1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
