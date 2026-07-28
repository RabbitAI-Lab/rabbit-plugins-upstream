## Description: <br>
planesnitch is a self-hosted aircraft monitor that helps an agent guide users through Docker-based setup for location-based ADS-B aircraft alerts, Telegram notifications, webhooks, watchlists, and related configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and operators use this skill to configure and run planesnitch for aircraft monitoring near chosen locations, including military, government, police, emergency squawk, custom ICAO, type, proximity, and all-aircraft watchlists. The skill is also useful for routing aircraft alerts into Telegram or trusted webhook endpoints. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: config.yaml can contain Telegram bot tokens, webhook URLs, auth headers, and watched location coordinates. <br>
Mitigation: Treat config.yaml as sensitive, avoid committing or sharing it, and mount it read-only as documented. <br>
Risk: Location coordinates and aircraft tracking data are sent to configured ADS-B sources and notification targets. <br>
Mitigation: Use only trusted ADS-B sources, Telegram chats, and webhook endpoints; use a self-hosted ultrafeeder when public ADS-B polling is not appropriate. <br>
Risk: Webhook notifications send alert payloads to arbitrary configured URLs. <br>
Mitigation: Vet webhook URLs and authentication headers before adding them to notifications. <br>


## Reference(s): <br>
- [planesnitch setup](references/setup.md) <br>
- [planesnitch ClawHub page](https://clawhub.ai/psyb0t/skills/planesnitch) <br>
- [planesnitch source homepage](https://github.com/psyb0t/docker-planesnitch) <br>
- [plane-alert-db aircraft watchlists](https://github.com/sdr-enthusiasts/plane-alert-db) <br>
- [ICAO Doc 8643 aircraft type designators](https://www.icao.int/publications/DOC8643/Pages/Search.aspx) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May reference Docker, config.yaml, CSV watchlists, Telegram setup, and webhook JSON behavior.] <br>

## Skill Version(s): <br>
1.8.5 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
