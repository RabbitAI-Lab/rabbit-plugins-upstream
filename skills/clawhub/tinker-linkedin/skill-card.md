## Description:

Tinker LinkedIn lets an agent use a user-shared LinkedIn browser tab to read profiles, search results, connections, inbox, and feed content, with message sending gated by per-action consent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, external users, and developers can use this skill for LinkedIn research, inbox triage, and controlled drafting or sending of messages through an existing browser session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A legacy LinkedIn session from an older version may be password-equivalent, and the security evidence reports that one status path may read such a legacy secret into memory.

Mitigation: Review before installing if an older version was used; prefer a version or workflow that checks or deletes legacy credentials without reading their value, and revoke old LinkedIn sessions when needed.

Risk: LinkedIn automation may create account, policy, or service-risk exposure if run aggressively or without user oversight.

Mitigation: Keep a human in the loop, stay within the documented daily ceilings and fixed pacing, and stop rather than retrying if LinkedIn returns 429 responses or challenges.

Risk: Message sending is a write action on the user's LinkedIn account.

Mitigation: Require per-action consent that repeats the exact conversation URN; without matching consent, return the message as a draft instead of sending it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-linkedin)
- [Publisher profile](https://clawhub.ai/user/globalcaos)
- [LinkedIn session settings](https://www.linkedin.com/psettings/sessions)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown and CLI-oriented text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce profile, company, search, inbox, feed, activity, and draft message information from the shared LinkedIn tab.]

## Skill Version(s):

1.2.1 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
