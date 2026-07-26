## Description: <br>
Control Unreal Engine Editor via OpenClaw Unreal Plugin for level and actor management, transforms, PIE control, debugging, input simulation, console commands, viewport screenshots, and log capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tomleelive](https://clawhub.ai/user/tomleelive) <br>

### License/Terms of Use: <br>
Apache-2.0 <br>


## Use Case: <br>
Developers and technical artists use this skill to operate a trusted local Unreal Engine Editor session through OpenClaw for scene inspection, actor creation and deletion, transforms, play-in-editor control, console execution, screenshots, and logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad Unreal Editor controls that can change projects, including delete, save, import, console, and input-simulation actions. <br>
Mitigation: Install only for trusted local Unreal projects, keep source control or backups, and require explicit review before allowing those actions. <br>
Risk: Screenshots and log reads can expose sensitive information visible in the editor or present in project logs. <br>
Mitigation: Review screenshots and logs before sharing them outside the local machine. <br>
Risk: The current security assessment reports broad project-changing controls without built-in confirmation gates and inconsistent safety guidance. <br>
Mitigation: Keep disableModelInvocation enabled and review each high-impact request before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tomleelive/skills/openclaw-unreal-skill) <br>
- [Project homepage](https://github.com/TomLeeLive/openclaw-unreal-skill) <br>
- [OpenClaw Unreal Plugin](https://github.com/openclaw/openclaw-unreal-plugin) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and structured tool parameters for Unreal Editor actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May queue commands against a connected local Unreal Editor session and return session status, screenshots, logs, or command results.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter, changelog, release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
