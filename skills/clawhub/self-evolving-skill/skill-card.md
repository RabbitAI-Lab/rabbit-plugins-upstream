## Description: <br>
Meta-cognitive self-learning system - Automated skill evolution based on predictive coding and value-driven mechanisms. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[whtoo](https://clawhub.ai/user/whtoo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to create, execute, analyze, save, and reload self-evolving skills that adapt from execution context, embeddings, success signals, and value scores. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may retain local task context, embeddings, or learned skill state for future runs. <br>
Mitigation: Set an explicit storage directory, avoid sensitive inputs until retention and deletion behavior are clear, and review stored state periodically. <br>
Risk: Local MCP or Python helper configuration can affect what code starts automatically. <br>
Mitigation: Review the local MCP/Python server configuration before enabling automatic startup. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/whtoo/skills/self-evolving-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Configuration] <br>
**Output Format:** [JSON tool responses and Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist local skill state, task context, embeddings, and learning history depending on configuration.] <br>

## Skill Version(s): <br>
1.0.2 (source: package.json, openclaw.yaml, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
