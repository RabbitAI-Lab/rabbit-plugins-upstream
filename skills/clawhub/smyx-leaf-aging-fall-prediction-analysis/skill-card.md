## Description: <br>
Analyzes indoor houseplant image or video sequences to detect leaf aging indicators and predict likely leaf-fall risk windows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, plant-care operators, and developers can use this skill to analyze fixed-angle indoor plant media, identify senescence signs, produce structured reports, and query prior cloud-generated reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says the skill uploads plant images, videos, or URLs to the lifeemergence cloud service. <br>
Mitigation: Use only media that is appropriate to send to that service, and avoid sensitive home-camera footage unless retention, account, and deletion practices are acceptable. <br>
Risk: The security review says the skill can create or reuse a local identity and store access tokens in the workspace. <br>
Mitigation: Review the generated local identity and token storage before installation, and install only in workspaces where that credential behavior is acceptable. <br>
Risk: The security verdict is suspicious and calls for review before installation. <br>
Mitigation: Review the skill and its scan results before deployment, especially cloud upload and credential-handling behavior. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-leaf-aging-fall-prediction-analysis) <br>
- [API Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis text with report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save analysis output to a local file when an output path is provided.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
