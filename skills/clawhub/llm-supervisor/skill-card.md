## Description: <br>
Graceful rate limit handling with Ollama fallback. Notifies on rate limits, offers local model switch with confirmation for code tasks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dhardie](https://clawhub.ai/user/dhardie) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to keep OpenClaw sessions responsive when cloud LLM providers hit rate limits, while requiring explicit confirmation before code tasks run on a local Ollama model. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reroute agents between cloud and local models, which may affect model quality, provider policy compliance, or cost controls. <br>
Mitigation: Review the provider-switching behavior before installation, confirm that local Ollama fallback is acceptable, and verify that cloud mode using anthropic:default matches the intended provider setup. <br>
Risk: Code tasks may run on a local model after a cloud rate limit if confirmation controls are too broad or misunderstood. <br>
Mitigation: Use a clear confirmationPhrase such as CONFIRM LOCAL CODE and require explicit approval before local code-generation tasks proceed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/dhardie/skills/llm-supervisor) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact Skill Definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown notifications and command replies with inline shell commands and LLM profile configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Session state tracks cloud or local mode, the active local model, recent rate-limit errors, and whether local code execution has been confirmed.] <br>

## Skill Version(s): <br>
0.3.0 (source: server release metadata and skill.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
