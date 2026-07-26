## Description: <br>
Helps agents learn from explicit corrections and self-reflection by maintaining local tiered memory for preferences, project patterns, and recurring lessons. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and agent users use this skill to add self-reflection and memory routines that capture explicit corrections, manage local preference files, and surface learned patterns during future work. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores preferences, corrections, and project details in local memory, which may retain sensitive information longer than intended. <br>
Mitigation: Periodically review stored memory and avoid retaining credentials, confidential preferences, sensitive project details, health data, or third-party personal information. <br>
Risk: The artifact says memory lives under ~/self-improving/ while also directing setup changes to workspace steering files such as AGENTS, SOUL, and HEARTBEAT.md. <br>
Mitigation: Confirm write scope before installation and limit changes to ~/self-improving/ unless broader workspace integration is explicitly approved. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/self-improving) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with file paths and occasional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update local memory files and workspace steering files when explicitly approved.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
