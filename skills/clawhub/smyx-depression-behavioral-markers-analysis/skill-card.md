## Description:

Analyzes fixed bedroom and dining-area camera footage to summarize long immobility, lying-in-bed duration, appetite-related behavior changes, and related behavioral alerts for elderly or solo-living individuals.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External care teams, family support workflows, and developers integrating home-care monitoring use this skill to generate behavioral-change summaries from fixed home camera inputs. The skill supports observation and alerting only; it is not a medical diagnostic tool.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles sensitive bedroom and dining-area camera footage for health-related behavioral monitoring.

Mitigation: Use only with explicit informed consent, documented processing and retention terms, and an environment approved for sensitive home-camera health data.

Risk: Security evidence flags plaintext development endpoints and under-disclosed credential persistence.

Mitigation: Do not deploy with real footage until audited HTTPS production endpoints are used and local token storage is removed or secured.

Risk: Behavioral markers may be misunderstood as a depression diagnosis.

Mitigation: Present outputs as observation summaries and escalation prompts only, and require qualified human review for health decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-depression-behavioral-markers-analysis)
- [Publisher profile](https://clawhub.ai/user/18072937735)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries, JSON report data, and shell commands.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and family or community clinician alert text when analysis completes.]

## Skill Version(s):

1.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
