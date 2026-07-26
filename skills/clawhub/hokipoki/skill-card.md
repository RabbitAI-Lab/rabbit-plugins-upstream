## Description: <br>
HokiPoki routes agent requests between Claude, Codex, and Gemini through the HokiPoki CLI for second opinions, model switching, and provider/listener workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[budjoskop](https://clawhub.ai/user/budjoskop) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to send selected tasks, files, directories, or repositories to another AI CLI for a fresh response. It also guides trusted provider/listener workflows for sharing local AI accounts through HokiPoki. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review before execution as proposals could introduce incorrect or misleading guidance into skills. <br>
Mitigation: Review and scan skill before deployment. <br>

## Reference(s): <br>
- [HokiPoki Skill Page](https://clawhub.ai/budjoskop/skills/hokipoki) <br>
- [HokiPoki CLI Command Reference](references/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands and JSON-oriented CLI usage] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prefer specific files over broad directory or repository sharing, review content for secrets before sending it off-device, use --no-auto-apply when returned patches should not be applied automatically, and run provider/listener mode only in trusted workspaces and accounts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
