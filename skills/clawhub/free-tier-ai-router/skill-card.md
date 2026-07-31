## Description: <br>
Quota-aware LLM router for free-tier Gemini, Mistral, OpenRouter, Kilo and Cerebras keys that probes model availability and quality, applies published rate limits, and routes agent requests while preserving scarce quota and persisted cooldowns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to choose among multiple free-tier LLM provider keys, avoid avoidable rate-limit failures, and keep high-scarcity quota available for tasks that need it. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles AI provider API keys and can send prompts or system text to selected third-party providers. <br>
Mitigation: Use only provider keys and prompt content appropriate for those services, avoid sensitive probe prompts, and review provider routing before deployment. <br>
Risk: The skill writes persistent response cache, cooldown, and state data under the user's home directory. <br>
Mitigation: Use --no-cache for sensitive work and review or clear local state when changing trust boundaries. <br>
Risk: The one-file bootstrap and setup scripts perform broad install and integration behavior. <br>
Mitigation: Review get-ai-router.sh and setup scripts before use, especially on shared systems or managed workstations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/free-tier-ai-router) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Probe evidence](artifact/PROBE.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, configuration files, and text responses from selected LLM providers] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May send prompts and system text to configured third-party AI providers and may persist cache, cooldown, and routing state under the user's home directory.] <br>

## Skill Version(s): <br>
2.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
