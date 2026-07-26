## Description: <br>
Interact with Docker-deployed Xunlei services to submit magnet links, monitor download tasks, and prioritize main content downloads with filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[saaak](https://clawhub.ai/user/saaak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and operators use this skill to configure a connection to their own Xunlei Docker service, submit magnet downloads, and inspect active or completed tasks from an agent workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends magnet links and selected file metadata to the configured Xunlei service and can consume storage and bandwidth. <br>
Mitigation: Submit only content the user is allowed to download, and monitor the configured service for storage and bandwidth impact. <br>
Risk: The bundled config.json contains a concrete host and port that may not match the user's intended Xunlei service. <br>
Mitigation: Review or replace config.json before installation so the skill points only to the user's own service. <br>
Risk: Dependency installation and axios versioning require operator review. <br>
Mitigation: Install dependencies from a trusted registry and consider pinning or updating axios after checking compatibility. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/saaak/skills/docker-xunlei-downloader) <br>
- [cnk3x/xunlei Docker service](https://github.com/cnk3x/xunlei) <br>
- [xunlei-docker-ext reference project](https://github.com/saaak/xunlei-docker-ext) <br>
- [README.md](README.md) <br>
- [CONFIG.md](CONFIG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration] <br>
**Output Format:** [Plain text and Markdown-style command guidance returned by the agent] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may call a configured Xunlei service and return task status, completion summaries, service version, configuration details, or submission results.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
