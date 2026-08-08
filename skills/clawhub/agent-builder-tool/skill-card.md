## Description: <br>
Agent Builder Tool helps users create, configure, publish, remix, and manage custom AgentPMT AI agents through hosted remote tool calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[agentpmt](https://clawhub.ai/user/agentpmt) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers, operators, and AgentPMT users use this skill to create and manage private or published custom AI agents, attach tools, workflows, and context documents, remix existing agents, and preview showcase examples without writing code. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: State-changing actions can publish, archive, remix, or replace context documents on remote AgentPMT agents. <br>
Mitigation: Confirm the target agent and intended changes before invoking state-changing actions. <br>
Risk: AgentPMT credentials or payment material could be exposed if copied into prompts or logs. <br>
Mitigation: Keep credentials in the setup flow and out of prompts, generated instructions, and logs. <br>


## Reference(s): <br>
- [AgentPMT marketplace product](https://www.agentpmt.com/marketplace/agent-builder-tool) <br>
- [ClawHub skill page](https://clawhub.ai/agentpmt/skills/agent-builder-tool) <br>
- [Generated action schema](artifact/schema.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, JSON, Configuration] <br>
**Output Format:** [Markdown guidance with JSON request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines 16 AgentPMT actions and expects returned JSON to be treated as the source of truth.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
