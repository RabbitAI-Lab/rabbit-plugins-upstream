## Description: <br>
Estimates relative nighttime plant respiration intensity from thermal canopy imagery or video, with optional CO2 context, and returns structured results, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze nighttime thermal plant imagery or video for plant factories, artificial climate chambers, and closed greenhouses. It helps estimate a relative respiration index, classify metabolic activity, surface abnormal conditions, and provide nighttime environment-control guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant images, videos, or supplied URLs may be sent to lifeemergence.com services for analysis. <br>
Mitigation: Review the skill before installation and only submit media or URLs that the user is authorized to process with the external service. <br>
Risk: The skill may create or reuse a local identity and retrieve identity-linked history. <br>
Mitigation: Run it in an appropriate workspace or account context, and review historical-report queries before using the list function. <br>
Risk: Service tokens may be stored in a workspace SQLite database. <br>
Mitigation: Restrict workspace access and clear or rotate stored credentials according to local security policy after use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-night-respiration-rate-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON text with command examples, structured analysis results, recommendations, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an optional output file when the --output parameter is used.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
