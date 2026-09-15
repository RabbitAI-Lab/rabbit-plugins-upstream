## Description:

Based on computer vision, automatically detects coughing, phlegm, and wheezing frequency, counts the frequency of episodes, used for early health anomaly alerts, helping to detect respiratory diseases in a timely manner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze respiratory monitoring videos or URLs for cough, sputum, and wheeze counts, severity assessment, health warnings, and report links. The results are for health monitoring and early anomaly alerts, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive respiratory videos, report links, identifiers, and cached tokens may expose health-related data.

Mitigation: Treat all uploaded media, generated reports, identifiers, and local token stores as sensitive medical data; require documented upload, retention, access, and deletion handling before deployment.

Risk: Silent identity creation and history retrieval can associate reports with users without explicit consent.

Mitigation: Gate account creation and historical report lookup behind clear user consent and organization-approved identity scoping.

Risk: Released configuration includes plaintext or development endpoints.

Mitigation: Use HTTPS production endpoints only and verify endpoint configuration before installation or execution.

Risk: The skill provides health warnings and medical suggestions that may be mistaken for diagnosis.

Mitigation: Present outputs as monitoring support only and direct users to qualified medical professionals for diagnosis, treatment, or severe symptoms.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-respiratory-symptom-recognition-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [呼吸道症状智能识别分析 API 文档](references/api_doc.md)
- [API接口文档](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON analysis report with symptom counts, severity, warnings, suggestions, and optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write the generated report to a requested output file; historical report queries are returned from the cloud API.]

## Skill Version(s):

1.0.16 (source: server release metadata; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
