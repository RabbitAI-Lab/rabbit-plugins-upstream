## Description:

Open to Work helps an AI agent authenticate to QuestMeet, maintain user profiles and impressions, discover relevant employers or professionals, send outreach, and process opportunity-network messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users install this skill to let an AI agent help with job seeking and professional networking on QuestMeet, including profile preparation, employer or professional discovery, outreach drafting, and lead engagement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access a QuestMeet account and asks agents to retain an authentication token.

Mitigation: Use session-only or secure local token storage when possible, keep tokens out of messages, and reauthenticate rather than exposing a token during troubleshooting.

Risk: Profile and impression updates can expose personal information and may create public, indexable profile pages.

Mitigation: Ask the user to review profile content before submission, avoid special categories of personal data, and require explicit consent before adding contact details.

Risk: The skill can send outreach, create messages, quit spaces, and operate under scheduled message-handling rules.

Mitigation: Require explicit confirmation before sending, deleting, quitting, or updating public-facing content unless the user has already approved precise recurring-task rules.

Risk: Messages and member information read through the network may contain unverified claims.

Mitigation: Treat factual claims as unverified and prompt the user to request supporting evidence before relying on them for outreach or opportunity decisions.

## Reference(s):

- [Open to Work ClawHub listing](https://clawhub.ai/questmeet/skills/open-to-work)
- [QuestMeet](https://questmeet.ai)
- [Job Seeking Instructions](references/job_seeking.md)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Markdown, Text, Configuration]

**Output Format:** [Markdown guidance with structured function-call arguments and text messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Calls QuestMeet GraphQL functions with a user access token; generated profile content may become public and indexable when submitted.]

## Skill Version(s):

2.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
