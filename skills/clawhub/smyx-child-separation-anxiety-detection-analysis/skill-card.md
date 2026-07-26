## Description: <br>
Analyzes fixed-camera pre-school drop-off videos to identify crying expressions, clinging or resistance behaviors, and produce a mild, moderate, or severe separation-anxiety level with supportive guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Parents, teachers, and operators of child-care monitoring workflows use this skill to analyze home-entrance or kindergarten-gate video and generate behavior observations, trend alerts, and calming recommendations. It is intended as supportive visual analysis, not a clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill processes highly sensitive child-related video or video URLs through a cloud service. <br>
Mitigation: Use only with appropriate guardian and school consent, review the remote service and retention practices, and prefer privacy-preserving capture such as masking where practical. <br>
Risk: The security evidence says the skill automatically creates or reuses persistent identities with locally stored tokens. <br>
Mitigation: Install only in environments where that identity behavior is acceptable, restrict local token access, and clear stored credentials when the workflow is no longer needed. <br>
Risk: The security verdict is suspicious because the data flow combines sensitive media upload with persistent identity binding. <br>
Mitigation: Review the skill carefully before deployment, limit use to the intended child-care monitoring scenario, and avoid using outputs as clinical diagnosis or prescription. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-child-separation-anxiety-detection-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Files] <br>
**Output Format:** [Markdown or JSON analysis report with behavior metrics, anxiety level, recommendations, and optional report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can write the report to a user-specified output file and can list historical cloud reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
