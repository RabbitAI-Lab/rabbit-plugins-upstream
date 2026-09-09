## Description:

Open Reddit in the user's Brave browser and take the user to the Reddit homepage.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ruchir17-cmd](https://clawhub.ai/user/ruchir17-cmd)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and end users use this skill when they want an agent to open Reddit in Brave, reuse an existing Reddit tab or browser session when available, and verify that the homepage loaded.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may reuse an existing logged-in Reddit browser session.

Mitigation: Do not enter credentials or make account changes; stop and report that authentication is required if Reddit asks the user to sign in.

Risk: Opening Reddit could expose account-specific content from the user's current browser session.

Mitigation: Limit behavior to opening and verifying the homepage, and avoid posting, commenting, messaging, voting, uploads, purchases, or account-setting changes unless separately requested.

## Reference(s):

- [ClawHub open-reddit skill page](https://clawhub.ai/ruchir17-cmd/skills/open-reddit)
- [Reddit homepage](https://www.reddit.com/)

## Skill Output:

**Output Type(s):** [guidance, shell commands, text]

**Output Format:** [Plain text or Markdown status with browser navigation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reuses an existing Brave session and Reddit tab when available; stops if login is required.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
