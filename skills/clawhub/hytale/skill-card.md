## Description: <br>
Manage and control a local Hytale dedicated server with commands to start, stop, update, and check server status using the official downloader. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[newcastlegeek](https://clawhub.ai/user/newcastlegeek) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and server operators use this skill to manage a local Hytale dedicated server, including starting, stopping, updating, and checking the server status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs a local Hytale downloader binary and server process from ~/hytale_server. <br>
Mitigation: Install only when intending to run a local Hytale server, obtain the downloader from the official source, and review commands before execution. <br>
Risk: hytale-downloader-credentials.json may contain sensitive credentials. <br>
Mitigation: Keep ~/hytale_server private, avoid committing or syncing the credentials file, and use restrictive file permissions. <br>


## Reference(s): <br>
- [Hytale Downloader](https://downloader.hytale.com/hytale-downloader.zip) <br>
- [ClawHub Skill Page](https://clawhub.ai/newcastlegeek/skills/hytale) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires local Java, screen, the Hytale downloader binary, and hytale-downloader-credentials.json in ~/hytale_server.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
