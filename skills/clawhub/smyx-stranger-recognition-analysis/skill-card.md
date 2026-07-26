## Description: <br>
Identifies strangers in surveillance images or video through face comparison and returns structured recognition results, warnings, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security operators, facilities teams, and developers use this skill to analyze surveillance images or video for unknown faces, compare detections against a known-person database, and review structured warnings or historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Biometric surveillance images, videos, or URLs may be sent to the provider's cloud service. <br>
Mitigation: Use only media the operator is authorized to process, and confirm consent, lawful basis, retention, and deletion responsibilities before deployment. <br>
Risk: The skill can create or reuse local identity state and store service tokens in the workspace data directory. <br>
Mitigation: Run it only in controlled workspaces, restrict access to workspace data, and remove or rotate local identity and token files when no longer needed. <br>
Risk: Face recognition output may be inaccurate or incomplete for consequential security decisions. <br>
Mitigation: Treat reports as decision support, require human review before action, and document escalation procedures for uncertain matches. <br>


## Reference(s): <br>
- [API Reference](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-stranger-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown reports with optional JSON payloads and saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return recognition summaries, warning details, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.7 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
