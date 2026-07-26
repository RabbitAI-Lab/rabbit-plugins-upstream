## Description: <br>
Guide for creating effective skills. This skill should be used when users want to create a new skill (or update an existing skill) that extends Claude's capabilities with specialized knowledge, workflows, or tool integrations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[yixinli867](https://clawhub.ai/user/yixinli867) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and skill authors use this skill to design, create, package, and iterate on agent skills with clear structure, concise instructions, and appropriate supporting resources. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may lead an agent to run helper script commands for scripts that are not included in the package. <br>
Mitigation: Before executing initialization or packaging commands, confirm the exact script paths and verify they come from the intended skill tooling. <br>
Risk: Generated skill guidance could introduce incorrect or misleading instructions into downstream skills. <br>
Mitigation: Review and scan created or modified skills before deployment. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands] <br>
**Output Format:** [Markdown guidance with inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide agents to propose or run local skill initialization and packaging commands.] <br>

## Skill Version(s): <br>
0.1.0 (source: server-resolved release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
