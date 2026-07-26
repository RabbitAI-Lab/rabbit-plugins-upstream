## Description: <br>
A Chinese-language model routing guide for individual developers that recommends Flash, Standard, or Plus / 32B model tiers based on task complexity and API cost goals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and individual builders use this skill to choose between Flash, Standard, and Plus / 32B model tiers for routine chat, coding, agent task distribution, and scheduled tasks while controlling API cost. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad execution and write permissions could allow actions beyond model-routing advice. <br>
Mitigation: Install with least privilege and require review before granting command execution or file-writing authority. <br>
Risk: State-changing configuration operations are described but not tightly scoped. <br>
Mitigation: Require explicit confirmation before modifying, importing, deleting, or resetting configuration. <br>
Risk: The skill may recommend a model tier that is too weak for critical or high-stakes decisions. <br>
Mitigation: Use the guidance only for routing support and avoid relying on it for medical, legal, or fully deterministic decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/model-routing-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with text, code snippets, and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include model-tier recommendations, decision trees, structured response examples, and execution logs.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
