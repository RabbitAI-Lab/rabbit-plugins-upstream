## Description: <br>
Self-hosted aircraft monitor that watches configured locations for matching aircraft, emergency squawks, custom ICAO lists, low-flying aircraft, or all aircraft using public ADS-B APIs or a self-hosted ultrafeeder, then sends alerts to Telegram or webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to configure and run a Docker-based aircraft alerting service for locations they care about. It is suited for proximity alerts, emergency-squawk monitoring, ICAO watchlists, CSV-based watchlists, and webhook or Telegram delivery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured location coordinates and matched aircraft data leave the host when polling ADS-B sources and sending alerts to Telegram or webhook targets. <br>
Mitigation: Use a trusted ADS-B source or a self-hosted ultrafeeder when location privacy matters, and configure only Telegram chats, bots, and webhook endpoints you control or explicitly trust. <br>
Risk: config.yaml can contain Telegram bot tokens, webhook URLs, and authorization headers in plaintext. <br>
Mitigation: Keep config.yaml private, do not commit or paste it into shared channels, and mount it read-only as documented. <br>
Risk: Webhook delivery posts aircraft and location alert payloads to arbitrary configured URLs. <br>
Mitigation: Vet webhook URLs before adding them and include notification targets in the deployment threat model. <br>


## Reference(s): <br>
- [Setup guide](references/setup.md) <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/planesnitch) <br>
- [Project homepage](https://github.com/psyb0t/docker-planesnitch) <br>
- [plane-alert-db CSV watchlists](https://github.com/sdr-enthusiasts/plane-alert-db) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with YAML configuration examples and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Docker and a local config.yaml; alert delivery depends on the configured ADS-B source, Telegram target, or webhook endpoint.] <br>

## Skill Version(s): <br>
1.8.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
