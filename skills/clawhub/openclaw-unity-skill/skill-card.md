## Description: <br>
Control Unity Editor via OpenClaw Unity Plugin for scene management, GameObject and Component manipulation, debugging, input simulation, Play mode control, package operations, tests, and explicit C# execution in trusted local projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomleelive](https://clawhub.ai/user/tomleelive) <br>

### License/Terms of Use: <br>
Apache License 2.0 <br>


## Use Case: <br>
Unity developers and game teams use this skill to inspect, modify, debug, and test Unity Editor projects through OpenClaw workflows and a local Unity bridge. It is best suited for trusted, version-controlled local projects where users can review project-changing commands before execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can run C# and perform broad Unity project-changing actions, including deletes, saves, package installs, batch actions, and keyboard or mouse simulation. <br>
Mitigation: Use only in trusted, local, version-controlled Unity projects and review high-impact commands before they run. <br>
Risk: The Unity/OpenClaw bridge exposes editor automation over a local connection. <br>
Mitigation: Keep the bridge limited to a trusted local environment and do not expose it beyond localhost or trusted networks. <br>
Risk: Project changes may cause data loss or project corruption if commands are incorrect. <br>
Mitigation: Keep backups or source control ready before automation sessions and confirm destructive operations with the user. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/tomleelive/skills/openclaw-unity-skill) <br>
- [Skill Homepage](https://github.com/TomLeeLive/openclaw-unity-skill) <br>
- [OpenClaw Unity Plugin](https://github.com/TomLeeLive/openclaw-unity-plugin) <br>
- [OpenClaw Docs](https://docs.openclaw.ai) <br>
- [Unity Plugin Tools Reference](references/tools.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline commands and JSON tool parameters; Unity tool responses are returned as JSON-formatted text.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce project-changing Unity commands through the OpenClaw Unity bridge; users should review destructive or code-running actions before execution.] <br>

## Skill Version(s): <br>
1.6.2 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
