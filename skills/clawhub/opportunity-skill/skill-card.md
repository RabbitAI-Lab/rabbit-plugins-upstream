## Description:

Opportunity-skill helps an AI agent connect a user with relevant people in QuestMeet's opportunity network by managing profiles and impressions, discovering buyers or professionals, sending outreach, and processing messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users install this skill to help an AI agent represent their opportunity goals, maintain public networking profiles, search for relevant buyers or professionals, send confirmed outreach, and process lead messages. It supports job seeking, recruiting, marketing, pitching, sourcing, and casual networking workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent access-token storage can expose account access if the token is saved in general long-term memory or an unprotected working-directory config file.

Mitigation: Store the access token only in a secure secret store and exclude it from chat messages, profile content, logs, and shared files.

Risk: The skill can remotely store inferred user traits and publish or update user profile content.

Mitigation: Require explicit user confirmation before public profile changes and impression uploads or deletions, and review content for sensitive personal data before submission.

Risk: The skill can read messages, send outreach or replies, run scheduled message processing, and leave spaces.

Mitigation: Require confirmation before outreach, message replies, scheduled message-processing rules, or leaving spaces; treat message claims as unverified until supported by evidence.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/questmeet/skills/opportunity-skill)
- [Job seeking guidance](references/job_seeking.md)
- [Recruiting guidance](references/recruiting.md)
- [Marketing or pitching guidance](references/marketing_or_pitching.md)
- [Sourcing or casual networking guidance](references/sourcing_or_casual_networking.md)
- [QuestMeet](https://questmeet.ai)

## Skill Output:

**Output Type(s):** [text, markdown, API calls, guidance]

**Output Format:** [Markdown and structured function arguments for QuestMeet API calls]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce public profile text, impressions, search queries, outreach proposals, message replies, and account-action recommendations.]

## Skill Version(s):

2.1.7 (source: release evidence and SKILL.md, updated 2026-09-08 05:00 UTC)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
