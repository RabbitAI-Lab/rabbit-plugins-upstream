## Description: <br>
Guides agents through prompt-engineering design patterns, multi-agent topology choices, failure handling, context management, tests, and runtime reasoning modes such as CoT, self-consistency, ToT, ReAct, and plan-and-execute. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, prompt engineers, and agent builders use this skill to design agent prompts, choose collaboration topologies, define failure handling, manage context budgets, and select appropriate reasoning modes for complex tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may steer an agent toward ReAct-style tool use for search, browsing, file reads, or calculation. <br>
Mitigation: Use the host agent's normal approval, permission, and audit controls for sensitive commands, file access, or external actions. <br>
Risk: Explicit prompt and reasoning templates can be applied too broadly when a task only needs a direct answer. <br>
Mitigation: Follow the skill's mode-selection guidance and use direct answering for simple requests. <br>


## Reference(s): <br>
- [OpenClaw Implementation Guide](references/implementation-guide.md) <br>
- [Reasoning Modes Academic Reference](references/modes-reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, configuration] <br>
**Output Format:** [Markdown guidance with templates, decision tables, and structured examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Text-only skill; no executable code or generated files.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
