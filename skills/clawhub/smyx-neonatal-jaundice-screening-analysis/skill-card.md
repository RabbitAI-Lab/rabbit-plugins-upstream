## Description: <br>
Screens newborn facial images or short videos for visual jaundice risk indicators, producing low, medium, high, or inconclusive risk hints with follow-up guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, clinical support teams, and developers use this skill to pre-screen newborn facial imagery for visual jaundice risk signals and retrieve structured cloud reports. It is an early attention aid and does not replace clinician diagnosis or bilirubin testing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive newborn face images, videos, and report-history requests are handled through the provider's cloud service. <br>
Mitigation: Use only with guardian consent and confirm the provider's retention, deletion, access-control, and data-handling expectations before deployment. <br>
Risk: The skill may silently create or reuse persistent identity and token state. <br>
Mitigation: Deploy only where silent account creation and local token storage are acceptable, and isolate or rotate local state according to the environment's policy. <br>
Risk: Visual jaundice screening can be misleading if treated as a diagnosis. <br>
Mitigation: Present results as preliminary risk hints and route medium, high, inconclusive, or persistent abnormal results to clinician review and bilirubin testing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-neonatal-jaundice-screening-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Neonatal jaundice screening API documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries and tables with optional JSON detail and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include jaundice risk level, confidence, recommended action, visual feature metrics, and cloud report links.] <br>

## Skill Version(s): <br>
1.0.7 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
