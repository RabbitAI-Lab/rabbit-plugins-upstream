## Description: <br>
Api Gateway Free helps agents use a hosted API gateway to connect to third-party services such as Slack, Gmail, and Stripe for read-only GET operations and basic connection and authentication checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to verify Maton API authentication, list available connections, and run read-only queries against connected SaaS services through a unified API gateway. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may cause the agent to run local maton CLI or curl commands. <br>
Mitigation: Review commands before execution and install the skill only in environments where local command execution for this workflow is acceptable. <br>
Risk: Connected services may expose sensitive data even through read-only queries. <br>
Mitigation: Use least-privilege read-only scopes and connect only the services needed for the current task. <br>
Risk: API keys or service credentials could be exposed in logs, prompts, or version control. <br>
Mitigation: Keep credentials in environment variables or approved secret stores and avoid printing or committing them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/api-gateway-free) <br>
- [SkillHub Homepage](https://skillhub.cn) <br>
- [Maton API Gateway](https://api.maton.ai/) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API Calls] <br>
**Output Format:** [Markdown with inline shell commands, route examples, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Focuses on read-only GET operations, connection checks, and credential handling guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
