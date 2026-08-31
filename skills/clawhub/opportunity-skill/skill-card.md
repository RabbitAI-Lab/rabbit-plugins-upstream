## Description:

Connects an AI agent to QuestMeet's opportunity network to help users manage profiles and impressions, find buyers or professionals, send outreach, and process networking messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT-0

## Use Case:

External users install this skill to let an agent support opportunity networking workflows, including profile creation, candidate or buyer discovery, outreach drafting, and message triage. It is aimed at job seekers, recruiters, entrepreneurs, freelancers, buyers, and professionals who use QuestMeet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can store QuestMeet access tokens and use them for account-level networking automation.

Mitigation: Require explicit user consent before storing credentials, and prefer a secure secret store over memory or plaintext configuration files.

Risk: The skill can create public profiles and impressions that may expose user information.

Mitigation: Review profile and impression content with the user before submission, and exclude special categories of personal data.

Risk: The skill can read messages, send outreach, create chats, invite contacts, or quit spaces.

Mitigation: Require explicit confirmation for each high-impact networking or messaging action unless the user has approved precise scheduled-task rules.

Risk: The artifact asks agents to check for newer versions and reinstall the skill.

Mitigation: Treat self-update or reinstall steps as user-approved maintenance actions rather than automatic behavior.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/questmeet/skills/opportunity-skill)
- [QuestMeet publisher profile](https://clawhub.ai/user/questmeet)
- [QuestMeet service](https://questmeet.ai)
- [Job Seeking Reference](artifact/references/job_seeking.md)
- [Recruiting Reference](artifact/references/recruiting.md)
- [Marketing Or Pitching Reference](artifact/references/marketing_or_pitching.md)
- [Sourcing Reference](artifact/references/sourcing.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Text, API calls, Configuration]

**Output Format:** [Markdown and structured text with QuestMeet account actions and API call results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update public profiles, impressions, outreach messages, chats, and spaces after user confirmation.]

## Skill Version(s):

2.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
