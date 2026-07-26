## Description: <br>
用直觉代替死记，让物理概念从“背下来”变成“真正懂了”，并通过生活类比、实验想象、公式推导三种解释模型先建直觉再学公式。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and tutoring agents use this skill to explain physics concepts by building intuition before formulas through daily-life analogies, thought experiments, formula meaning restoration, and layered understanding checks. It is for conceptual tutoring and validation, not physical experiment operation guidance or problem-solving drill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Physical experiment examples could be mistaken for unsupervised real-world instructions, especially examples involving sunlight, heat, electricity, pressure, or sharp objects. <br>
Mitigation: Present experiment examples as conceptual unless an appropriate supervisor is involved, and avoid operational safety-sensitive instructions when the goal is concept intuition. <br>
Risk: The skill describes updates to learning-profile fields and reminder handoffs after repeated concept failures. <br>
Mitigation: Keep learning-profile updates and reminders visible to the user and under user control. <br>


## Reference(s): <br>
- [Physics Analogy Bank](artifact/references/physics-analogy-bank.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-concept-intuition) <br>
- [Publisher Profile](https://clawhub.ai/user/qizhitang) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or conversational text with structured explanation steps, analogy mappings, formula interpretation, and validation prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No executable output; responses draw on the bundled physics analogy bank and should keep experiment examples conceptual unless supervised.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
