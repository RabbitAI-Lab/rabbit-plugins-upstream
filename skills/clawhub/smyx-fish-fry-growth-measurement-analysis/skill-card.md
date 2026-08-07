## Description: <br>
Through fixed cameras of fry tanks with a known-size reference object in view, this skill periodically analyzes fish fry images or videos to measure body length in millimeters, calculate individual growth rate in mm/day, draw growth curves, generate growth reports, and flag anomalies such as growth stagnation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquaculture operators, ornamental fish breeders, laboratory staff, and developers can use this skill to analyze fish fry tank media that includes a known-size reference object, then produce growth measurements, population statistics, growth-rate history, and action-oriented monitoring guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Selected fish-tank media or media URLs may be uploaded to the configured cloud service. <br>
Mitigation: Deploy only where the upload destination, retention expectations, and permitted media types are approved and visible to operators. <br>
Risk: The skill may silently create or reuse an internal account identity and query cloud-stored history. <br>
Mitigation: Use in environments where account identity handling and historical report access are explicitly authorized and reviewable. <br>
Risk: Authentication tokens may be stored in the workspace data directory. <br>
Mitigation: Restrict workspace access, avoid shared workspaces for sensitive deployments, and rotate or remove stored tokens when access is no longer needed. <br>
Risk: Visual body-length measurements can be unreliable when the reference object is missing, not on the same plane as the fish, affected by perspective distortion, or obstructed. <br>
Mitigation: Require a known-size reference object in the same plane, strict overhead capture, confidence checks, and an unreliable-result path instead of reporting precise growth metrics from poor inputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-fry-growth-measurement-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured report text with measurement results, growth statistics, recommendations, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can optionally write analysis output to a user-specified file and can list cloud-stored historical growth reports.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
