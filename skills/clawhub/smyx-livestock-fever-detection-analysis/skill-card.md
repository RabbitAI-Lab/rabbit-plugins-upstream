## Description:

Detects abnormal body temperature rise or drop in livestock and poultry from thermal or visible-light imagery, and outputs fever/hypothermia early warnings based on visual thermal features. | 通过热成像或视觉特征识别畜禽体温异常，预警发热。

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Farm operators, veterinarians, and developers use this skill to screen livestock and poultry thermal or visible-light images and videos for body-temperature abnormalities and to retrieve historical fever or hypothermia warning reports. It supports early health screening but does not provide disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media may be uploaded to the configured service for analysis.

Mitigation: Use only media that is approved for the service, and confirm data handling expectations before installation.

Risk: Report history is tied to an automatically managed identity and tokens may be stored in the workspace data directory.

Mitigation: Run the skill in an isolated workspace and review identity and token storage before using it with sensitive data.

Risk: The release includes development HTTP endpoint configuration.

Mitigation: Review and replace endpoint configuration with the intended production or approved service endpoints before use.

Risk: The output is a screening result, not a veterinary diagnosis or treatment recommendation.

Mitigation: Use results as an early-warning signal and escalate suspected disease cases to qualified veterinary or laboratory review.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [Livestock Fever Detection API Documentation](artifact/references/api_doc.md)
- [Common Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files]

**Output Format:** [Markdown or JSON-style structured analysis, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include abnormality levels, estimated temperature ranges, individual locations, report links, and historical report tables.]

## Skill Version(s):

1.0.10 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
