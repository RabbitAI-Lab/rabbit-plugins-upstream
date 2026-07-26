## Description: <br>
Efficiently routes tasks between cheap, default, and pro models using optional sub-agents and briefing to minimize token use and cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[staratheris](https://clawhub.ai/user/staratheris) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to route OpenClaw requests across lower-cost and stronger models, apply manual overrides, and create local briefs before escalating long contexts to sub-agents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Routing recommendations can select higher-cost models or sub-agents. <br>
Mitigation: Use explicit router prompts and review rules.json and state.json when cost control or model-selection behavior matters. <br>
Risk: Briefing long context before escalation may omit information that would affect the final answer. <br>
Mitigation: Review the generated brief before passing it to a higher-cost model or sub-agent for high-impact work. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/staratheris/skills/arya-model-router) <br>
- [ClawHub Publisher Profile](https://clawhub.ai/user/staratheris) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON routing decisions and text briefing output, with Markdown documentation and shell-command integration examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Routing decisions include model tier, selected model, score, reasons, actions, response policy, and an optional local briefing helper.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
