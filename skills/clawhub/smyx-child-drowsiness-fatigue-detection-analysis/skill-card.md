## Description: <br>
Analyzes child or student facial video from a classroom, desk, or online learning setting to estimate drowsiness indicators such as eye closure, PERCLOS, nodding, eye-region glossiness changes, and a 0-100 fatigue score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, guardians, teachers, and administrators can use this skill to analyze child learning-area video and generate structured fatigue indicators, rest reminders, and report links. It is intended as a visual fatigue-assessment aid, not as medical diagnosis or sleep-disorder diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child facial video can be uploaded or submitted to the configured cloud analysis service. <br>
Mitigation: Use only with clear parent, guardian, school, or administrator consent, and require explicit opt-in before any upload or URL-based analysis. <br>
Risk: The skill can silently create or reuse an account-linked identity and retrieve report history. <br>
Mitigation: Deploy only where account-linked history retrieval is expected, disclosed to users, and limited to authorized administrators or guardians. <br>
Risk: Local identity and token storage can expose account-linked access if the workspace is shared or poorly protected. <br>
Mitigation: Store the workspace on protected local storage, restrict file permissions, and review retention and token-handling policies before installation. <br>
Risk: Fatigue scores and reminders may be mistaken for clinical findings. <br>
Mitigation: Present results as visual learning-support signals only, and avoid using the skill as medical diagnosis or sleep-disorder diagnosis. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-drowsiness-fatigue-detection-analysis) <br>
- [Child Drowsiness Fatigue Detection API Documentation](artifact/references/api_doc.md) <br>
- [SMYX Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with fatigue metrics, event summaries, reminders, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local video file input, video URL input, optional report-history listing, and optional output-file writing.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
