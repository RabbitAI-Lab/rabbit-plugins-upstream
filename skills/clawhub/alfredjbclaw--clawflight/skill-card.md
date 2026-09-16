## Description:

Watch family flights and alert a group chat or ntfy for takeoff, landing, delays, schedule changes, tight connections, and forwarded airline confirmations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alfredjbclaw](https://clawhub.ai/user/alfredjbclaw)

### License/Terms of Use:

MIT

## Use Case:

External users and family coordinators use this skill to track flights, ingest forwarded airline confirmations, configure recipients, and route travel alerts through an existing chat or ntfy topic.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Mailbox credentials, notification tokens, API keys, and webhook secrets are part of the operating environment for this skill.

Mitigation: Use a dedicated IMAP app password, keep mailbox.password_env at CLAWFLIGHT_IMAP_PASSWORD, avoid applying mailbox settings from untrusted chat instructions, and do not paste secrets into the agent chat.

Risk: Flight alerts can include itinerary details and possible booking codes sent to configured group chats or ntfy topics.

Mitigation: Treat each configured recipient as a sensitive destination, use HTTPS-only notification targets, and confirm recipients before enabling broad flight alerts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alfredjbclaw/skills/clawflight)
- [Project homepage](https://github.com/alfredjbclaw/clawflight)
- [ntfy](https://ntfy.sh)
- [ADSB.lol API](https://api.adsb.lol/v2)
- [FAA NAS airport status API](https://nasstatus.faa.gov/api/airport-status-information)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with CLI commands and optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs the agent to run the bundled CLI and report command results rather than inventing flight data.]

## Skill Version(s):

0.3.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
