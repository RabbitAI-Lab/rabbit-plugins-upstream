## Description: <br>
Manager Self Evolution enables an agent manager to self-diagnose, identify defects, track improvements, and maintain skill health without relying on external prompts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wjl1004](https://clawhub.ai/user/wjl1004) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators of OpenClaw manager agents use this skill to run local self-diagnosis, health scoring, and improvement logging before tasks, during heartbeat checks, and after failures. It helps maintain discipline around memory, principles, installed skills, and secrets-audit status. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads local memory, principles, recent notes, and installed skill files during self-audits. <br>
Mitigation: Enable it only in workspaces where local self-audit of those files is expected, and review findings before acting on them. <br>
Risk: Broad heartbeat, daily, and task-before triggers can add routine self-audit output and evolution-log writes. <br>
Mitigation: Keep triggers manual or scoped when continuous self-auditing or Chinese-only output is not desired. <br>
Risk: The skill writes a local evolution log that may contain operational observations. <br>
Mitigation: Review the log location and retention practices so sensitive notes are not kept longer than intended. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wjl1004/skills/manager-self-evolution) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown documentation with inline bash examples and plain-text diagnostic output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or appends a local evolution-log.md when diagnostic checks record issues; output may be in Chinese.] <br>

## Skill Version(s): <br>
1.1.0 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
