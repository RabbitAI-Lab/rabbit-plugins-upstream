## Description:

Turns a student's own course materials into an exam-focused study guide and confidence-ranked prediction of likely exam questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samdozer](https://clawhub.ai/user/samdozer)

### License/Terms of Use:

MIT-0

## Use Case:

Students and academic support users use this skill to convert provided lecture slides, transcripts, past exams, model answers, lab manuals, notes, and related course files into a study guide, exam blueprint, and likely question set. It is designed for biology-family and related lab science courses, with Arabic and English transcript handling when supplied by the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes user-provided course files, which may contain unrelated private information.

Mitigation: Provide only the course materials needed for the target exam and exclude unrelated private documents.

Risk: The skill can create output files in the user's outputs folder.

Mitigation: Review generated files before sharing them and request the preferred output language before generation when English is not suitable.

Risk: Exam predictions may be less reliable when strong sources such as past papers, official model answers, or explicit professor statements are missing.

Mitigation: Treat confidence labels as prioritization guidance and supply past exams, model answers, and professor transcripts when available.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/SamDozer/exam-study-guide-predictor/tree/main/exam-study-guide-predictor)
- [ClawHub skill page](https://clawhub.ai/samdozer/skills/exam-study-guide-predictor)
- [Prediction & Analysis Method](references/prediction-and-analysis.md)
- [Output Format & Section Catalog](references/output-format.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Files, Guidance]

**Output Format:** [Markdown or self-contained HTML/Word study guide, with optional Anki-ready CSV]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces source-bound study guidance, confidence-ranked predictions, model answers, and optional user output files.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
