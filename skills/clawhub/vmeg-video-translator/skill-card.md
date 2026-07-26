## Description: <br>
VMEG Audio/Video Translation, Subtitle Translation, and Dubbing helps agents use VMEG Remote MCP for video, audio, and subtitle translation, material and task management, script editing, and export. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maxeileen55-beep](https://clawhub.ai/user/maxeileen55-beep) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and media teams use this skill to connect an agent to VMEG Remote MCP, manage media materials and translation tasks, edit scripts or subtitles, and export translated or dubbed media. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill connects to VMEG's remote service and may upload local audio or video files. <br>
Mitigation: Install it only when VMEG remote processing is intended, and confirm the exact local media file before allowing an agent to upload it. <br>
Risk: A vmeg_sk API key can grant account access if exposed. <br>
Mitigation: Prefer OAuth when available, protect API keys, and keep MCP configuration files out of shared repositories. <br>
Risk: Some VMEG operations can delete data, consume quota, or submit final renders and exports. <br>
Mitigation: Require user confirmation before deleting materials or tasks, retranslating, re-dubbing, or composing final exports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/maxeileen55-beep/skills/vmeg-video-translator) <br>
- [VMEG Homepage](https://www.vmeg.ai) <br>
- [VMEG Remote MCP Endpoint](https://www.vmeg.ai/api/mcp) <br>
- [README](README.md) <br>
- [VMEG MCP Tools Overview](references/tools.md) <br>
- [VMEG MCP Authentication](references/oauth.md) <br>
- [VMEG MCP Common Configuration](references/setup-common.md) <br>
- [Install VMEG Media Translation Skill](references/install.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Configuration instructions, Shell commands, API Calls] <br>
**Output Format:** [Markdown guidance with JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May trigger VMEG MCP tool calls and media uploads when the user authorizes them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
