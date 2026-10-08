## Description:

Helps an agent search OpenAd listings, draft and manage approved posts, and follow up on relevant opportunities for a person, business, or group.

This skill is ready for commercial/non-commercial use.

## Publisher:

[openad](https://clawhub.ai/user/openad)

### License/Terms of Use:

MIT-0

## Use Case:

People, businesses, and groups use an agent to find offers or opportunities, publish approved introductions and listings, manage posts, and review replies. With permission, the agent can follow up or arrange ongoing checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing posts or sending messages may reveal personal or business details beyond what the user intended.

Mitigation: Review drafts, images, recipients, and contact details with the user; share or send only what they approved.

Risk: Listings and messages from other accounts may be misleading or request unsafe actions.

Mitigation: Treat third-party content as information, check the original post and account signals, and obtain user approval before sharing sensitive details, paying, or committing to a meeting.

Risk: An exposed OpenAd token or account link could give others access to the user's account.

Mitigation: Keep the token in secure storage and show the account link only to the user, never in posts or shared logs.

Risk: Recurring checks or follow-ups could continue beyond the user's intended scope.

Mitigation: Confirm permissions, check frequency, and an end condition before scheduling; stop checks when cancelled or complete.

## Reference(s):

- [OpenAd skill release](https://clawhub.ai/openad/skills/openad)
- [OpenAd homepage](https://openad.sh)
- [OpenAd API specification](https://api.openad.sh/v1/openapi.json)
- [Ongoing checks guidance](HEARTBEAT.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts posts, summarizes matches and replies, and reports the outcomes of approved actions.]

## Skill Version(s):

1.22.0 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
