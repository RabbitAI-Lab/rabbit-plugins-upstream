## Description: <br>
ExpertLens-Lite gives an agent a structured reasoning persona for diagnosing the real problem, adapting to the task domain, self-auditing output, and optionally coordinating cross-model review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ashutosh2m](https://clawhub.ai/user/ashutosh2m) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to make a host agent produce more deliberate, domain-adapted, self-audited answers for complex, creative, strategic, architectural, or publishable work. It is not intended to activate for simple factual lookups, one-step edits, or casual conversation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can broadly auto-activate and influence how the host agent frames complex or high-stakes work. <br>
Mitigation: Install it only where a persistent expert-reasoning persona is desired, and keep normal host review practices in place for consequential outputs. <br>
Risk: Cross-model collaboration or web-enabled workflows may expose user context to external AI services. <br>
Mitigation: Keep browser, external AI, and email tools disabled unless explicitly needed, and review any context before it is shared outside the current agent. <br>
Risk: The skill may propose persistent memory or saved context on platforms that support it. <br>
Mitigation: Require explicit user approval before memory or file writes, and inspect saved content for sensitive or unnecessary context. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/ashutosh2m/skills/expertlens) <br>
- [Project homepage](https://github.com/Ashutosh2M/ExpertLens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-formatted prose, lists, tables, recommendations, and task-specific code or command blocks when requested by the user.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Markdown-only skill instructions; no direct code execution, credential handling, API calls, or file writes are defined by the skill itself.] <br>

## Skill Version(s): <br>
2.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
