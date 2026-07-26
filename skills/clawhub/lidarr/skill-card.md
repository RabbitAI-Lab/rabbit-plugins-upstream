## Description: <br>
Search and add music to Lidarr. Supports artists, albums, and quality profiles (FLAC preferred). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rappo](https://clawhub.ai/user/rappo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent search Lidarr, add artists or albums, monitor releases, refresh metadata, and manage a music library through an existing Lidarr server. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can modify a Lidarr media library by adding artists, monitoring albums, refreshing metadata, and removing artists. <br>
Mitigation: Require clear user confirmation before running add, monitor, refresh, or remove commands. <br>
Risk: The remove command can delete media files when called with --delete-files. <br>
Mitigation: Treat delete-file operations as destructive and require explicit confirmation that names the target artist and delete-files option. <br>
Risk: The skill uses a Lidarr API key stored in a local config file. <br>
Mitigation: Keep the config file private and verify the Lidarr URL before allowing the agent to run commands. <br>


## Reference(s): <br>
- [ClawHub Lidarr Skill](https://clawhub.ai/rappo/skills/lidarr) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, configuration] <br>
**Output Format:** [Plain text and JSON emitted by shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and jq plus a private Lidarr URL and API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
