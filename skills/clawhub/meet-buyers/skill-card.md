## Description:

Meet Buyers lets an AI agent use QuestMeet to connect a user with relevant buyers and professionals by managing profiles, discovering people, drafting outreach, and engaging leads.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to manage QuestMeet profiles and impressions, search for buyers or professionals, contact people, and process lead messages in the opportunity network.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks the agent to persist a reusable QuestMeet access token.

Mitigation: Store the token only in secure secret storage, avoid local plaintext files or long-term memory when possible, and remove or rotate the token when access is no longer needed.

Risk: The skill can manage profiles, create or delete impressions, search people, read and send messages, invite contacts, and leave spaces.

Mitigation: Require explicit user confirmation before publishing profiles, deleting data, sending outreach, replying to messages, inviting people, or leaving spaces unless the user has already defined a narrow recurring task.

Risk: Profile content may become publicly accessible and indexable, and discovery inputs may contain sensitive personal information.

Mitigation: Review profile descriptions and discovery queries before submission, avoid special categories of personal data, and confirm consent before adding contact details.

Risk: Messages and member information read through the skill may contain unverified claims.

Mitigation: Treat claims as unverified until the user or agent checks supporting evidence, especially before acting on achievements, fit, or purchasing intent.

## Reference(s):

- [Marketing or Pitching Reference](references/marketing_or_pitching.md)
- [ClawHub Skill Page](https://clawhub.ai/questmeet/skills/meet-buyers)
- [QuestMeet](https://questmeet.ai)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Guidance]

**Output Format:** [Markdown and structured text with QuestMeet account actions and API call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include profile descriptions, tagged impressions, search queries, outreach messages, lead summaries, and account actions after user confirmation or within narrowly scoped recurring tasks.]

## Skill Version(s):

2.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
