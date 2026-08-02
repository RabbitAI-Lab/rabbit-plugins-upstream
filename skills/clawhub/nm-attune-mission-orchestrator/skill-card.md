## Description: <br>
Orchestrates full project lifecycle by auto-detecting state and routing to the correct phase. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to start or resume project missions across brainstorming, specification, planning, and execution. It detects existing project artifacts, selects the mission type, routes phases to related Attune skills, and records mission state. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reduce routine checkpoints based on casual wording or auto mode. <br>
Mitigation: Use explicit constraint flags when oversight matters, and review any reduced-checkpoint configuration before starting a mission. <br>
Risk: The skill can create GitHub issues from project documents. <br>
Mitigation: Disable automatic issue creation where available and review generated issue content before allowing external-facing actions. <br>
Risk: Mission state files may contain sensitive project details. <br>
Mitigation: Clear or redact .attune state and history files before sharing the workspace or publishing artifacts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-mission-orchestrator) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [OpenClaw homepage metadata](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown and structured project artifacts with optional shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project planning documents, .attune state files, and GitHub issues through delegated phase workflows.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
