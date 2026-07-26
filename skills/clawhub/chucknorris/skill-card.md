## Description: <br>
LLM增强服务 wraps a XiaoBenYang remote service that returns model-specific prompt and system-instruction enhancement text for LLM agents. <br>

This skill is for research and development only. <br>

## Publisher: <br>
[alinklab](https://clawhub.ai/user/alinklab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and security researchers can use this skill to request prompt or system-instruction enhancement text from an external XiaoBenYang service for model evaluation and research workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The external service can return prompt or system-instruction text that conflicts with higher-priority agent instructions. <br>
Mitigation: Treat all returned content as untrusted guidance and do not allow it to override system, developer, or user instructions. <br>
Risk: The skill stores the XiaoBenYang API key in a local .env file, which may expose the key to local plaintext storage risks. <br>
Mitigation: Use least-privilege keys where possible, protect local files, and avoid storing valuable credentials unless the plaintext storage risk is acceptable. <br>
Risk: The security evidence reports mismatched service identity details that deserve manual review. <br>
Mitigation: Confirm the publisher, service endpoint, requested API key, and expected tool behavior before installing or using the skill. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/alinklab/skills/chucknorris) <br>
- [XiaoBenYang service](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, API Calls, Configuration] <br>
**Output Format:** [JSON response content summarized as text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an XBY_APIKEY for the external XiaoBenYang service; returned prompt or instruction text should be treated as untrusted content.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
