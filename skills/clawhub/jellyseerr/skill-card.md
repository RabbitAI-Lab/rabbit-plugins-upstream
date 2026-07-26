## Description: <br>
Request movies and TV shows through Jellyseerr. Use when the user wants to add media to their Plex/Jellyfin server, search for content availability, or manage media requests. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ericrosenberg](https://clawhub.ai/user/ericrosenberg) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and home media administrators use this skill to search Jellyseerr, submit movie and TV requests, and receive availability notifications for Plex or Jellyfin libraries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores a Jellyseerr API key in the user's local configuration and uses it to submit media requests. <br>
Mitigation: Install only when that local credential storage is acceptable, keep the config file restricted, and rotate the Jellyseerr API key if it is exposed. <br>
Risk: The webhook setup creates a persistent service and an unauthenticated network listener. <br>
Mitigation: Review the service file before enabling it, restrict port 8384 to Jellyseerr or localhost, avoid broad firewall exposure, and consider HTTPS or authentication. <br>
Risk: Persistent notifications can be enabled through either systemd webhooks or cron polling. <br>
Mitigation: Know how to stop and disable the systemd service or remove the cron job before enabling persistent notifications. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/ericrosenberg/skills/jellyseerr) <br>
- [Jellyseerr Webhook Setup Guide](references/WEBHOOK_SETUP.md) <br>
- [Jellyseerr API Reference](references/api.md) <br>
- [Jellyseerr Project](https://github.com/Fallenbagel/jellyseerr) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, JSON configuration examples, and Python or shell script execution steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate or update local Jellyseerr configuration, request-tracking cache files, notification queue files, cron entries, and systemd service configuration when the user runs the provided scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
