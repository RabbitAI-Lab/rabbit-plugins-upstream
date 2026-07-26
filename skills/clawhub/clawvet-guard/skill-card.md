## Description: <br>
Vet any OpenClaw skill for prompt injection, credential theft, and RCE before you install it. Runs a clawvet scan and blocks risky installs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohibshaikh](https://clawhub.ai/user/mohibshaikh) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to scan OpenClaw skills before installation, review risk grades and findings, and block skills that show high-risk behavior. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can ask the agent to run Bash commands with npx to execute clawvet scans. <br>
Mitigation: Install only when that execution model is acceptable, and review the exact command and target before running scans. <br>
Risk: Scanner results may miss issues in unknown third-party skills or be treated as stronger assurance than they provide. <br>
Mitigation: Treat scan results as evidence for review, surface high and critical findings, and require user approval before proceeding on moderate risk results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohibshaikh/skills/clawvet-guard) <br>
- [Server-resolved GitHub provenance](https://github.com/MohibShaikh/clawvet/tree/master/skills/clawvet-guard) <br>
- [Source repository](https://github.com/MohibShaikh/clawvet) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON scan-result interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke npx clawvet scans that return riskGrade, riskScore, findingsCount, and findings details.] <br>

## Skill Version(s): <br>
0.1.0 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
