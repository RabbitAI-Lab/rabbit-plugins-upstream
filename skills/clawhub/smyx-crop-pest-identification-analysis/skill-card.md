## Description: <br>
Identifies common crop pests from crop leaf, bud, or fruit images and videos by sending the media to server-side APIs, then returns pest types, counts, confidence scores, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze crop imagery for early pest identification and to retrieve structured pest reports for tomato, corn, peanut, cotton, or other supported crops. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Submitted images, videos, or URLs are sent to the provider's cloud service for analysis. <br>
Mitigation: Review the provider's handling of farm imagery and report history before installing, and submit only media that is approved for cloud processing. <br>
Risk: The skill can silently create or reuse a backend identity and persist authentication tokens in a local SQLite database. <br>
Mitigation: Install only in trusted workspaces, review local identity and token persistence, and clear stored credentials according to workspace policy. <br>
Risk: Pest identification results are advisory and may be incorrect or incomplete. <br>
Mitigation: Use the output as observation support and confirm treatment decisions with qualified agronomy or local plant-protection guidance. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-crop-pest-identification-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown or JSON text with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes pest labels, estimated counts, confidence scores, report links, and historical report tables when requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence; artifact frontmatter states 1.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
