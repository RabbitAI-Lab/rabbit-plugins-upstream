## Description: <br>
planesnitch helps users configure and run a Docker-based aircraft monitor that polls ADS-B sources and sends location-based aircraft alerts to Telegram or webhooks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psyb0t](https://clawhub.ai/user/psyb0t) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and aircraft monitoring enthusiasts use this skill to set up a self-hosted watch-and-alert workflow for configured locations, aircraft watchlists, emergency squawks, and webhook or Telegram notifications. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Configured locations, aircraft positions, squawks, registrations, and optional aircraft images may be sent to public ADS-B APIs, Telegram, or configured webhook endpoints. <br>
Mitigation: Use a trusted self-hosted ultrafeeder when location privacy matters, and configure only Telegram chats or webhook URLs you control or explicitly trust. <br>
Risk: config.yaml can contain Telegram bot tokens, webhook URLs, and authorization headers in plaintext. <br>
Mitigation: Keep config.yaml private, do not commit or paste it into shared channels, and mount it read-only where possible. <br>
Risk: The workflow relies on a Docker image and optional downloaded CSV/config files. <br>
Mitigation: Review the Docker image and downloaded files before use, and refresh watchlist CSVs from trusted sources. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/psyb0t/skills/planesnitch) <br>
- [Setup guide](references/setup.md) <br>
- [Project homepage](https://github.com/psyb0t/docker-planesnitch) <br>
- [plane-alert-db CSV watchlists](https://github.com/sdr-enthusiasts/plane-alert-db) <br>
- [ICAO Doc 8643 aircraft type designators](https://www.icao.int/publications/DOC8643/Pages/Search.aspx) <br>
- [doc8643 aircraft type image reference](https://doc8643.com) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with YAML and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces setup and configuration guidance for Docker, config.yaml, Telegram alerts, webhooks, CSV watchlists, and local cache volumes.] <br>

## Skill Version(s): <br>
1.8.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
