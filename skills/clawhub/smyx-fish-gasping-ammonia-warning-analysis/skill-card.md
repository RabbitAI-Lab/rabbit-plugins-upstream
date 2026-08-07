## Description: <br>
Analyzes aquarium camera images or videos for fish gasping, rapid mouth movement, and intensified gill movement, then reports a visual warning for possible ammonia poisoning or hypoxia. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, aquarium operators, and developers use this skill to analyze aquarium video or image inputs for visual warning signs of fish gasping and to receive structured risk reports, suggested water-quality checks, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads aquarium media to the LifeEmergence/Open API backend for cloud analysis. <br>
Mitigation: Use only aquarium media that is acceptable to send to that backend, and avoid sensitive local files or private surroundings in the camera frame. <br>
Risk: The skill silently creates or reuses a cloud identity and stores access tokens in the workspace data directory. <br>
Mitigation: Run it in a workspace where account-linked token storage is acceptable, and clear the workspace data directory when the session should no longer be reused. <br>
Risk: History-report queries retrieve account-linked cloud records. <br>
Mitigation: Avoid broad history queries unless account-linked report retrieval is expected and acceptable for the deployment. <br>
Risk: Visual warning results can be mistaken for a diagnosis or definitive water-quality measurement. <br>
Mitigation: Treat results as warning signals and verify with water testing and qualified aquarium or aquaculture support before making high-impact decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Structured aquarium risk report in Markdown or JSON, optionally with a report export link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are based on provided aquarium media or cloud history queries and may include warning level, observed fish-gasping metrics, recommended checks, and disclaimers.] <br>

## Skill Version(s): <br>
1.0.10 (source: ClawHub release evidence; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
