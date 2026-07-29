## Description: <br>
Analyzes thermal-camera images or videos of multi-person gatherings to identify relative skin-temperature anomalies and recommend confirmation with a calibrated thermometer. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to screen thermal-camera media from homes, meeting rooms, kindergartens, nursing-home activity areas, or similar gathering spaces for relative body-temperature anomalies. It reports directional screening results and report links, but it is not a medical diagnosis tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Thermal household or public-area videos may contain sensitive health-related information and are sent to the vendor cloud service. <br>
Mitigation: Use the skill only with informed consent from recorded people, avoid unnecessary uploads, and handle resulting reports as sensitive health-adjacent data. <br>
Risk: The skill silently creates or reuses a local identity and associates cloud report history with that identity. <br>
Mitigation: Deploy only where identity separation, report access, and workspace sharing are understood and reviewed before use. <br>
Risk: Relative thermal anomalies can be affected by sensor quality, environmental conditions, face coverage, recent activity, hot drinks, or nearby heating and cooling sources. <br>
Mitigation: Treat alerts as screening guidance only and confirm any concern with a calibrated thermometer or appropriate medical evaluation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [Thermal Fever Screening API Documentation](references/api_doc.md) <br>
- [General Analysis API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-formatted structured analysis results with report links and suggested follow-up actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs relative temperature anomaly findings, cloud report history, and export links; results depend on valid thermal-camera input and vendor cloud service availability.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
