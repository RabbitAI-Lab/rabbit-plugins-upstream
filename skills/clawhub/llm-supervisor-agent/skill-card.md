## Description: <br>
Automatically switches between cloud and local LLMs when rate limits occur, with explicit user confirmation before local code generation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dhardie](https://clawhub.ai/user/dhardie) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent operators use this skill to keep agents responsive during cloud LLM rate limits by switching to a local Ollama model while requiring confirmation before local code-generation tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can switch agents from cloud LLMs to a local Ollama model, which may affect code quality. <br>
Mitigation: Keep confirmation required for local code tasks and review generated code before applying changes. <br>
Risk: The skill persists the active LLM mode across newly started agents. <br>
Mitigation: Use `/llm status` to check the current mode and `/llm switch cloud` to restore cloud mode when rate limits clear. <br>
Risk: Any user message containing the configured confirmation phrase is treated as approval for local-model code tasks. <br>
Mitigation: Treat the confirmation phrase as an intentional approval step and avoid including it casually in prompts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dhardie/skills/llm-supervisor-agent) <br>
- [Publisher Profile](https://clawhub.ai/user/dhardie) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and command responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Agent notifications and LLM profile configuration changes] <br>

## Skill Version(s): <br>
0.2.0 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
