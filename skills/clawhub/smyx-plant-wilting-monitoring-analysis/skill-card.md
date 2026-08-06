## Description: <br>
Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, growers, agronomists, and developers use this skill to analyze plant images, videos, or URLs for early wilting indicators, environmental versus pathological wilt signals, severity grading, and historical report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant media or supplied URLs may be sent to the configured cloud service for analysis. <br>
Mitigation: Use only media and URLs that are approved for external processing; avoid private, internal, or sensitive inputs. <br>
Risk: Report history may be linked to a persistent local identity and tokens may be stored in the workspace data database. <br>
Mitigation: Use an isolated workspace for sensitive testing and review local credential or token storage before deployment. <br>
Risk: Security evidence marks the release as suspicious and requiring review. <br>
Mitigation: Review and scan the skill before deployment, with particular attention to cloud identity handling, token storage, and outbound data transfer. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis) <br>
- [API interface documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, API Calls, Markdown, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved output file and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can return structured plant wilting monitoring results, recommendations, report links, or a Markdown table of cloud report history.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.11) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
