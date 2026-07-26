## Description: <br>
SecOpsAI for OpenClaw helps agents run the live SecOps detection pipeline, inspect findings, triage incidents, and get mitigation guidance from chat. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[techris93](https://clawhub.ai/user/techris93) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Security operators, OpenClaw administrators, and developers use this skill to review OpenClaw audit-log findings, run local SecOps checks, investigate incidents, and request mitigation guidance. The skill is suited to chat-driven triage workflows where read-only review is the default and write actions require confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can execute shell commands through the local secopsai CLI. <br>
Mitigation: Install only from trusted sources and review commands before execution, especially in environments with sensitive audit logs. <br>
Risk: Triage close, orchestrate, and apply-action workflows can modify the local SOC store. <br>
Mitigation: Use read-only commands first, require explicit confirmation for write actions, and confirm finding IDs and dispositions before applying changes. <br>
Risk: Unattended automation can apply operational changes without enough review. <br>
Mitigation: Run scheduled jobs under a controlled account, ensure automated writes are intended, and back up the SOC database before unattended automation. <br>
Risk: Audit-log summaries and finding details may expose sensitive security information. <br>
Mitigation: Treat generated summaries and command output as sensitive and share them only with authorized users. <br>


## Reference(s): <br>
- [SecOpsAI for OpenClaw on ClawHub](https://clawhub.ai/techris93/secopsai-skill) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown responses with inline shell commands and parsed JSON summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs may summarize local security findings, proposed triage actions, mitigation steps, and command results from the secopsai CLI.] <br>

## Skill Version(s): <br>
0.3.6 (source: release evidence and changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
