## Description: <br>
Loop Builder helps agents turn loosely described repeated tasks into controllable workflow designs with evidence gates, feedback signals, stopping rules, and explicit human decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yangchao228](https://clawhub.ai/user/yangchao228) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workflow authors use this skill to decide whether a repeated task should become a Prompt, checklist, Human-in-the-Loop flow, full Loop package, specialized Agent, or reusable Skill. It helps define required context, feedback, iteration limits, stop rules, circuit breakers, and human approval points before executable artifacts are generated. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated Loop, Agent, or Skill packages may shape later file edits, installation, publication, production changes, deletion, billing, credentials, or other high-impact actions. <br>
Mitigation: Review each generated package before use and require separate, action-specific approval for high-impact steps. <br>
Risk: A workflow design may be misleading if the agent proceeds without required context or decision evidence. <br>
Mitigation: Use the skill's context gate, stop when required evidence is missing, and resume only after the missing decision-critical inputs are supplied. <br>
Risk: Iteration can continue after feedback stops improving or scope expands beyond the confirmed task. <br>
Mitigation: Apply bounded iteration limits, explicit stop rules, circuit breakers, and human approval points before generating or acting on executable artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/yangchao228/skills/loop-builder) <br>
- [OpenClaw homepage](https://github.com/yangchao228/my_open_skills/tree/main/skills/engineering/loop-builder) <br>
- [Loop Pattern Reference](references/loop-patterns.md) <br>
- [Loop Checklists](references/checklists.md) <br>
- [Specialized Skill Generation Contract](references/skill-generation-contract.md) <br>
- [Specialized Loop Agent Package](references/agent-package.md) <br>
- [Scenario Defaults](references/scenarios.md) <br>
- [Loop Templates](references/templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, configuration] <br>
**Output Format:** [Markdown with structured status cards, workflow cards, checklists, and reusable artifact templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are gated by context sufficiency, workflow confirmation, and action-specific approval for risky or irreversible steps.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
