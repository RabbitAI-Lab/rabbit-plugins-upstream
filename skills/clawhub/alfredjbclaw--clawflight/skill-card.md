## Description:

Track and follow family flights, alert a group chat or ntfy on takeoff, landing, delays, schedule changes and tight connections; mute alerts, run diagnostic audits of stored data and system health.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alfredjbclaw](https://clawhub.ai/user/alfredjbclaw)

### License/Terms of Use:

MIT

## Use Case:

External users and household organizers use this skill through an agent to manage family flight tracking, configure recipients, run diagnostics, and receive alerts about takeoff, landing, delays, schedule changes, cancellations, and tight connections.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores family itinerary details, traveler records, recipient channel targets, confirmation codes, and queued alert text locally.

Mitigation: Install only when local storage of this travel data is acceptable, use the configured state directory deliberately, and delete the state directory and any separate config file when removing the skill.

Risk: Alert text can include traveler names and confirmation codes and is sent to configured recipients or notification services.

Mitigation: Configure only trusted recipients and channels, review notification targets before enabling unattended jobs, and avoid posting secrets in chat.

Risk: Optional mail ingestion reads forwarded itinerary email from a configured mailbox.

Mitigation: Use a dedicated forwarding mailbox, restrict trusted senders to addresses you control, and store mailbox credentials in environment variables.

Risk: Setup can create cron jobs that run the bundled CLI unattended.

Mitigation: Review the cron commands printed by setup before applying them and use doctor to verify configuration and state paths.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alfredjbclaw/skills/clawflight)
- [ntfy](https://ntfy.sh)
- [ADS-B public feed](https://api.adsb.lol/v2)
- [FAA NAS airport status API](https://nasstatus.faa.gov/api/airport-status-information)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions, Markdown, Text]

**Output Format:** [Markdown with inline shell commands and concise status summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May request clarification before muting, removing, or following a flight when the flight or recipient is ambiguous.]

## Skill Version(s):

0.3.3 (source: frontmatter and package __version__)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
