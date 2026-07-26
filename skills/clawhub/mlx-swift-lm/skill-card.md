## Description: <br>
MLX Swift LM - Run LLMs and VLMs on Apple Silicon using MLX. Covers local inference, streaming, tool calling, LoRA fine-tuning, and embeddings. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ronaldmannak](https://clawhub.ai/user/ronaldmannak) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineers use this skill for Swift guidance when building local LLM, VLM, embedding, tool-calling, and LoRA fine-tuning workflows on Apple Silicon with MLX. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Examples may download models or media from remote sources. <br>
Mitigation: Use trusted or pinned model sources and validate remote media URLs before running copied examples. <br>
Risk: Tool-calling examples can execute application-defined side effects. <br>
Mitigation: Require confirmation or review before executing side-effecting tool calls. <br>
Risk: Prompt caches, saved chat history, LoRA adapters, and training artifacts may contain sensitive local data. <br>
Mitigation: Treat generated caches and training outputs as sensitive files and store or share them according to local data-handling policy. <br>
Risk: Hugging Face tokens or private model credentials may be exposed if copied into examples or logs. <br>
Mitigation: Keep tokens in secure configuration, avoid hard-coding credentials, and redact them from logs and shared artifacts. <br>


## Reference(s): <br>
- [MLX Swift LM Skill Page](https://clawhub.ai/ronaldmannak/skills/mlx-swift-lm) <br>
- [ModelContainer & Model Loading](references/model-container.md) <br>
- [KV Cache System](references/kv-cache.md) <br>
- [Concurrency Patterns](references/concurrency.md) <br>
- [Tool Calling](references/tool-calling.md) <br>
- [Tokenizer & Chat Messages](references/tokenizer-chat.md) <br>
- [Supported Models](references/supported-models.md) <br>
- [LoRA Adapters](references/lora-adapters.md) <br>
- [LoRA Training](references/training.md) <br>
- [Embedding Models](references/embeddings.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Configuration] <br>
**Output Format:** [Markdown with Swift code examples and configuration guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Documentation-only guidance; examples may reference local files, Hugging Face models, prompt caches, and training artifacts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
