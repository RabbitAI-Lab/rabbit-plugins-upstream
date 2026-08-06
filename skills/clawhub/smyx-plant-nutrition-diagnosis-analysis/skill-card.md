## Description: <br>
Diagnoses plant nutrient deficiency or excess from plant media using computer vision and plant physiology, then returns targeted fertilization suggestions for precision nutrient management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, and agricultural support teams use this skill to analyze plant leaf images or videos for nutrient deficiency or excess and receive structured fertilization guidance. Agents can also retrieve cloud-hosted historical diagnosis reports for the associated user identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant media and associated identifiers are sent to external Life Emergence APIs for cloud processing. <br>
Mitigation: Use the skill only with media and identifiers approved for cloud processing, and avoid sensitive or unrelated imagery. <br>
Risk: The skill may silently create or reuse an account identity and store user and token records locally. <br>
Mitigation: Run it only in trusted workspaces, review local workspace data retention practices, and clear local records when they are no longer needed. <br>
Risk: Historical report retrieval is cloud-backed and tied to the associated identity. <br>
Mitigation: Enable history lookup only when cloud retrieval of prior reports is acceptable for the user and deployment context. <br>
Risk: Fertilization recommendations may be incomplete without local agronomic context. <br>
Mitigation: Treat results as decision support and confirm final fertilization plans with soil testing, crop conditions, and local agricultural guidance. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-nutrition-diagnosis-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Interface Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, files] <br>
**Output Format:** [Markdown text with structured JSON report content and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include diagnosis details, fertilization suggestions, cloud report links, or cloud history records.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; SKILL.md frontmatter reports 1.0.10) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
