## Description: <br>
Estimates livestock body length and weight from side-view images, videos, or URLs and returns structured measurements, fattening-stage assessment, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External farmers, livestock operators, and agents use this skill to submit side-view livestock media for contactless body-size and weight estimates and to retrieve account-bound history reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uploads livestock media to a remote cloud service for processing. <br>
Mitigation: Use only media and URLs intended for that service, and avoid private farm footage or internal/private URLs unless sharing them with the service is approved. <br>
Risk: The skill silently creates or reuses an internal cloud identity and account-bound report history. <br>
Mitigation: Run it only in workspaces where account-bound history is expected, and review access controls before use in shared environments. <br>
Risk: The security evidence notes local storage of service tokens in the workspace data area. <br>
Mitigation: Limit workspace access, clean stored tokens when decommissioning the skill, and avoid running it in untrusted shared workspaces. <br>
Risk: Body size, weight, and fattening-stage outputs are estimates and may be affected by pose, occlusion, reference-object quality, lighting, and video quality. <br>
Mitigation: Use outputs as monitoring references and verify operational decisions with established weighing equipment and farm management procedures. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON text, with optional saved text output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include estimated body measurements, weight, fattening stage, confidence or usability notes, report links, and account-bound history listings.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; SKILL.md frontmatter reports 1.0.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
