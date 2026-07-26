## Description: <br>
Analyzes fixed aquarium camera video to flag visual signs of fish gasping near the surface that may indicate hypoxia or ammonia-related risk. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarium owners, public aquarium operators, aquaculture operators, and developers use this skill to analyze aquarium or pond video for fish gasping patterns and receive structured warning reports with recommended next steps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium images or video and identity-linked report records are sent to the Life Emergence cloud service. <br>
Mitigation: Use only with media and report data approved for that service, and avoid submitting sensitive or unnecessary footage. <br>
Risk: The skill can create or reuse a local account record and store returned service tokens in the workspace database. <br>
Mitigation: Run in an isolated workspace when possible, and review or clear shared workspace data such as data/smyx-api-key.txt before use. <br>
Risk: Visual warnings could be mistaken for a diagnosis or automatic treatment instruction. <br>
Mitigation: Treat outputs as risk warnings only; confirm water quality and consult an aquarium veterinarian or aquatic technician before medication or other high-impact action. <br>


## Reference(s): <br>
- [Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured report text, with optional report export link.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include warning level, observed fish behavior metrics, recommended non-medication actions, disclaimers, and history-report listings from the cloud service.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
