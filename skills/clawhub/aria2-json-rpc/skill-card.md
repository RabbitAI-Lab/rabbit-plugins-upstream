## Description: <br>
Interact with aria2 download manager via JSON-RPC 2.0. Manage downloads, query status, and control tasks through natural language commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[azzgo](https://clawhub.ai/user/azzgo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, operators, and external users use this skill to let an agent manage an aria2 download manager, including starting downloads, checking status, pausing or resuming tasks, and adjusting aria2 options through provided Python scripts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can start, stop, monitor, remove, purge, and reconfigure downloads in a user's aria2 instance. <br>
Mitigation: Require confirmation before destructive or broad actions such as remove, purge, pause-all, resume-all, or global option changes. <br>
Risk: An exposed or weakly protected aria2 RPC endpoint could allow unintended control of downloads. <br>
Mitigation: Keep the RPC secret private and prefer localhost or TLS-protected remote RPC connections. <br>
Risk: Downloads from unreviewed URLs, torrents, or metalink files may introduce unwanted content or operational risk. <br>
Mitigation: Review URLs and torrent or metalink files before adding them to aria2. <br>


## Reference(s): <br>
- [Aria2 RPC Methods Reference](references/aria2-methods.md) <br>
- [Execution Guide](references/execution-guide.md) <br>
- [Troubleshooting](references/troubleshooting.md) <br>
- [Configuration Guide](CONFIG.md) <br>
- [aria2 official documentation](https://aria2.github.io/) <br>
- [ClawHub skill page](https://clawhub.ai/azzgo/skills/aria2-json-rpc) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON-RPC result summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute Python helper scripts that call a configured aria2 JSON-RPC endpoint.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter reports 1.1.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
