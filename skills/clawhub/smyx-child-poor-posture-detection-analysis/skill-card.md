## Description: <br>
This skill analyzes children's posture videos from a desk or lamp-mounted camera to estimate spinal curvature and head tilt, then returns posture findings, voice reminder text, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators of smart study lamps, home study desks, or classroom monitoring workflows use this skill to analyze child posture videos, trigger posture reminder text, and review cloud-backed posture reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Children's posture videos or URLs may be sent to the configured cloud service for analysis. <br>
Mitigation: Use only with guardian consent, start with non-sensitive test videos, and confirm the configured service is appropriate for the deployment environment. <br>
Risk: Cloud reports may be associated with an automatically managed identity, and local tokens or profile data may be stored in the workspace. <br>
Mitigation: Use a dedicated workspace and account, avoid shared environments, and clear local state or tokens according to organizational policy. <br>
Risk: Visual posture angles are estimates and can be unsuitable for medical decisions. <br>
Mitigation: Use outputs as habit reminders and posture summaries only; seek qualified medical review for health concerns or diagnosis. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-style structured reports, with optional shell commands for running the bundled script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include posture metrics, voice reminder text, history tables, and report links.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release evidence; artifact frontmatter says 1.0.4) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
