## Description: <br>
Upload a problem photo or paste a problem statement to identify the content, solve it step by step, and generate an interactive HTML solution report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bettermen](https://clawhub.ai/user/bettermen) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and learners use this skill to turn uploaded homework or practice-problem images into structured explanations, final answers, related practice prompts, and study suggestions. It supports mathematics, physics, chemistry, biology, English, Chinese, history, geography, and politics problems. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad homework-solving trigger phrases may activate the skill when the user did not intend to create a full solution report. <br>
Mitigation: Confirm the user has provided a practice problem, photo, or pasted question before performing image reading and report generation. <br>
Risk: Generated HTML reports may include the user's submitted problem content. <br>
Mitigation: Review the local report before sharing it and avoid uploading sensitive or private problem images. <br>
Risk: Photo recognition can misread blurry, reflective, handwritten, or incomplete problem statements. <br>
Mitigation: Flag uncertain recognition, ask for clarification when key conditions are missing, and clearly label any assumptions used in the solution. <br>
Risk: The skill could be used to answer live exam questions. <br>
Mitigation: Refuse assistance for ongoing exams and redirect the user to practice, review, or past-paper analysis. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/bettermen/skills/photo-solver) <br>
- [Subject Taxonomy](references/subject-taxonomy.md) <br>
- [Solution Quality Checklist](references/quality-checklist.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Files, Guidance] <br>
**Output Format:** [Interactive HTML report plus a concise text summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces photo-solver-report.html with KaTeX-rendered formulas and asks the agent to present the generated file.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
