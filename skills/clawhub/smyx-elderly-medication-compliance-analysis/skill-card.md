## Description: <br>
Analyzes medication-area video to detect whether an elder picked up medication, brought it to the mouth, and showed a swallow, then returns a compliance status and report link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, elder-care operators, and developers use this skill to analyze fixed-camera video from medication areas and confirm whether the pick-up, to-mouth, and swallow steps were observed. It supports compliance reporting and caregiver follow-up without providing medical dosage or treatment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Medication-area video and report history may include sensitive home health information and may be sent to a configured cloud service. <br>
Mitigation: Confirm consent from monitored elders or caregivers before use, verify the configured cloud destination, and review who can access history reports and export links. <br>
Risk: The skill can create or reuse local identity state and persist tokens in the workspace data directory. <br>
Mitigation: Review local workspace storage and access controls before installation, and clear stored identity or token data when the skill is no longer needed. <br>
Risk: A visual compliance result may be incomplete or wrong and should not be treated as medical advice. <br>
Mitigation: Use the result as an auxiliary adherence signal only, and require caregiver confirmation before acting on missed-dose or incomplete-swallow alerts. <br>


## Reference(s): <br>
- [API interface documentation](references/api_doc.md) <br>
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files] <br>
**Output Format:** [Markdown or JSON structured analysis report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include detected steps, missed steps, compliance status, confidence, event timestamps, alert text, snapshot URLs, report links, and exported result files.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
