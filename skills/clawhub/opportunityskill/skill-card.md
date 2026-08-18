## Description:

Opportunity Skill lets AI agents connect users with career and business opportunities through QuestMeet profile, discovery, outreach, and lead-engagement workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[questmeet](https://clawhub.ai/user/questmeet)

### License/Terms of Use:

MIT

## Use Case:

External users and their AI agents use this skill to authenticate with QuestMeet, manage profiles and impressions, search for buyers or professionals, prepare outreach, and process opportunity-related messages. It is intended for career and business opportunity matching workflows where the user wants an agent to coordinate profile, discovery, and lead-engagement tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account tokens may be exposed if stored in general agent memory or plaintext workspace files.

Mitigation: Use a secure secret store when available, keep tokens out of user-visible messages, and rotate credentials if exposure is suspected.

Risk: The skill can read messages and perform broad QuestMeet account actions, including profile or impression changes, outreach, invitations, messages, and leaving spaces.

Mitigation: Require explicit user confirmation before sending messages, inviting people, quitting spaces, deleting impressions, changing profiles, or enabling recurring lead tasks.

Risk: Self-update behavior can replace the local skill with code from the upstream repository.

Mitigation: Review the release source, hashes, and security scan evidence before reinstalling or updating the skill.

## Reference(s):

- [Server-resolved source repository](https://github.com/QuestMeet/opportunityskill)
- [ClawHub skill page](https://clawhub.ai/questmeet/skills/opportunityskill)
- [QuestMeet](https://questmeet.ai)
- [README](README.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Guidance, Configuration]

**Output Format:** [Markdown guidance with JSON-like API responses and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update QuestMeet profiles, impressions, messages, spaces, and local token configuration when the user authorizes those workflows.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata); upstream skill docs report v1.7.

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
