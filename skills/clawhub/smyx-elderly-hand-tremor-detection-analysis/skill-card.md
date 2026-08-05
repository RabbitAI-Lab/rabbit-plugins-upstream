## Description: <br>
Using a fixed home camera to record video of an elderly person's hand at rest, the skill sends a local video file or video URL for AI motion analysis and returns tremor frequency, amplitude, resting-tremor risk indicators, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, care organizations, and health-monitoring developers use this skill to screen elderly hand-rest videos for periodic resting tremor indicators and to retrieve prior cloud reports. The output is a screening aid and does not replace professional neurological diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive elderly hand videos or video URLs are sent to a remote backend for analysis and report retrieval. <br>
Mitigation: Use only with informed consent from the recorded person or authorized caregiver, and confirm backend retention, deletion, and access controls with the publisher before deployment. <br>
Risk: The skill can create or reuse a local identity and use authentication tokens for analysis history. <br>
Mitigation: Run in an isolated workspace, restrict access to local skill data, and verify account scoping before using history-query features. <br>
Risk: The output provides health-related screening indicators that could be mistaken for diagnosis. <br>
Mitigation: Present results as objective motion-analysis signals and route medium or high risk findings to qualified neurological review. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-elderly-hand-tremor-detection-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown text containing structured JSON-style analysis results, risk indicators, history lists, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the rendered analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
