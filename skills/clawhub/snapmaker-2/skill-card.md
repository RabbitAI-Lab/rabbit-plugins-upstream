## Description: <br>
Control and monitor Snapmaker 2.0 3D printers via their HTTP API for status checks, job management, progress watching, and event monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to let an agent discover, monitor, upload jobs to, and control a Snapmaker 2.0 printer on a local network. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can affect physical printer hardware through local-network file upload and start, pause, resume, or stop actions. <br>
Mitigation: Require explicit user approval before state-changing actions and verify the printer, file, and current job state before execution. <br>
Risk: The documented confirmation safeguards do not match the current script behavior for pause, resume, and stop commands. <br>
Mitigation: Review safety behavior before deployment and avoid unattended state-changing commands until confirmations are verified or added. <br>
Risk: The printer token is stored in config.json and grants local API access. <br>
Mitigation: Treat config.json as a secret, keep it out of shared repositories and logs, and restrict it to trusted workspaces. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/odrobnik/skills/snapmaker-2) <br>
- [Snapmaker 2.0 HTTP API Notes](references/API_NOTES.md) <br>
- [Snapmaker Forum API Documentation](https://forum.snapmaker.com/t/documentation-of-the-web-api/20976) <br>
- [Snapmaker Forum Auto-start Guide](https://forum.snapmaker.com/t/guide-automatic-start-via-drag-drop/29177) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may produce JSON status or discovery output when run with --json.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
