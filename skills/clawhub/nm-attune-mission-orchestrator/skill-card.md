## Description: <br>
Orchestrates the full project lifecycle by auto-detecting state and routing to the correct phase. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to start or resume project workflows, select the appropriate mission type, route through brainstorm, specification, planning, and execution phases, review plans, and persist mission state for recovery. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can reduce routine oversight when users give casual autonomy directives. <br>
Mitigation: Use supervised or checkpoint-heavy settings for sensitive work and avoid casual autonomy phrases when review gates should remain active. <br>
Risk: The skill can create GitHub issues from project artifacts through delegated workflow behavior. <br>
Mitigation: Keep automatic issue creation disabled or review proposed issue text before allowing external-facing actions. <br>
Risk: The skill persists mission state and plan history under .attune, which can retain project details across sessions. <br>
Mitigation: Periodically inspect, redact, or clean the .attune directory, especially before sharing a workspace. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-mission-orchestrator) <br>
- [Metadata homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with structured workflow artifacts and JSON state files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project documents, .attune state/history files, code, tests, and GitHub issues through delegated development skills.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release metadata; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
