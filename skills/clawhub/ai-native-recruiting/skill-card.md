## Description:

AI-Native Recruiting helps an agent use QuestMeet to represent a user, manage recruiting profiles and impressions, discover relevant people, conduct outreach, and process lead engagement messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and recruiting teams use this skill to connect an agent to QuestMeet for candidate discovery, profile and impression management, outreach, and follow-up message handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores reusable account tokens in generic memory or local files.

Mitigation: Use a protected credential store or restricted local configuration, and never include the access token in messages or shared outputs.

Risk: The skill can change profiles, impressions, outreach, messages, and spaces on the user's behalf.

Mitigation: Require explicit user confirmation before profile edits, impression deletion, outreach, message posting, or leaving spaces.

Risk: Profile, search, outreach, and message data is sent to QuestMeet.

Mitigation: Install only when the user accepts that data flow, and avoid submitting special categories of personal data.

Risk: Recurring scheduled-task rules may allow repeated discovery or lead-engagement actions.

Mitigation: Review schedule rules carefully and keep mutating actions subject to clear authorization boundaries.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/questmeet/skills/ai-native-recruiting)
- [Recruiting Reference](references/recruiting.md)
- [QuestMeet](https://questmeet.ai)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown and text guidance, with structured results from QuestMeet API calls.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update profiles, impressions, outreach messages, chat messages, spaces, and scheduled-task guidance when the user authorizes those actions.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
