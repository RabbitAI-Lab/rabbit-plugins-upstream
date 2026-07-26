## Description: <br>
Claude Tmux is an instruction-only helper for managing tmux sessions and reporting operation results from an agent workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to have an agent manage tmux sessions, window operations, and command-oriented workflows while returning status and execution logs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests exec capability with vague tmux scoping. <br>
Mitigation: Review proposed commands before execution and run the skill only in an environment where tmux and shell access are intentionally allowed. <br>
Risk: The evidence reports confusing AI/API-key claims. <br>
Mitigation: Do not provide an API key unless the publisher explains why it is needed; prefer agent-provided LLM access when available. <br>
Risk: The authoritative security verdict is suspicious. <br>
Mitigation: Install only after review and supervise commands and outputs during use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/claude-tmux) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples and inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Instruction-only output; execution behavior depends on the supervising agent and available tmux environment.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
