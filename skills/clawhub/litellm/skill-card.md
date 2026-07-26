## Description: <br>
Call 100+ LLM providers through LiteLLM's unified API for model comparison, task-based routing, cost optimization, and fallback model access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ishaan-jaff](https://clawhub.ai/user/ishaan-jaff) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to call external LLM providers or a LiteLLM proxy from a unified interface. It supports comparing model responses, routing tasks to specialized or lower-cost models, and accessing models unavailable in the primary runtime. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, system messages, and responses may be sent to the selected LLM provider or LiteLLM proxy. <br>
Mitigation: Use only approved providers or proxies for sensitive work, and avoid sending secrets, regulated data, or confidential code unless that destination is approved. <br>
Risk: Provider API keys or LiteLLM proxy keys are required for many calls. <br>
Mitigation: Store keys in environment variables or a managed secret store, limit their scopes, and rotate them according to local policy. <br>
Risk: Model selection and repeated calls can create unexpected usage costs. <br>
Mitigation: Monitor provider usage, set budgets or rate limits where available, and consider pinning the LiteLLM dependency in controlled environments. <br>


## Reference(s): <br>
- [LiteLLM provider documentation](https://docs.litellm.ai/docs/providers) <br>
- [ClawHub LiteLLM skill page](https://clawhub.ai/ishaan-jaff/skills/litellm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python and shell examples; helper script output is plain text or JSON.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Model, prompt, optional system message, temperature, max token limit, and provider or proxy credentials may affect outputs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
