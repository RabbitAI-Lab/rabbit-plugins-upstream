## Description: <br>
Analyzes 30-60 seconds of adult facial video with remote photoplethysmography (rPPG) to produce HRV metrics and trend-oriented stress, fatigue, and cardiovascular wellness signals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and health-management teams use this skill to analyze adult seated facial video or a video URL for HRV metrics, signal quality, historical trends, and report links. It is intended for personal wellness and operational trend monitoring, not medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face video and HRV-derived data are processed by a configured cloud service. <br>
Mitigation: Use the skill only with explicit consent from the person in the video and avoid third-party or non-consensual video URLs. <br>
Risk: Report history is tied to an automatically managed local identity. <br>
Mitigation: Treat historical report retrieval as sensitive and review automatic list triggers before enabling the skill in shared environments. <br>
Risk: Local workspace data can contain account tokens and report linkage state. <br>
Mitigation: Restrict access to the workspace data directory and avoid committing or sharing generated local data files. <br>
Risk: HRV outputs can be mistaken for medical conclusions. <br>
Mitigation: Present results as wellness trend indicators only and do not use them as a substitute for ECG, clinical evaluation, or medical diagnosis. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-facial-hrv-trend-monitoring-analysis) <br>
- [Adult Facial HRV API Documentation](references/api_doc.md) <br>
- [Analysis API Error Codes](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON structured analysis report with HRV metrics, trend fields, status messages, and optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report export links and historical report lists retrieved from the configured cloud service.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
