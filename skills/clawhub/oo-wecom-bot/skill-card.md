## Description: <br>
WeCom Bot enables agents to read, create, update, and delete WeCom messages, schedules, meetings, documents, sheets, smart pages, and todos through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workplace automation users use this skill to operate WeCom Bot workflows from an agent, including messaging, scheduling, meetings, docs, sheets, smart pages, and todo management. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform broad WeCom write and delete actions across messages, schedules, meetings, documents, sheets, smart pages, and todos. <br>
Mitigation: Confirm the exact target, payload, and expected effect with the user before running any write or destructive action. <br>
Risk: The dynamic call_tool action is not clearly restricted to read-only behavior. <br>
Mitigation: Use curated actions when possible; if call_tool is necessary, inspect the live schema and get explicit approval before any state-changing operation. <br>
Risk: The security verdict is suspicious for this release. <br>
Mitigation: Install only when the user trusts OOMOL and intends to let the agent operate the connected WeCom Bot account. <br>


## Reference(s): <br>
- [WeCom Bot homepage](https://work.weixin.qq.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wecom-bot) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses live connector schema inspection before action execution; command results are returned as JSON by the oo CLI.] <br>

## Skill Version(s): <br>
1.0.2 (source: release evidence and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
