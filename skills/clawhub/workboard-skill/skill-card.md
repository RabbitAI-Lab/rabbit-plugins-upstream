## Description: <br>
Guides OpenClaw operators through using the Workboard skill to list, create, inspect, dispatch, and troubleshoot agent work cards. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeanbai0818-cloud](https://clawhub.ai/user/jeanbai0818-cloud) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and OpenClaw operators use this skill to manage local Workboard cards, dispatch ready cards to worker runs, inspect lifecycle state, and diagnose Gateway or permission issues. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Following the skill's commands can create or modify local Workboard card state. <br>
Mitigation: Confirm the active OpenClaw profile and state root before running create, dispatch, or other write operations. <br>
Risk: Dispatch can start local Gateway worker runs when ready cards are available. <br>
Mitigation: Run dispatch only with an intended Gateway and token, and check ready cards before starting workers. <br>
Risk: The skill documentation is written in Chinese. <br>
Mitigation: Installers should be comfortable reviewing Chinese-language operational instructions before using the skill. <br>


## Reference(s): <br>
- [Workboard card lifecycle](./references/card-lifecycle.md) <br>
- [Workboard agent tools protocol](./references/agent-tools.md) <br>
- [OpenClaw Workboard documentation](https://docs.openclaw.ai/zh-CN/plugins/workboard) <br>
- [ClawHub package page](https://clawhub.ai/jeanbai0818-cloud/skills/workboard-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only skill; examples may produce JSON when users run OpenClaw commands with --json.] <br>

## Skill Version(s): <br>
2026.7.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
