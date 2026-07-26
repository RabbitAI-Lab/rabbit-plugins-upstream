## Description: <br>
Rewrites and adapts existing prompts for a target language model while preserving intent, facts, variables, constraints, and output requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daiwk](https://clawhub.ai/user/daiwk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt authors, and agents use this skill to optimize, migrate, or tune prompts for a selected model family while preserving the original prompt contract and noting material changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Provider guidance can become stale or may not match a newly released model variant. <br>
Mitigation: Use the universal profile when a model is not covered and check the provider's official documentation when current model-specific behavior matters. <br>
Risk: A rewritten prompt could accidentally weaken or omit an original requirement. <br>
Mitigation: Review the optimized prompt against the original prompt contract and validate important workflows with representative evaluations. <br>


## Reference(s): <br>
- [Anthropic Claude profile](references/anthropic.md) <br>
- [DeepSeek profile](references/deepseek.md) <br>
- [ByteDance Doubao / Seed profile](references/doubao.md) <br>
- [Google Gemini profile](references/google.md) <br>
- [Moonshot Kimi profile](references/kimi.md) <br>
- [Meta Llama Instruct profile](references/llama.md) <br>
- [MiniMax profile](references/minimax.md) <br>
- [Mistral profile](references/mistral.md) <br>
- [OpenAI profile](references/openai.md) <br>
- [Alibaba Qwen profile](references/qwen.md) <br>
- [Universal optimization profile](references/universal.md) <br>
- [xAI Grok profile](references/xai.md) <br>
- [ClawHub skill page](https://clawhub.ai/daiwk/skills/model-aware-prompt-optimizer) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown sections with a copy-ready optimized prompt] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include material changes, assumptions or questions, and optional API settings when relevant.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
