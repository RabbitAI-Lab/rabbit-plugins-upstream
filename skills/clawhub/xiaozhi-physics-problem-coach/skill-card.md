## Description: <br>
A Chinese-language physics problem-solving coach that guides students through diagramming, physical modeling, calculation, and reflection instead of giving full answers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Students and tutors use this skill to work through physics exercises by first establishing a physical diagram, then selecting a model, writing equations, checking units, and reflecting on errors. It is especially oriented toward mechanics, circuits, optics, and common middle-school physics problem types. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may persist or sync detailed student learning records, including mistakes, answers, weak points, and recovery state. <br>
Mitigation: Use it only when the platform provides clear consent, local-only storage when promised, deletion and export controls, and a no-storage mode; confirm these controls before using it with students, especially minors. <br>
Risk: Image-based problem intake depends on multimodal vision or OCR and can misread unclear problem statements. <br>
Mitigation: When image recognition is unavailable or uncertain, ask the student to type the problem and known conditions, then confirm the interpretation before continuing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-physics-problem-coach) <br>
- [physics-4step-statemachine.md](artifact/references/physics-4step-statemachine.md) <br>
- [physics-socrates-guide.md](artifact/references/physics-socrates-guide.md) <br>
- [physics-diagram-guide.md](artifact/references/physics-diagram-guide.md) <br>
- [claw-templates-physics.md](artifact/references/claw-templates-physics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Conversational Markdown guidance with prompts, checks, and step-by-step tutoring structure] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask the student to provide text descriptions or drawings when image/OCR support is unavailable.] <br>

## Skill Version(s): <br>
2.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
