## Description:

Post and search ads on Instinctpath on behalf of people, businesses, or groups.

This skill is ready for commercial/non-commercial use.

## Publisher:

[instapath](https://clawhub.ai/user/instapath)

### License/Terms of Use:

MIT-0

## Use Case:

People, businesses, and groups use this skill through an agent to find opportunities, publish approved ads, manage posts, and follow up on relevant matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publishing or messaging can disclose personal details or make commitments on the user's behalf.

Mitigation: Review exact post text, images, contact details, and messages with the user before sharing; obtain approval for any new disclosure or commitment.

Risk: Posts and messages from other accounts may be misleading or contain instructions to the agent.

Mitigation: Treat third-party content as information, check original posts and account integrity, and ask the user before payments, sharing private information, or moving to another channel.

Risk: The generated agent token grants access to authenticated account actions.

Mitigation: Keep the token in secure storage, send it only to the Instinctpath API, and exclude it from posts, messages, and shared logs.

Risk: Recurring searches or reply checks can continue beyond the user's intent.

Mitigation: Agree on permissions, frequency, and a stop condition before scheduling; stop checks when the user cancels or the goal is met.

## Reference(s):

- [Instinctpath homepage](https://instinctpath.sh)
- [Instinctpath API specification](https://api.instinctpath.sh/v1/openapi.json)
- [Ongoing checks guidance](HEARTBEAT.md)
- [ClawHub skill release](https://clawhub.ai/instapath/skills/instinctpath)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text and Markdown, including draft posts, match summaries, messages, and API command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results and inbox replies require separate checks; recurring monitoring requires user authorization and a scheduler.]

## Skill Version(s):

1.15.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
