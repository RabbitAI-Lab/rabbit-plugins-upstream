## Description: <br>
Analyzes fixed-camera bedroom video of an elderly person at rest to estimate respiratory rate and flag possible tachypnea or dyspnea risk without providing a medical diagnosis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, elder-care operators, and developers use this skill to submit resting chest or abdomen video, receive a structured respiratory-rate analysis, and review historical cloud reports. It is an assistive monitoring tool and does not replace clinical assessment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Bedroom-health videos and cloud reports may contain highly sensitive personal and health information. <br>
Mitigation: Use the skill only with consent from the monitored person or an authorized caregiver, and confirm the remote service and data handling practices are trusted before deployment. <br>
Risk: The skill may silently create or reuse an internal identity and associate analysis activity with that identity. <br>
Mitigation: Run it in per-user workspaces and verify identity, deletion, and retention practices before use in care settings. <br>
Risk: Authentication tokens may persist in a local workspace database. <br>
Mitigation: Protect local workspaces, restrict access to token storage, and rotate or remove stored credentials when the skill is no longer needed. <br>
Risk: Respiratory-rate alerts are assistive signals and may be incomplete or wrong. <br>
Mitigation: Require human follow-up for urgent alerts and do not treat the output as a diagnosis or substitute for clinical care. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-elderly-tachypnea-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured reports with optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence; SKILL.md frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
