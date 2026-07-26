## Description: <br>
Manage and use local Ollama models for model management, chat and completions, embeddings, tool use, and OpenClaw sub-agent integration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[timverhoogt](https://clawhub.ai/user/timverhoogt) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill to manage local Ollama models, send chat, generation, and embedding requests, and route OpenClaw sub-agent workflows to local models. It is useful for teams that want local LLM experimentation or operation through a configurable Ollama host. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts, model outputs, and model-management actions are sent to the configured Ollama host, which may be remote if OLLAMA_HOST is changed. <br>
Mitigation: Keep OLLAMA_HOST on localhost for sensitive prompts and use only trusted remote Ollama servers. <br>
Risk: Model pull, remove, and sub-agent workflows can affect local model availability or target an unintended host or model. <br>
Mitigation: Double-check the target host and model name before running pull, rm, or sub-agent workflows. <br>


## Reference(s): <br>
- [Models Guide](references/models.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/timverhoogt/skills/ollama-local) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, Python examples, and JSON API examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs depend on the configured Ollama host, selected local model, and command being run.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
