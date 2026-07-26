## Description: <br>
检查本机 Claude Code 二进制是否含有向系统提示词日期行注入近不可见 Unicode 撇号（U+2019/U+02BC/U+02B9）的隐写标记代码，并在受影响时升级到干净版本。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwbwin](https://clawhub.ai/user/wwbwin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to audit a local Claude Code installation for documented date-line Unicode marker behavior and to plan an upgrade when the installed binary is affected or suspect. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can propose a global npm upgrade for Claude Code, which changes software outside the current agent session. <br>
Mitigation: Require explicit user approval before running upgrade commands and confirm the command targets the intended @anthropic-ai/claude-code package. <br>
Risk: The audit reads a local Claude Code binary and reports a verdict that may be SUSPECT when only partial marker signals are present. <br>
Mitigation: Treat SUSPECT as a prompt for manual review or upgrade rather than as definitive proof of affected behavior. <br>


## Reference(s): <br>
- [Known Versions and Unicode Marker Signals](references/known_versions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and optional JSON audit output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Audit results may classify the local Claude Code binary as CLEAN, SUSPECT, or AFFECTED; upgrade commands require explicit user approval.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
