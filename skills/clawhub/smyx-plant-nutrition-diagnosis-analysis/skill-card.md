## Description: <br>
Diagnoses plant nutrient deficiency or excess from plant leaf images or videos and returns structured fertilization guidance for precision nutrient management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze plant leaf media, identify likely nutrient deficiency or excess, and receive structured diagnostic findings with fertilization suggestions. It can also query cloud-hosted historical diagnosis reports associated with the skill's internal account identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends plant media to a cloud service and should not be treated as an offline-only image-analysis helper. <br>
Mitigation: Use it only with media approved for that cloud workflow, and confirm the service's data handling meets the installing organization's requirements. <br>
Risk: The skill may silently create or reuse a cloud-linked identity and store authentication tokens locally. <br>
Mitigation: Run it in an appropriate workspace, protect or remove local identity and token storage according to policy, and review account linkage before deployment. <br>


## Reference(s): <br>
- [API Interface Documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill usage demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Structured Markdown report text or JSON, with optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may include diagnostic findings, physiological cause analysis, fertilization suggestions, report links, or a Markdown table of historical reports.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter states 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
