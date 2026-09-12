## Description:

Watches family flights and alerts a group chat about takeoff, landing, delays, gate and schedule changes, tight connections, upcoming flights, and follow or mute actions without requiring an API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alfredjbclaw](https://clawhub.ai/user/alfredjbclaw)

### License/Terms of Use:

MIT

## Use Case:

External users and families use this skill to track travel itineraries, manage flight alert subscriptions, and send flight status changes to a group chat. Agents use it to translate user requests into bundled CLI commands and report command results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive travel, mailbox, and chat data.

Mitigation: Review privacy tradeoffs before installation, use a dedicated mailbox and app password, keep mailbox SSL enabled, avoid unrelated secrets in the skill environment, and limit alert recipients to people who should see itinerary details.

Risk: Flight alerts can expose itinerary details such as confirmation codes and seat assignments.

Mitigation: Treat confirmation codes and seat assignments as sensitive, review redaction behavior before broad deployment, and keep chat destinations tightly scoped.

## Reference(s):

- [ClawHub listing for clawflight](https://clawhub.ai/alfredjbclaw/skills/clawflight)
- [Project homepage declared by the skill](https://github.com/alfredjbclaw/clawflight)
- [ADS-B public feed endpoint](https://api.adsb.lol/v2)
- [FAA NAS airport status endpoint](https://nasstatus.faa.gov/api/airport-status-information)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text with CLI commands and optional JSON status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include command results from the bundled clawflight CLI.]

## Skill Version(s):

0.2.1 (source: server release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
