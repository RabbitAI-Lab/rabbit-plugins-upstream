## Description: <br>
Analyzes aquarium images, videos, or media URLs to identify abnormal fish swimming postures such as side-swimming, upside-down posture, axial rotation, floating, or sinking and return structured monitoring results. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External aquarists, aquarium operators, and developers use this skill to submit aquarium camera footage for visual posture-abnormality analysis, abnormal-duration ratios, alert levels, recommended actions, and history or report lookup. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends aquarium media or media URLs and an automatically resolved identity to the publisher's cloud service. <br>
Mitigation: Use only with appropriate consent and review the deployment's network destinations, data handling, and retention before enabling the skill. <br>
Risk: The skill can create local workspace data that may include account tokens or identity state. <br>
Mitigation: Run it in a constrained workspace, limit access to local data files, and review token retention or cleanup procedures. <br>
Risk: History-report queries may retrieve cloud-stored analysis records associated with the resolved identity. <br>
Mitigation: Constrain when history lookup is triggered and verify that returned records are appropriate for the current user or workspace. <br>
Risk: Visual posture analysis can be mistaken for a veterinary diagnosis. <br>
Mitigation: Treat results as monitoring signals only and require expert or veterinary review before acting on possible disease or water-quality concerns. <br>


## Reference(s): <br>
- [Fish abnormal swimming API documentation](artifact/references/api_doc.md) <br>
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fish-abnormal-swimming-detection-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, files, guidance] <br>
**Output Format:** [Markdown text with structured JSON analysis results, report links, and optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and history-list results when report lookup is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release metadata; artifact frontmatter says 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
