## Description: <br>
Real-time detection of flames and smoke in video and image scenes, suitable for fire early warning in industrial parks, forests, warehouses, and other locations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, safety teams, and developers use this skill to submit surveillance images, video files, or media URLs for fire and smoke analysis, receive structured detection reports, and query account-linked historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded fire or smoke imagery, video URLs, and account-linked report history are sent to a vendor cloud service. <br>
Mitigation: Use only with media approved for vendor processing, and review retention, deletion, billing, and account-control expectations before deployment. <br>
Risk: The skill can create or reuse an internal account identity and store service tokens in a local workspace database. <br>
Mitigation: Run it in a controlled workspace, restrict access to workspace data, and review local credential-storage expectations before use. <br>
Risk: Fire and smoke detections are advisory and may not be sufficient for emergency confirmation. <br>
Mitigation: Treat results as safety-warning support and require professional site confirmation and emergency response procedures for suspected fires. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fire-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Fire detection API documentation](references/api_doc.md) <br>
- [Common analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands] <br>
**Output Format:** [Markdown report text or JSON, with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include detection results, risk notes, report links, and historical report tables; documented media inputs are jpg/jpeg/png/mp4/avi/mov up to 10MB.] <br>

## Skill Version(s): <br>
1.0.14 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
