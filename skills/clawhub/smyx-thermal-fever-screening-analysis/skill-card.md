## Description: <br>
Analyzes multi-person thermal-camera images or videos to flag relative skin-temperature anomalies and recommend thermometer recheck without making a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze thermal-camera footage from multi-person gatherings, produce structured relative-temperature screening results, and query prior cloud reports. It is intended as a health-screening aid and directs users to confirm anomalies with a calibrated thermometer. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill handles thermal or health-adjacent videos, participant information, generated reports, and local account tokens through Life Emergence cloud endpoints. <br>
Mitigation: Install and run it only when those endpoints are trusted for the captured media and reports, and avoid shared workspaces unless identity and report access are isolated. <br>
Risk: Thermal footage of people in homes, meetings, kindergartens, or nursing-home areas can expose sensitive health and privacy information. <br>
Mitigation: Get explicit consent from people captured in the footage and store reports and media with appropriate access controls. <br>
Risk: Relative temperature anomalies can be affected by camera limits, face visibility, masks, hats, exercise, hot drinks, sun exposure, air conditioning, or nearby heat sources. <br>
Mitigation: Treat results as screening guidance only and confirm any alert with a calibrated thermometer or qualified medical evaluation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-thermal-fever-screening-analysis) <br>
- [API Documentation](artifact/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include relative-temperature deltas, anomaly counts, recheck guidance, and historical report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
