## Description:

Analyzes submitted pet videos for behaviors associated with separation anxiety and returns structured observations, suggested interventions, and report links.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and animal care staff can review video recorded while a pet is alone, receive observations about possible separation-related behaviors, and view suggested support strategies or past reports. The results are for behavioral observation, not medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private recordings may still be uploaded when `--export-env-only` is used, and `--api-url` is not a reliable privacy control.

Mitigation: Do not rely on these options to prevent uploads; confirm the service's recording retention and deletion practices before sending private footage.

Risk: Account credentials are handled without clear user control.

Mitigation: Use a dedicated service identity and protect the local credential database.

Risk: The package does not verify remote service behavior, and the analysis is not continuous monitoring or an automatic comfort-device system.

Mitigation: Treat results as on-demand cloud analysis and do not rely on them as continuous supervision or automatic intervention.

Risk: Behavior observations may be mistaken for a medical assessment.

Mitigation: Use results as behavioral observations only; consult a veterinarian or qualified behavior professional about severe distress.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-separation-anxiety-relief-analysis)
- [API interface notes](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured behavior report; history listings can be presented as Markdown tables.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [On-demand analysis of submitted media; may include suggested interventions and report links.]

## Skill Version(s):

1.0.14 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
