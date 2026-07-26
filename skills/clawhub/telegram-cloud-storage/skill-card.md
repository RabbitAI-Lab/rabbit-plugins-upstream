## Description: <br>
A high-performance Telegram Cloud Storage solution using Teldrive that turns Telegram into an unlimited cloud drive with a local API/UI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oki3505f](https://clawhub.ai/user/oki3505f) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to install, configure, run, and operate a local Teldrive service that exposes Telegram-backed storage through a web UI, REST API, and Python client for file operations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The install flow downloads and prepares a Teldrive binary from an upstream GitHub release. <br>
Mitigation: Install only if the upstream tgdrive/teldrive release source is trusted, and review the downloaded binary source before running it. <br>
Risk: The skill handles Telegram app credentials, database credentials, JWT secrets, tokens, and session data. <br>
Mitigation: Keep config.toml, token.txt, TELDRIVE_TOKEN, TELDRIVE_SESSION_HASH, database credentials, and Telegram session data private. <br>
Risk: The client can upload, rename, or delete remote files through the local Teldrive API. <br>
Mitigation: Require explicit user approval before an agent performs modifying file operations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/oki3505f/skills/telegram-cloud-storage) <br>
- [Publisher profile](https://clawhub.ai/user/oki3505f) <br>
- [Teldrive project](https://github.com/tgdrive/teldrive) <br>
- [Teldrive 1.8.0 Linux AMD64 release archive](https://github.com/tgdrive/teldrive/releases/download/1.8.0/teldrive-1.8.0-linux-amd64.tar.gz) <br>
- [Telegram API credentials](https://my.telegram.org) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands, Python client commands, and configuration details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The Python client may return JSON responses from the local Teldrive API and may write downloaded files to local paths.] <br>

## Skill Version(s): <br>
1.8.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
