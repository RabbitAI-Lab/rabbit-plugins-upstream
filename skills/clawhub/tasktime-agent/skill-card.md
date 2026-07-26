## Description: <br>
TaskTime Pro is a local-first work manager for freelancers, and this skill lets same-device agents operate tasks, timers, expenses, invoices, reports, and review screens through scoped access and approval controls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tasktimepro](https://clawhub.ai/user/tasktimepro) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an agent work with TaskTime Pro on the same device: planning and updating work, managing tasks and clients, tracking time, preparing invoice data, reviewing reports, handling expenses, opening app review screens, and recovering setup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Granting the skill access to a TaskTime Pro workspace can allow authorized agent actions to create or change business records. <br>
Mitigation: Confirm the requested access before installation, use only needed scopes, inspect or preview data before writes, and rely on TaskTime Pro approval prompts for sensitive operations. <br>
Risk: Pairing codes, approval tokens, authorization headers, exported account data, invoice PDFs, or email payloads may expose sensitive workspace information if logged or shared unnecessarily. <br>
Mitigation: Keep these artifacts out of logs and durable notes unless the user explicitly asks for the artifact, and use short-lived pairing or approval flows through the visible app session. <br>
Risk: Bypassing the bridge and editing browser storage, sync files, invoice records, or billing state directly could corrupt workspace data or skip application safeguards. <br>
Mitigation: Use the supported TaskTime Pro bridge and visible app review screens; do not mutate raw persisted app data outside TaskTime Pro tools. <br>


## Reference(s): <br>
- [TaskTime Pro OpenClaw setup](https://tasktime.pro/agents/openclaw/) <br>
- [TaskTime Pro agent docs](https://tasktime.pro/agents/) <br>
- [TaskTime Pro quickstart](https://tasktime.pro/agents/quickstart/) <br>
- [TaskTime Pro security model](https://tasktime.pro/agents/security/) <br>
- [TaskTime Pro MCP tool reference](https://tasktime.pro/agents/tools/) <br>
- [TaskTime Pro MCP tools JSON](https://tasktime.pro/agents/mcp-tools.json) <br>
- [TaskTime Pro bridge discovery manifest](https://tasktime.pro/.well-known/tasktime-agent.json) <br>
- [TaskTime Pro debugging guide](https://tasktime.pro/agents/debugging/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide MCP tool calls and browser-visible review workflows; sensitive actions remain subject to granted scopes, explicit intent, and app approvals.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
