## Description: <br>
Codex Conductor orchestrates spec-driven software delivery for Codex CLI across greenfield or brownfield projects with gated or autonomous execution, gate tracking, validation evidence, documentation updates, and reusable agent workflow guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[shalomobongo](https://clawhub.ai/user/shalomobongo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate end-to-end software delivery through explicit specs, staged gates, delegated coding-agent tasks, validation evidence, and continuously updated project documentation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create or update project documentation and orchestrator state in the target workspace. <br>
Mitigation: Use it in a version-controlled workspace and review diffs after scaffold and documentation steps. <br>
Risk: The skill can run validation shell commands and delegate tasks to configured coding-agent CLIs. <br>
Mitigation: Inspect generated prompts and commands, run them in a controlled workspace, and avoid passing secrets through prompts, validation commands, or logs. <br>
Risk: Gate precondition bypasses such as --no-enforce can weaken the intended review process. <br>
Mitigation: Treat bypass use as an audit exception and record why it was needed. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/shalomobongo/skills/codex-conductor) <br>
- [Spec-Driven Development](references/spec-driven-development.md) <br>
- [Planning Questionnaire](references/planning-questionnaire.md) <br>
- [Modes](references/modes.md) <br>
- [Gate Checklists](references/gate-checklists.md) <br>
- [Testing Matrix](references/testing-matrix.md) <br>
- [Manual Test Templates](references/manual-test-templates.md) <br>
- [Codex Runbook](references/codex-runbook.md) <br>
- [Gate Prompt Templates](references/gate-prompts.md) <br>
- [Research Playbook](references/research-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, Code] <br>
**Output Format:** [Markdown guidance with shell command examples, generated prompts, JSON gate status, and project documentation files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Creates or updates project docs and .orchestrator state; can invoke configured coding-agent CLIs through provided scripts.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
