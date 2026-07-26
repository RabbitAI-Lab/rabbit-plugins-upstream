## Description: <br>
Intelligent webhook dispatcher with GitHub API fallback. Automatically handles git push failures by routing to GitHub Contents API. Supports retry logic, delivery receipts, and multi-endpoint fan-out. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nima54851](https://clawhub.ai/user/nima54851) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to route failed Git pushes through the GitHub Contents API, retry uploads, produce delivery receipts, and fan out selected updates across repositories. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad authority to change GitHub repository contents through API fallback. <br>
Mitigation: Use a tightly scoped GitHub token and configure explicit repository, branch, and path limits before enabling fallback uploads. <br>
Risk: Automatic fallback and multi-repository fan-out can upload files without enough user confirmation. <br>
Mitigation: Require confirmation before fallback uploads or fan-out dispatches, especially when more than one repository or path is affected. <br>
Risk: Alert webhooks may send metadata to external endpoints. <br>
Mitigation: Disable alert webhooks by default or restrict them to trusted endpoints with known metadata handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nima54851/skills/lingxi-webhook-dispatcher) <br>
- [Publisher profile](https://clawhub.ai/user/nima54851) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON configuration examples, shell command examples, and delivery receipt descriptions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce GitHub API upload instructions, retry summaries, and JSON delivery receipt locations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
