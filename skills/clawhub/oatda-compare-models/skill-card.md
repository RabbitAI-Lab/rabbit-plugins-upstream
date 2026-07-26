## Description: <br>
Compare multiple LLM models side by side through OATDA's unified AI gateway and return each model's output with token usage and cost. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devcsde](https://clawhub.ai/user/devcsde) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical users use this skill to send one prompt to several LLM providers through OATDA and compare quality, cost, and token usage across model responses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts are sent to OATDA and connected model providers as external API data. <br>
Mitigation: Avoid submitting secrets or confidential content unless the user's OATDA account and data-handling expectations permit it. <br>
Risk: The skill depends on an OATDA API key for API calls. <br>
Mitigation: Keep the API key private and verify only its presence or a short prefix when troubleshooting. <br>
Risk: Multi-model comparisons can consume credits across every selected model. <br>
Mitigation: Check balance or reduce the model list before running larger comparisons. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/devcsde/skills/oatda-compare-models) <br>
- [OATDA Homepage](https://oatda.com) <br>
- [OATDA Compare API](https://oatda.com/api/v1/compare) <br>
- [OATDA API Keys](https://oatda.com/dashboard/api-keys) <br>
- [OATDA Credits](https://oatda.com/dashboard/credits) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns side-by-side model responses with per-model token usage and cost when provided by OATDA.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
