## Description:

Analyzes thermal or visible-light imagery of livestock and poultry to flag possible abnormal temperature rises or drops for early screening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Livestock and poultry caretakers can use the skill to screen thermal or visible-light images and videos for individuals with possible temperature abnormalities, then review structured findings and report links. Its results support early screening and are not veterinary diagnoses or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may automatically provision accounts and store login tokens locally.

Mitigation: Require explicit account enrollment and use a separate workspace for each user.

Risk: Selected media is sent to Life Emergence's cloud service, and the export-only option may not prevent uploads.

Mitigation: Confirm that export-only mode works before use and review the service's data-retention terms.

Risk: Image-based temperature findings could be mistaken for a veterinary diagnosis.

Mitigation: Use results for screening only; consult a veterinarian and use appropriate laboratory testing for diagnosis and treatment decisions.

## Reference(s):

- [API reference](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-livestock-fever-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown]

**Output Format:** [Structured analysis results with possible abnormal individuals, estimated temperature ranges, alert levels, and report links; historical report lists are presented as Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the supplied imagery and remote analysis service. The skill provides screening information only, not disease diagnosis or treatment advice.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
