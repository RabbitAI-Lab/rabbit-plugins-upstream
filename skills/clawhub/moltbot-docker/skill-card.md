## Description: <br>
Enables the bot to manage Docker containers, images, and stacks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mkrdiop](https://clawhub.ai/user/mkrdiop) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use MoltDocker to ask an agent for Docker container, image, and stack management help, including status checks, logs, inspection, start and stop actions, cleanup guidance, and troubleshooting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Docker commands can stop containers, remove images, prune Docker data, or otherwise affect running services and local resources. <br>
Mitigation: Review the exact Docker command and target before execution, and require confirmation for destructive actions such as removing containers, removing images, or pruning Docker data. <br>
Risk: Docker logs, inspect output, and configuration details may expose sensitive information. <br>
Mitigation: Review outputs before sharing them, summarize long command results, and redact secrets or sensitive configuration values. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May summarize long Docker command output for readability.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
