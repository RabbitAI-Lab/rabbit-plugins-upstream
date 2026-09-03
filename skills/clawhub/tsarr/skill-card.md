## Description:

Manage home media services through TsArr from OpenClaw. Use for Radarr, Sonarr, Lidarr, Readarr, Prowlarr, Bazarr, qBittorrent, Seerr, and Jellyfin tasks such as checking health, inspecting queues and history, browsing libraries, searching, adding, editing, deleting items, viewing profiles, tags, and root folders, managing torrents, managing media requests, triggering library scans, reading watched state, checking active playback sessions, fixing missing or poor cover images, and checking TsArr configuration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[robbeverhelst](https://clawhub.ai/user/robbeverhelst)

### License/Terms of Use:

MIT-0

## Use Case:

External OpenClaw users and home media administrators use this skill to inspect, configure, and operate TsArr-managed Radarr, Sonarr, Lidarr, Readarr, Prowlarr, Bazarr, qBittorrent, Seerr, and Jellyfin services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide actions that delete media items, delete qBittorrent files, change watched state, control Jellyfin sessions, or approve and decline media requests.

Mitigation: Review commands before approval, inspect current service state before mutations, and avoid non-interactive destructive flags unless the user explicitly requests automation.

Risk: The skill depends on configured API keys and qBittorrent credentials for access to local media services.

Mitigation: Keep service API keys and qBittorrent credentials protected, and review configuration output before sharing it.

## Reference(s):

- [TsArr GitHub repository](https://github.com/robbeverhelst/tsarr)
- [Setup](references/setup.md)
- [Common Workflows](references/common-workflows.md)
- [Service Cheatsheet](references/service-cheatsheet.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON-oriented command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses should show planned commands, summarize results, and call out destructive effects before execution.]

## Skill Version(s):

1.0.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
