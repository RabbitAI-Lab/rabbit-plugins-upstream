## Description: <br>
Manage home media services through TsArr from OpenClaw. Use for Radarr, Sonarr, Lidarr, Readarr, Prowlarr, Bazarr, qBittorrent, and Seerr tasks such as checking health, inspecting queues and history, browsing libraries, searching, adding, editing, deleting items, viewing profiles, tags, and root folders, managing torrents, managing media requests, and checking TsArr configuration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[robbeverhelst](https://clawhub.ai/user/robbeverhelst) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and operators use this skill to inspect and manage TsArr-connected home media services, download queues, media requests, and service configuration through guided CLI workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide agents through destructive media-library, request, and torrent actions such as deletes, request approvals, --delete-files, and --yes usage. <br>
Mitigation: Review planned commands before execution, inspect existing items before mutation, and reserve destructive flags or non-interactive confirmation for explicit user requests. <br>
Risk: TsArr configuration may contain service API keys and qBittorrent credentials. <br>
Mitigation: Protect .tsarr.json, ~/.config/tsarr/config.json, environment variables, logs, screenshots, and shared terminals from credential exposure. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/robbeverhelst/skills/tsarr) <br>
- [TsArr homepage](https://github.com/robbeverhelst/tsarr) <br>
- [Setup](references/setup.md) <br>
- [Common Workflows](references/common-workflows.md) <br>
- [Service Cheatsheet](references/service-cheatsheet.md) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown] <br>
**Output Format:** [Markdown with inline bash commands and concise operational summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefers JSON, table, plain, quiet, and selected-field CLI output modes when useful for inspection or parsing.] <br>

## Skill Version(s): <br>
1.0.4 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
