## Description: <br>
This skill should be used when the user asks to "compress context", "summarize conversation history", "implement compaction", "reduce token usage", or mentions context compression, structured summarization, tokens-per-task optimization, or long-running agent sessions exceeding context limits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leoyessi10-tech](https://clawhub.ai/user/leoyessi10-tech) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent builders use this skill to design, implement, and evaluate context-compression workflows for long-running agent sessions, large codebases, and token-constrained task execution. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Compressed summaries can preserve sensitive user goals, file paths, errors, decisions, and excerpts from prior conversation. <br>
Mitigation: Treat generated summaries and evaluation inputs as sensitive; redact private content before sharing or storing them. <br>
Risk: Adapting the LLM-judge example can send compacted context to an external provider. <br>
Mitigation: Get explicit user control before sending compressed context externally and redact sensitive details first. <br>
Risk: The included evaluator uses simplified token estimation, pattern-based extraction, and stubbed judge calls. <br>
Mitigation: Replace the examples with model-specific tokenizers, production-grade extraction, and reviewed API integrations before relying on the scores operationally. <br>


## Reference(s): <br>
- [Context Compression Evaluation Framework](references/evaluation-framework.md) <br>
- [ClawHub skill page](https://clawhub.ai/leoyessi10-tech/skills/context-engineering) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with structured examples, tables, and optional Python evaluation code] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce structured summaries, probe questions, scoring rubrics, implementation plans, and evaluation snippets for context-compression workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
