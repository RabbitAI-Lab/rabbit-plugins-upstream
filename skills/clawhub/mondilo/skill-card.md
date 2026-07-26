## Description: <br>
Command-line reference for listing, inspecting, and checking skill availability and eligibility with moltbot skills commands. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mondilo1](https://clawhub.ai/user/mondilo1) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill as a concise CLI reference for moltbot skills commands to list available skills, inspect a named skill, check requirement status, and troubleshoot missing binaries, environment variables, or configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Operational workflows may use API tokens or change remote service state when invoked. <br>
Mitigation: Install only for expected ClawHub/OpenClaw or release workflows, configure tokens with least privilege, and review commands before destructive or public actions. <br>
Risk: Troubleshooting workflows may inspect local environment or configuration values. <br>
Mitigation: Avoid sharing credential values in prompts or logs, and redact sensitive environment or configuration details before distribution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/mondilo1/skills/mondilo) <br>
- [Skills](/tools/skills) <br>
- [Skills config](/tools/skills-config) <br>
- [ClawdHub](/tools/clawdhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [CLI command reference and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
