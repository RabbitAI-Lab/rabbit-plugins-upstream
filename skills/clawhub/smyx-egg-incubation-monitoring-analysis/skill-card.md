## Description: <br>
Analyzes turtle or snake egg images and videos to detect visual development signals, classify incubation stage, and generate incubation progress reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External reptile breeders, hatchery operators, and smart-incubator workflows use this skill to analyze egg images or videos for fertilization, vascular development, embryo signals, mold, and unreliable-input conditions. It returns structured monitoring results, suggested handling posture, history lookups, and report links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Egg images, videos, URLs, and report-history requests are sent to remote lifeemergence.com services. <br>
Mitigation: Use the skill only when users consent to remote processing and understand what media or URLs will be transmitted. <br>
Risk: The skill may create or reuse a local identity and store returned session tokens in a workspace SQLite database. <br>
Mitigation: Run it in a controlled workspace, review token storage behavior before deployment, and clear local credentials when they are no longer needed. <br>
Risk: Incubation-stage classifications and handling suggestions can affect breeding decisions if the input image is poor or the remote analysis is wrong. <br>
Mitigation: Treat results as decision support, verify important cases against species-specific incubation records and image quality checks, and consult a qualified reptile breeding professional for high-risk outcomes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-egg-incubation-monitoring-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or plain-text reports with JSON detail output and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write results to a file when an output path is provided; uses remote lifeemergence.com services for analysis and report history.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter says 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
