## Description:

TinkerClaw LinkedIn lets an agent use a shared LinkedIn browser session to inspect profiles, people search results, companies, connections, inbox conversations, messages, notifications, and feed data, with session storage controls and a gated message-send command.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent gather LinkedIn profile, company, connection, inbox, message, notification, and feed context from an already authenticated browser session. It is suited to research and inbox triage workflows where a human controls session sharing and any outbound message.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires access to an active LinkedIn session, including inbox, connections, feed, and cached profile data.

Mitigation: Install only when that access is acceptable, prefer the default browser transport, and revoke the LinkedIn session when finished.

Risk: Reusable LinkedIn login cookies can grant account access if exposed.

Mitigation: Use OS keychain storage, avoid LINKEDIN_NO_KEYCHAIN and manual cookie handling where possible, and run session logout --purge-data when the skill is no longer needed.

Risk: Automation against LinkedIn may create account restriction or ban risk.

Mitigation: Keep human control over the session and outbound messages, respect the built-in pacing and daily ceilings, and avoid repeated retries after rate-limit or login-challenge errors.

Risk: Cached profile and company data may include third-party personal data.

Mitigation: Disable caching with LINKEDIN_CACHE=0 when local retention is not appropriate and purge cached data with session logout --purge-data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/globalcaos/skills/tinker-linkedin)
- [LinkedIn session management](https://www.linkedin.com/psettings/sessions)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; CLI commands return JSON or text status output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node and a shared LinkedIn browser session; supports Linux and macOS.]

## Skill Version(s):

1.1.0 (source: release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
