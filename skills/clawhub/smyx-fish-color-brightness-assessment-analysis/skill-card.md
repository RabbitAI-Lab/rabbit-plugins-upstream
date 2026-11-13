## Description:

Analyzes side-view images or videos of ornamental fish to estimate color vibrancy using HSV measurements and species-specific baselines, then returns a structured assessment report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquarists, aquarium operators, and developers can use the skill to assess ornamental fish coloration from camera images or video and review structured scores and trends. Treat results as color monitoring guidance, not a disease diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan rates this skill suspicious and reports that local media may be sent to a remote service and identity or credential data may be transmitted or stored.

Mitigation: Review the service's data handling before use and submit only media and account information you are authorized to share.

Risk: The security guidance notes that an export-only option may still trigger analysis, and the scan was partial because a referenced local path could not be resolved.

Mitigation: Do not assume an export-only option avoids analysis; review the data flow and the files involved before using it.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [Skill introduction demo](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-color-brightness-assessment-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured JSON reports and Markdown tables with concise text guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include HSV measurements, species-baseline comparisons, vibrancy scores, trends, and husbandry suggestions; detail can be basic, standard, or JSON.]

## Skill Version(s):

1.0.15 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
