## Description: <br>
Migrate OpenAI-compatible apps, SDKs, examples, and environment variables to TokenLab while preserving request semantics and adding live model discovery. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hedging8563](https://clawhub.ai/user/hedging8563) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to migrate OpenAI-compatible, OpenRouter, LiteLLM, LangChain, LlamaIndex, Anthropic, or Gemini integrations to TokenLab with minimal code and configuration changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A migration could unintentionally route application traffic through TokenLab. <br>
Mitigation: Review the proposed diff, confirm TokenLab is the intended provider, and run the migrated path's smoke test before deployment. <br>
Risk: API keys could be exposed if they are committed to source control or included directly in prompts. <br>
Mitigation: Set TOKENLAB_API_KEY through the user's normal secret-management process and keep credentials out of source files. <br>
Risk: Native provider behavior could change if Anthropic, Gemini, media, audio, embeddings, rerank, or translation flows are flattened into generic chat calls. <br>
Mitigation: Preserve native endpoint semantics unless the user explicitly accepts the behavior change, and check TokenLab model details before claiming feature parity. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/hedging8563/skills/tokenlab-openai-compatible-migration) <br>
- [TokenLab OpenAI-compatible API base URL](https://api.tokenlab.sh/v1) <br>
- [TokenLab model discovery endpoint](https://api.tokenlab.sh/v1/models) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with focused diffs, configuration blocks, runnable snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a smoke test command, model discovery command, and rollback note.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
