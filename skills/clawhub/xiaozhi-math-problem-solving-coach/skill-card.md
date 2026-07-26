## Description: <br>
A math tutoring coach that guides students through problem solving with Socratic questions, CLAW prompts, photo-question workflows, error analysis, same-type practice, and exam review without directly giving answers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qizhitang](https://clawhub.ai/user/qizhitang) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External learners and education agents use this skill to work through math questions, identify where a student is stuck, analyze mistakes, generate similar practice problems, and prepare focused exam review while avoiding direct answer-giving. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Student photos may contain personal, school, or location information when the photo-question workflow is used. <br>
Mitigation: Require clear consent and image-redaction guidance before OCR or multimodal processing, especially in environments with students or minors. <br>
Risk: Learning-profile and error-history records may be read or written during tutoring workflows. <br>
Mitigation: Provide controls to inspect, disable, limit access to, and delete learning-profile and error-history records. <br>
Risk: Tutoring guidance and generated practice problems can be incomplete or misleading for a learner's level or curriculum. <br>
Mitigation: Use teacher, parent, or administrator review for high-stakes learning contexts and encourage students to verify reasoning rather than rely on final answers. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-math-problem-solving-coach) <br>
- [CLAW template extensions](references/claw-templates-extended.md) <br>
- [Math Socratic guide](references/math-socrates-guide.md) <br>
- [Photo four-step state machine](references/photo-4step-statemachine.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown-style conversational tutoring guidance, diagnostic questions, prompt templates, review outlines, and practice problems.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use photo-question interpretation through multimodal or OCR-capable host systems and may read or update learning-profile and error-history records when those companion skills are available.] <br>

## Skill Version(s): <br>
2.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
