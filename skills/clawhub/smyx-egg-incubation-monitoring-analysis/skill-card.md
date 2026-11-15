## Description:

Analyzes images of turtle or snake eggs for visible development signs and produces incubation monitoring reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile breeders and incubator operators use the skill to review turtle or snake egg images, track visible development signals, and consult incubation reports and report history.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags identity and token handling beyond the stated egg-monitoring purpose.

Mitigation: Review the identity and token flow before use, and avoid sharing credentials or internal identity values with the skill.

Risk: The security review reports possible uploads of submitted media to an external service.

Mitigation: Submit only images or videos you are authorized to share, after reviewing the destination service and its data terms.

Risk: The security review says the export-only option still runs analysis; it also notes that the scan was partial and the imported analysis service could not be verified.

Mitigation: Treat export-only as an analysis run, avoid sending sensitive media, and confirm the service behavior before relying on it.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis)
- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Structured JSON analysis reports and Markdown history tables with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports describe visible development signals and suggested actions.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
