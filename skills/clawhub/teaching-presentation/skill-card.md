## Description: <br>
Creates classroom-ready teaching presentation outlines and PPTX files from lesson plans, web content, or topic keywords, including content classification, structured JSON outlines, classroom flow planning, interaction design, role mapping, and teacher-facing speaker notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers and education content creators use this skill to turn lesson plans, instructional web content, or topic keywords into classroom presentation outlines and PPTX files. The skill emphasizes teacher action cues, student response prompts, interaction planning, and slide speaker notes rather than static knowledge summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lesson plans and source materials may contain sensitive student, school, or classroom information. <br>
Mitigation: Review and redact private information before providing materials to the agent, and inspect generated outlines and PPTX files before classroom use. <br>
Risk: The full workflow depends on referenced supporting files and a PPTX generation skill being available. <br>
Mitigation: Confirm required references and the PPTX skill are installed before relying on the skill for end-to-end presentation generation. <br>


## Reference(s): <br>
- [Server-resolved GitHub repository](https://github.com/flyboat403/teaching-presentation) <br>
- [ClawHub skill page](https://clawhub.ai/flyboat403/skills/teaching-presentation) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Configuration, Guidance, Files] <br>
**Output Format:** [Markdown guidance with structured JSON outlines and generated PPTX presentation files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May stop after outline generation when the user asks for outline-only output; otherwise expects PPTX generation and validation.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
