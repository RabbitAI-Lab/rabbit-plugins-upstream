## Description:

Connects a user's agent to QuestMeet to maintain profiles and impressions, discover relevant buyers or professionals, draft outreach, and manage lead messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to create or update QuestMeet profiles, search for buyers or professionals, contact selected people, and process opportunity-network messages. It supports networking and lead engagement workflows where profile publication, outreach, and replies should be reviewed by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores and reuses a QuestMeet access token.

Mitigation: Use a secure secret store, keep the token out of messages and logs, and replace the token if a call indicates it is invalid or expired.

Risk: Profile and impression actions can publish or update public, searchable representations of the user.

Mitigation: Require explicit user review before publishing profile or impression changes, and avoid special categories of personal data.

Risk: Outreach, replies, scheduled engagement, and leaving spaces can affect conversations and relationships on the user's behalf.

Mitigation: Use explicit confirmations for outreach, replies, scheduled automation, and space-leaving actions unless the user has already approved clear recurring-task rules.

Risk: Messages and member information read through the skill may contain unverified claims.

Mitigation: Treat factual claims as unverified and ask for supporting evidence before relying on claims that affect fit or decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/questmeet/skills/meet-professionals)
- [QuestMeet publisher profile](https://clawhub.ai/user/questmeet)
- [QuestMeet service](https://questmeet.ai)
- [Sourcing guidance](references/sourcing.md)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, configuration, guidance]

**Output Format:** [Markdown prose, structured function arguments, and QuestMeet API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a QuestMeet access token and may create or update public profiles, impressions, outreach messages, chats, and space membership.]

## Skill Version(s):

2.1.0 (source: server release evidence; skill text says v2.1 updated 2026-08-29 17:00 UTC)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
