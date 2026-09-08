## Description:

Tinker LinkedIn lets an agent use a user-shared LinkedIn browser session to crawl profiles, people search, companies, connections, inbox, feed, notifications, and selected messages through a zero-dependency Node CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[globalcaos](https://clawhub.ai/user/globalcaos)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect LinkedIn identity, profiles, companies, connections, inbox, messages, feed, posts, notifications, and activity counters from an existing signed-in browser session. It is suited to controlled research and inbox triage workflows where the user accepts account-level LinkedIn access and automation risk.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles LinkedIn session cookies that are equivalent to account login access.

Mitigation: Use the default browser transport when possible, avoid storing cookies unless necessary, keep session data in the OS keychain, and run session logout plus LinkedIn session revocation when finished.

Risk: Automation can expose private account data and may affect the user's LinkedIn account standing.

Mitigation: Review each intended workflow before execution, keep pacing enabled, respect the built-in daily ceilings, and avoid unattended bulk profile crawling or messaging.

Risk: Crawled third-party profile or company data can be retained locally.

Mitigation: Disable caching with LINKEDIN_CACHE=0 when retention is not acceptable, or use session logout --purge-data to remove cached profiles and activity counters.

Risk: Configurable relay endpoints could send browser-session activity outside the intended local relay if changed.

Mitigation: Keep LINKEDIN_CDP_URL and LINKEDIN_RELAY_HTTP pointed at loopback endpoints and review environment overrides before running the CLI.

Risk: The skill can send LinkedIn messages when explicitly confirmed.

Mitigation: Require a human-approved message and conversation target before using message-send with --i-mean-it.

## Reference(s):

- [Tinker LinkedIn on ClawHub](https://clawhub.ai/globalcaos/skills/linkedin-hack)
- [Publisher profile: globalcaos](https://clawhub.ai/user/globalcaos)
- [LinkedIn session revocation settings](https://www.linkedin.com/psettings/sessions)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-like CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may reflect live LinkedIn account data and cached profile or company data; message sending is gated by an explicit confirmation flag.]

## Skill Version(s):

1.1.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
