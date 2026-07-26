## Description: <br>
Through fixed enclosure cameras, the skill analyzes turtle mouth and nasal media to identify frequent open-mouth breathing in non-feeding states, visible mucus, and nasal discharge that may warrant a pneumonia risk warning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, animal-care operators, and developers use this skill to analyze turtle enclosure images or videos for visual respiratory warning signs and to produce structured risk reports, recommendations, report links, or historical report tables. The output is a visual risk assessment aid and is not a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends turtle enclosure media or video URLs to the Life Emergence backend for analysis. <br>
Mitigation: Use only media and URLs that are appropriate for cloud processing, and avoid URLs that contain embedded access tokens or other sensitive values. <br>
Risk: The skill can create or reuse a cloud-linked identity and persists login tokens and identity records locally. <br>
Mitigation: Review and manage the workspace data directory before and after use, especially in shared environments. <br>
Risk: Historical report queries are served from the cloud and can reveal prior analysis records associated with the linked identity. <br>
Mitigation: Run history queries only in contexts where the linked identity and its report history are intended to be used. <br>
Risk: The skill provides visual health risk warnings that could be mistaken for a veterinary diagnosis. <br>
Mitigation: Treat results as visual screening guidance only and consult a qualified reptile veterinarian for diagnosis and treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-turtle-pneumonia-symptom-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown or JSON-like structured report with shell command examples and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May query cloud-hosted analysis and history APIs and may save requested output to a file.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter states 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
