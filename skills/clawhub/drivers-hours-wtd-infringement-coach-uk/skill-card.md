## Description: <br>
Creates a 1-page driver-facing tacho/WTD infringement note plus corrective actions and a review date. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kowl64](https://clawhub.ai/user/kowl64) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Fleet managers, transport compliance staff, and operations teams use this skill to turn driver tacho and working time infringement evidence into a driver-facing coaching note, corrective actions, and a review date. It is intended for evidence-based coaching and escalation support, not standalone legal or disciplinary advice. <br>

### Deployment Geography for Use: <br>
United Kingdom <br>

## Known Risks and Mitigations: <br>
Risk: The bundled RAG escalation rule may not match the user's actual company policy. <br>
Mitigation: Confirm or replace the RAG rule with the current internal policy before using the skill for live compliance work. <br>
Risk: Driver infringement notes may include sensitive employment or compliance data. <br>
Mitigation: Provide only the driver data needed for the note and keep outputs factual, source-attributed, and limited to the relevant review period. <br>
Risk: Outputs could be used in formal HR or disciplinary processes without appropriate review. <br>
Mitigation: Have a manager or compliance owner review generated notes and action plans before using them in any formal process. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kowl64/skills/drivers-hours-wtd-infringement-coach-uk) <br>
- [Company RAG escalation rule](artifact/references/rag-escalation-rule.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance] <br>
**Output Format:** [Markdown files containing a driver infringement note and corrective action plan] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses UK spelling, asks for missing driver or source-record inputs, and keeps outputs factual and evidence-based.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
