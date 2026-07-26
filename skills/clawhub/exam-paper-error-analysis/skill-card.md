## Description: <br>
Analyzes exam mistakes across general and vocational education, including single-question diagnosis, whole-paper loss analysis, variant exercise generation, and error-category review from text, images, or PDFs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[flyboat403](https://clawhub.ai/user/flyboat403) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Teachers, tutors, and vocational education instructors use this skill to diagnose student mistakes, plan targeted review, generate practice variants, and produce structured local HTML reports for classroom follow-up. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exam submissions can include student work or personal identifiers in generated local HTML reports. <br>
Mitigation: Choose an appropriate save location, avoid unnecessary personal identifiers, and delete reports when they are no longer needed. <br>
Risk: Analysis quality depends on readable input and confirmed extraction from images or PDFs. <br>
Mitigation: Review recognized content with the user before analysis and request clearer images, page ranges, or missing answer details when needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/flyboat403/skills/exam-paper-error-analysis) <br>
- [Server-resolved GitHub Source](https://github.com/flyboat403/exam-paper-error-analysis/tree/main/skills/exam-paper-error-analysis) <br>
- [HTML Report Structure](references/html-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Guidance, HTML, Files] <br>
**Output Format:** [HTML document with inline CSS and structured analysis sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local reports and asks users to confirm extracted or recognized exam content before analysis.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
