## Description: <br>
Analyzes video inputs for mental-health and behavioral signals, returning structured psychological analysis reports, risk indicators, improvement suggestions, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to submit local video files or video URLs to a cloud analysis service for mental-health tendency analysis and to retrieve prior reports. It is positioned for employee care, campus screening, and home health monitoring workflows where outputs are treated as reference material rather than clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive video or image inputs and psychological analysis results are processed by the publisher's cloud service and may be linked to an internal identity. <br>
Mitigation: Use only with informed consent, approved data handling, and clear retention, deletion, and account-isolation terms before applying it to real mental-health, workplace, or campus screening data. <br>
Risk: The skill can silently create or reuse local authentication state and user identity. <br>
Mitigation: Review token storage and identity isolation before deployment, and run the skill in an isolated account or environment for each intended user population. <br>
Risk: Psychological analysis outputs may be mistaken for clinical diagnosis or treatment advice. <br>
Mitigation: Present outputs as reference-only screening information and require professional review or referral for users with meaningful psychological distress. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychology-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown reports or JSON, with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local mp4, avi, and mov files or video URLs; documented file size limit is 10 MB.] <br>

## Skill Version(s): <br>
1.0.13 (source: server release metadata and auto changelog; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
