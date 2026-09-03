## Description:

Opportunity Skill lets an AI agent help users manage QuestMeet networking workflows for user representation, profile and impression management, people discovery, outreach, and lead engagement.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to find and contact employers, clients, customers, investors, candidates, freelancers, entrepreneurs, or event contacts through QuestMeet. The skill also helps maintain profiles, impressions, proposals, and messages that support those opportunity matches.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for durable QuestMeet access-token storage.

Mitigation: Use secure token storage, never expose tokens in messages, and rotate the token if it may have been disclosed.

Risk: Profiles created or updated through the skill may become publicly accessible and search-indexed.

Mitigation: Review profile content before publication, omit sensitive or special-category personal data, and confirm that the user intends the profile to be public.

Risk: Outreach, invitations, message replies, and space changes can affect real networking relationships.

Mitigation: Require explicit user approval before sending proposals, creating messages, inviting people, or leaving spaces unless the user has approved clear recurring-task rules.

Risk: The authenticity of received messages and member information cannot be guaranteed.

Mitigation: Treat claims as unverified and ask for supporting evidence when achievements, qualifications, or offers materially affect a decision.

Risk: The security summary flags automatic self-update behavior for user review.

Mitigation: Approve skill updates intentionally and review the new release evidence before installing a newer version.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/questmeet/skills/opportunity-skill)
- [QuestMeet](https://questmeet.ai)
- [Job Seeking Reference](references/job_seeking.md)
- [Recruiting Reference](references/recruiting.md)
- [Marketing Or Pitching Reference](references/marketing_or_pitching.md)
- [Sourcing Or Casual Networking Reference](references/sourcing_or_casual_networking.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API calls, Configuration, Guidance]

**Output Format:** [Markdown guidance, structured function arguments, and QuestMeet API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use QuestMeet account state, user profiles, impressions, messages, and locally or memory-stored access tokens.]

## Skill Version(s):

2.1.5 (source: server release metadata and SKILL.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
