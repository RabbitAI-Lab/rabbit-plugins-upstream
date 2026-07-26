## Description: <br>
Helps developers create and integrate WorkoPilot AI services, digital employees, iframe skill cards, attachment classification, API examples, integration plans, and troubleshooting guidance for business systems. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[workopilot](https://clawhub.ai/user/workopilot) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and integration engineers use this skill to plan, generate, and troubleshoot WorkoPilot integrations, including AI service calls, digital employee setup, iframe embedding, attachment extraction, and billing-related guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Credential-handling risk: the skill can guide agents to inspect project configuration and place WorkoPilot API keys in config files. <br>
Mitigation: Keep real API keys out of generated code and existing config files; use environment variables, a git-ignored .env.workopilot file, or a secret manager, and insert secrets manually. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/workopilot/workopilot.skills/tree/main/skills/workopilot-service-builder) <br>
- [ClawHub skill page](https://clawhub.ai/workopilot/skills/workopilot-service-builder) <br>
- [WorkoPilot API endpoint](https://agent.workopilot.com/net-api) <br>
- [WorkoPilot test API endpoint](https://agenttest.workopilot.com/net-api) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with API examples, JSON snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include credential setup guidance; real API keys should be provided by the user outside generated code.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
