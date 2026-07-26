## Description: <br>
Assesses health risks from physical exam reports and generates a structured risk profile plus a health management report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[unisound-llm](https://clawhub.ai/user/unisound-llm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Health management teams and physical exam centers use this skill to classify cardiovascular, metabolic, tumor-marker, liver, kidney, and thyroid risks from exam reports and produce time-bound follow-up plans. Outputs are health-management references and are not a substitute for clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Health exam content may be sent to the configured external LLM endpoint and may include sensitive medical data. <br>
Mitigation: Use only when authorized to send the data, remove names and identifiers before use, and follow local health data handling requirements. <br>
Risk: Using an output path stores a generated health risk report locally. <br>
Mitigation: Use local file output only when storage is intended, and protect or delete the report according to the sensitivity of the source data. <br>
Risk: The generated risk assessment may be incomplete or unsuitable for diagnosis. <br>
Mitigation: Treat the output as health-management reference material and route high-risk findings to qualified medical professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/unisound-llm/skills/unisound-health-risk-assessment) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, guidance] <br>
**Output Format:** [JSON followed by a plain-text health risk report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can print to stdout or write a local report file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
