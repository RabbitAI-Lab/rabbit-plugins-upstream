## Description: <br>
Optimize, compress, clarify, structure, score, and audit natural-language prompts for LLMs, GPT, Claude, Gemini, AI Agents, and MCP workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[margaretzybgl](https://clawhub.ai/user/margaretzybgl) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt engineers, and agent builders use this skill to turn conversational or loosely structured requests into compact, auditable downstream-agent prompts while preserving stated constraints. It is suited for coding, product requirements, research, MCP workflows, prompt engineering, and security-review requests where the prompt should be improved without executing the underlying task. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A rewritten prompt could be sent to another agent before a user reviews whether it still preserves the original intent. <br>
Mitigation: Review the optimized prompt and audit ledger before using the prompt for downstream execution. <br>
Risk: Private data or secrets in the input prompt may be exposed if the configured model adapter sends prompts to an external provider. <br>
Mitigation: Avoid including secrets or private data in prompts, especially when using an external model adapter. <br>
Risk: Prompt compression can be misleading when ambiguity, conflict, or risky execution changes meaning. <br>
Mitigation: Use the skill's passthrough and conservative modes, validation status, and fallback metadata to identify cases where the original prompt should remain unchanged. <br>


## Reference(s): <br>
- [Optimize Prompt ClawHub Listing](https://clawhub.ai/margaretzybgl/skills/optimize-prompt) <br>
- [LLM Prompt Firewall Related Skill](https://clawhub.ai/margaretzybgl/skills/llm-prompt-firewall) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [JSON object containing the optimized prompt, audit ledger, validation status, confidence, scoring feedback, and fallback metadata.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The optimized_prompt field is the downstream instruction; prompt_ir is for audit, debugging, and regression testing.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
