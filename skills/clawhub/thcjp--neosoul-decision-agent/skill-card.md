## Description: <br>
Neosoul Decision Agent provides structured decision support that learns local decision preferences over time and returns confidence-labeled analyses, prompts, and review records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and individual users use this skill to analyze product, technical architecture, business strategy, and personal decisions with structured tradeoff frameworks while reusing local decision-memory files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local decision-memory files may capture sensitive personal, legal, health, or business strategy context. <br>
Mitigation: Review and delete files under ~/decision-making regularly, avoid recording sensitive details unless intentional, and confirm before saving new preferences or decision records. <br>
Risk: Learned preferences and prior decision records may bias later analyses if they are outdated or incorrect. <br>
Mitigation: Treat recommendations as decision support, review cited memory sources, and update or remove stale preferences before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/neosoul-decision-agent) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision analyses, status summaries, local memory records, and optional bash setup commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local files under ~/decision-making; no network access is described.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
