## Description: <br>
Analyzes user-provided multi-angle pet video files or URLs through server-side APIs to reconstruct 3D body shape, estimate BCS on a 1-9 scale, classify body condition, and return standardized observations without diagnosis or treatment advice. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and pet-health platform operators use this skill to analyze pet body-condition videos for weight-management workflows in smart feeders, pet cameras, and pet health management platforms. It can also query cloud-hosted historical BCS reports for the automatically associated user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet media or supplied media URLs may be sent to lifeemergence.com and open.lifeemergence.com services. <br>
Mitigation: Install only with user consent for that data flow, and avoid private, internal, or sensitive household media URLs unless the publisher provides clearer consent and retention controls. <br>
Risk: The skill can silently create or reuse an automatically managed identity and store service tokens in a local workspace SQLite database. <br>
Mitigation: Review local credential storage, account lifecycle controls, and workspace access before deployment. <br>
Risk: Cloud history queries can retrieve reports linked to the managed identity. <br>
Mitigation: Limit use to contexts where cloud-linked report history is expected, and disclose that history retrieval comes from the publisher's service rather than local memory. <br>


## Reference(s): <br>
- [ClawHub skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-body-condition-score-3d-analysis) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files] <br>
**Output Format:** [Markdown or JSON analysis report with structured BCS observations, report links, and optional saved output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [History-report queries are formatted from cloud API responses; analysis results are not veterinary diagnosis or treatment advice.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
