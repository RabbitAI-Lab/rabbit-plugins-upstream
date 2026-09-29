## Description:

Helps agents retrieve and analyze Fireflies meeting transcripts, summaries, contacts, and recordings through a Maton-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users can find and analyze meeting conversations, retrieve transcripts and summaries, and manage recordings in an authorized Fireflies account. Maton also supports user-approved automations using that connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Meeting transcripts and cross-meeting searches can expose sensitive personal or business information.

Mitigation: Limit queries to the needed meetings and fields, and avoid retaining or sharing raw responses without approval.

Risk: An unintended account or broad connection can access more meetings than the user expects.

Mitigation: Confirm the Fireflies account and connection, request only needed access, and prefer OAuth to raw API keys.

Risk: Writes, deletions, hosted functions, triggers, and webhooks may change data or create persistent automations.

Mitigation: Require separate explicit approval for each action, its target, and its intended effects.

## Reference(s):

- [ClawHub release](https://clawhub.ai/byungkyu/skills/fireflies-api)
- [Fireflies API documentation](https://docs.fireflies.ai/)
- [Fireflies GraphQL API reference](https://docs.fireflies.ai/graphql-api)
- [Maton](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with commands, code examples, and meeting analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May contain sensitive meeting content; return only the fields needed for the task.]

## Skill Version(s):

1.2.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
