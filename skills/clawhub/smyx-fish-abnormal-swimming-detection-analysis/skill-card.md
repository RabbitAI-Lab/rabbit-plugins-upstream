## Description: <br>
Analyzes aquarium camera images or videos to flag visual fish swimming-posture abnormalities such as side-swimming, upside-down posture, axial rotation, floating, or sinking, and reports abnormal-duration ratios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Aquarium keepers, aquarium operators, and agents use this skill to analyze fixed-camera fish media, produce structured posture-monitoring reports, and review historical cloud reports. The output is visual posture analysis and suggested next actions, not a veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Aquarium media or media URLs may be sent to the configured cloud service. <br>
Mitigation: Use the skill only when the service's retention and account controls are acceptable, and avoid sensitive or private camera footage. <br>
Risk: The skill can silently create or reuse an internal identity, store tokens locally, and fetch prior cloud history. <br>
Mitigation: Install and run it in a contained workspace, review account behavior before deployment, and limit use to authorized users and media. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, configuration] <br>
**Output Format:** [Markdown and JSON analysis reports with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an optional output file when requested; historical report queries return structured cloud report records.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
