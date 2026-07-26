## Description: <br>
Add and manage movies in a Radarr instance via its HTTP API, including movie lookup, quality profile and root folder selection, movie requests by title/year or TMDB ID, and search triggering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vishalchaudhary](https://clawhub.ai/user/vishalchaudhary) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users, operators, and home media administrators use this skill to request movies from chat, add them to Radarr, resolve required Radarr profile/root choices, and receive progress updates. Optional integrations enrich requests with TMDB, OMDb, and Plex metadata when those credentials are configured. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to a Radarr API key and can optionally use TMDB, OMDb, and Plex credentials. <br>
Mitigation: Install only when those services should be accessible to the agent, store credentials in the configured environment file, and limit credential scope where the upstream services allow it. <br>
Risk: Progress notifications are queued for chat targets stored in local tracking files. <br>
Mitigation: Review the outbox and cron sender configuration so updates are sent only to intended chats, and restrict group usage to trusted users through OpenClaw allowlists. <br>
Risk: The asset fetch helper can download from arbitrary URLs to arbitrary writable output paths. <br>
Mitigation: Constrain or harden asset download inputs before high-trust deployment, and review requested URLs and output locations before execution. <br>


## Reference(s): <br>
- [Radarr+ ClawHub listing](https://clawhub.ai/vishalchaudhary/skills/radarr-plus) <br>
- [Radarr+ Onboarding](references/onboarding.md) <br>
- [Radarr+ Setup & Configuration](references/setup.md) <br>
- [Radarr API quick notes](references/radarr-api-notes.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payloads] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create local Radarr tracking and outbox JSON files, and may download poster assets when optional metadata features are used.] <br>

## Skill Version(s): <br>
0.1.7 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
