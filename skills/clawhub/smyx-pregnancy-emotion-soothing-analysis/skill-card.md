## Description: <br>
Analyzes authorized fixed-camera video, with optional audio, from pregnancy home or prenatal waiting-room settings to identify emotion-related signals and return structured reports and soothing-action guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and care teams use this skill to submit authorized local files or URLs for pregnancy emotion-signal analysis, historical report lookup, and structured recommendations without producing a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive pregnancy-related camera/audio inputs and remote processing may expose intimate health and household data. <br>
Mitigation: Use only with explicit consent from the pregnant person and anyone recorded, confirm the listed LifeEmergence remote services are acceptable, and avoid deployments without notice and opt-out controls. <br>
Risk: Local identity or token persistence may create account-linkage exposure. <br>
Mitigation: Run the skill only in controlled workspaces where local credential persistence is allowed, and review token storage, rotation, and revocation before installation. <br>
Risk: Claimed smart-speaker and contact-alert interventions are not established by the security evidence. <br>
Mitigation: Treat intervention outputs as advisory until the publisher separately proves opt-in controls, retention limits, and audit logs. <br>
Risk: Pregnancy emotion inference can be mistaken for medical diagnosis or emergency assessment. <br>
Mitigation: Keep outputs limited to observed behavior and soothing guidance, and route recurring or severe concerns to qualified clinicians or appropriate hotlines. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pregnancy-emotion-soothing-analysis) <br>
- [Pregnancy emotion soothing API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance] <br>
**Output Format:** [Plain text or Markdown with JSON-formatted report content and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the generated result to a caller-provided output file.] <br>

## Skill Version(s): <br>
1.0.5 (source: ClawHub release metadata; artifact frontmatter lists 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
