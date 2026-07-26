## Description: <br>
Adds security governance layers to an OpenClaw agent, including budget controls, permissions, audit logging, a kill switch, identity signing, skill vetting, process isolation, and gateway protection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[onezeroeight-ai](https://clawhub.ai/user/onezeroeight-ai) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to install and configure Sammā Suit governance controls for OpenClaw agents. It focuses on enforcing permissions, budgets, audit logging, identity signing, process limits, skill vetting, and shutdown controls during agent operation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports broad control over an agent and full activity logging without enough installation, data-use, or rollback detail. <br>
Mitigation: Before installing, obtain the full source, exact install command, pinned release, SAMMA_API_KEY scope, audit-log storage and retention rules, data-flow documentation, and a clear disable or uninstall procedure. <br>
Risk: The artifact starts installation guidance but does not provide a complete command or rollback procedure. <br>
Mitigation: Avoid using the skill with sensitive or production agents until complete installation, configuration, and recovery instructions are available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/onezeroeight-ai/skills/samma-suit) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with installation and configuration steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SAMMA_API_KEY.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
