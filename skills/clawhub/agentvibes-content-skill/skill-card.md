## Description: <br>
API wrapper skill for AgentVibes content workflows that calls external APIs, returns API response data, and supports content creation, management, multimodal generation, monitoring, retries, and multi-format handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external agent users use this skill to route AgentVibes content creation and management requests through API calls and receive structured response data. It is not positioned for complex cases that require human judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill describes broad API, publishing, deletion, and multi-tenant administration powers without enough documented scope or safeguards. <br>
Mitigation: Review before installing, use a limited API key, and restrict use to clearly scoped test or non-critical resources unless the publisher documents exact endpoints, permissions, tenant limits, and confirmation requirements. <br>
Risk: The artifact requires API key configuration and includes executable-agent posture. <br>
Mitigation: Store API keys outside version control, grant only the minimum required permissions, and confirm write or delete actions before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agentvibes-content-skill) <br>
- [ClawDIS homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON response examples and shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe API responses with success, data, and error fields.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
