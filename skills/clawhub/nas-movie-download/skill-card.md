## Description: <br>
Search and download movies via Jackett and qBittorrent, with automatic subtitle download support through SMB integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[roger0808](https://clawhub.ai/user/roger0808) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to search torrent indexers, add movie downloads to qBittorrent, and manage subtitle retrieval and upload for NAS-hosted video files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release ships hardcoded credentials and API keys. <br>
Mitigation: Remove bundled credentials before installation, rotate any exposed passwords or API keys, and replace them with least-privilege secrets managed outside the skill artifact. <br>
Risk: The skill can broadly access or modify NAS and qBittorrent content. <br>
Mitigation: Install only in an environment you fully control and review SMB mount, archive/move, qBittorrent delete, and broad subtitle workflows before running them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/roger0808/skills/nas-movie-download) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and configuration values] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May direct the agent to run local scripts that interact with Jackett, qBittorrent, SMB shares, and subtitle providers.] <br>

## Skill Version(s): <br>
3.2.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
