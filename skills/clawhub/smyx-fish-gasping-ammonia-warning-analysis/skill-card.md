## Description: <br>
Analyzes aquarium camera images or videos for fish gasping, rapid mouth movement, and increased gill-cover motion to produce a visual risk warning for possible hypoxia or ammonia-related water-quality stress. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and aquarium operators can use this skill to analyze fixed-camera aquarium media and receive structured visual warning reports for fish gasping or abnormal respiration. The skill supports risk triage and recommended next steps, but it should not be treated as a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium videos or URLs may be uploaded to the publisher's cloud service for analysis. <br>
Mitigation: Use the skill only with media the user is willing to send to the publisher service, and obtain explicit confirmation before uploads in sensitive settings. <br>
Risk: The skill can create or reuse an internal account identity and query account-linked report history. <br>
Mitigation: Confirm history lookups before running them and review or remove local workspace data and API-key files when persistent account linkage is not desired. <br>
Risk: The visual warning can be mistaken for a definitive diagnosis or treatment instruction. <br>
Mitigation: Present results as visual risk warnings only, require water-quality testing for confirmation, and refer users to an aquarium veterinarian or aquatic technician for serious or repeated alerts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-fish-gasping-ammonia-warning-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Structured text, Markdown tables, and JSON-style analysis report content] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include alert level, fish behavior metrics, recommended actions, disclaimers, and report links.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
