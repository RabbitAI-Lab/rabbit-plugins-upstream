## Description: <br>
Ai Talent Grader evaluates AI-role candidates from resumes, interview records, and job descriptions by producing resume audits, follow-up interview questions, six-dimension L1-L4 capability grading, and cognitive review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Hiring teams and recruiters use this skill to audit candidate resumes, cross-check interview records, grade AI-era capability from L1-L4, and generate follow-up questions or structured reports for AI-related roles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles sensitive candidate resumes and interview transcripts with weak data-handling disclosure. <br>
Mitigation: Use only in environments approved for candidate data, redact unnecessary personal information, and add explicit privacy and retention guidance before deployment. <br>
Risk: Broad activation language could lead to processing uploaded candidate materials without clear user intent. <br>
Mitigation: Require explicit user confirmation before processing resumes, interview notes, or job descriptions. <br>
Risk: Dependency versions are not pinned to reviewed exact versions. <br>
Mitigation: Pin and review dependency versions before installation in production or hiring workflows. <br>


## Reference(s): <br>
- [Resume Audit Guide](references/resume_audit.md) <br>
- [Behavioral Anchors](references/behavioral_anchors.md) <br>
- [Evaluation Matrices](references/evaluation_matrices.md) <br>
- [Interview Modules](references/interview_modules.md) <br>
- [Output Templates](references/output_templates.md) <br>
- [Calibration Cases](references/calibration-cases.md) <br>
- [Cognitive Review Engine](references/cognitive_review.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, guidance] <br>
**Output Format:** [Markdown reports, JSON summaries, interview questions, and structured scoring tables] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include candidate grading levels, confidence notes, risk flags, and follow-up interview prompts.] <br>

## Skill Version(s): <br>
3.3.2 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
