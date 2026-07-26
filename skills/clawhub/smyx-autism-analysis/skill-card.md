## Description: <br>
Performs video-based analysis of autism-related child behavior characteristics, identifies core symptom features, and returns structured reports with intervention recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, caregivers, educators, and professionals can use this skill to submit child video files or URLs for preliminary autism spectrum behavior analysis, structured screening-style reports, and intervention guidance. The output is for early screening support and does not replace professional medical diagnosis or clinical evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may send child videos or video URLs to the publisher's remote service for analysis. <br>
Mitigation: Use only with proper guardian consent and only when the publisher's privacy, retention, deletion, and access-control terms are acceptable. <br>
Risk: The skill can create or reuse an internal identity, query cloud-stored report history, and persist local authentication tokens. <br>
Mitigation: Run in a controlled environment, review local token storage before deployment, and clear local credentials and report access when no longer needed. <br>
Risk: The analysis is autism-related screening support and may be mistaken for a clinical diagnosis. <br>
Mitigation: Present outputs as preliminary screening information and direct users to qualified medical professionals for diagnosis or clinical evaluation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-autism-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [API interface documentation](artifact/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with recommendations and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
