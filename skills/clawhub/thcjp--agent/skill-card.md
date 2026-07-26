## Description: <br>
Defines an agent's identity, personality, voice, and boundaries to help create consistent persona-driven assistants for LLM applications and agent orchestration. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to shape persona, tone, and behavioral boundaries for conversational assistants in LLM apps and agent orchestration. It is not intended for critical decisions that require guaranteed determinism. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests shell execution and advertises broad automation features without a clear command scope. <br>
Mitigation: Review carefully before installing, require explicit approval for commands, and disable shell execution unless the publisher documents exactly what may run. <br>
Risk: The security summary flags a persona-focused skill with broad automation claims and limited safeguards. <br>
Mitigation: Use it for assistant style and configuration guidance only until the release has been reviewed and accepted in the target environment. <br>
Risk: The skill states that it is not suitable for decisions requiring complete certainty. <br>
Mitigation: Keep high-stakes or deterministic decisions in reviewed workflows with human oversight. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/agent) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return structured persona/configuration results and environment setup guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
