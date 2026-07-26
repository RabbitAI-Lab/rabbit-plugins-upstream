## Description: <br>
Guides an agent to coach users through metacognitive monitoring when they are stuck, repeating mistakes, overconfident, or deciding whether to trust AI-assisted reasoning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to structure reflection during difficult reasoning, problem solving, debugging, strategy work, and AI-assisted verification. It helps an agent ask staged monitoring questions, calibrate confidence, and produce a metacognitive worksheet. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can add friction if invoked during routine work or creative flow. <br>
Mitigation: Follow the skill's When NOT to use guidance and disable or ignore it when uninterrupted flow or routine task completion matters more than monitoring. <br>
Risk: Metacognitive prompts may reinforce worry for users who are already over-monitoring. <br>
Mitigation: Redirect rather than continue coaching when the user's issue is anxiety or rumination rather than a concrete reasoning task. <br>
Risk: The skill provides reasoning guidance and confidence calibration, not independent verification of facts, code, or citations. <br>
Mitigation: For high-stakes claims, source references, security-relevant code, financial figures, medical claims, or legal citations, verify against primary sources before relying on the output. <br>


## Reference(s): <br>
- [Primary sources for metacognition](references/sources.md) <br>
- [Metacognition while working with AI copilots](examples/metacognition-with-ai-copilots-2024-2026.md) <br>
- [Polya at Stanford and Schoenfeld at Berkeley](examples/polya-at-stanford-and-schoenfeld-at-berkeley-1942-1985.md) <br>
- [Flavell 1979 metacognition paper](https://doi.org/10.1037/0003-066X.34.10.906) <br>
- [Parasuraman and Riley 1997 automation bias paper](https://doi.org/10.1518/001872097778543886) <br>
- [deciqAI Metacognition page](https://www.deciqai.com/c/metacognition) <br>
- [deciqAI Metacognition machine-readable metadata](https://www.deciqai.com/s/metacognition.json) <br>
- [ClawHub skill page](https://clawhub.ai/deciqai/skills/metacognition) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown worksheet and stepwise coaching prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [In coach mode, the skill pauses at explicit wait points before advancing; for concrete tasks, it produces a staged metacognitive worksheet.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
