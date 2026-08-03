## Description: <br>
Analyzes adult face images or short videos from a smart mirror, fixed camera, file, or URL to estimate visible fatigue-related facial features and return a non-diagnostic fatigue/stress index from 0 to 100. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, employees, and developers use this skill to submit adult front-facing facial images or short videos for a visual fatigue/stress score, level, contributing features, directional wellness suggestions, and cloud report history. The output is for personal state monitoring and workplace wellness workflows, not medical diagnosis or clinical stress assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face images, videos, URLs, and face-derived reports may be sent to lifeemergence cloud services. <br>
Mitigation: Use only with the subject's consent and avoid submitting sensitive media unless the deployment has appropriate privacy, retention, and deletion controls. <br>
Risk: The skill may create or reuse a persistent local identity or token database for cloud report history. <br>
Mitigation: Avoid shared workspaces unless account separation, history access, and deletion expectations are clear. <br>
Risk: The fatigue/stress score is based on visual facial features and can be affected by lighting, makeup, filters, pose, or image quality. <br>
Mitigation: Present results as non-diagnostic wellness guidance and recommend professional medical follow-up for persistent concerns or symptoms. <br>


## Reference(s): <br>
- [Adult Facial Fatigue / Stress Index API Documentation](references/api_doc.md) <br>
- [Shared Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, API Calls, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown text containing structured JSON-like analysis results, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs a fatigue/stress score, level, contributing facial features, suggestions, and cloud report history when requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
