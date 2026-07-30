## Description: <br>
Suggests next actions after task completion, including optional Stop-hook and UserPromptSubmit-hook automation for detecting completed work, stalled follow-up steps, and workflow decision points. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to surface concrete follow-up choices after completed work, including verification, commit, PR, cleanup, and stalled-work recovery paths. It can also automate next-action prompts in supported hook environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad automatic workflow authority can steer follow-up work without being explicitly requested when hooks are installed. <br>
Mitigation: Install only when automatic workflow orchestration is desired, review hook registration, and disable the Stop or UserPromptSubmit hooks when only manual suggestions are wanted. <br>
Risk: Local debug logs may retain transcript paths and short content snippets from recent assistant messages. <br>
Mitigation: Review log contents, keep logs local and access-controlled, and redact or disable debug logging where conversation metadata or snippets are sensitive. <br>
Risk: Next-action options can propose external workflow steps such as commits, pushes, PRs, or cleanup actions. <br>
Mitigation: Treat generated options as proposals, confirm the selected action before execution, and keep PR creation in draft mode unless the user explicitly chooses a ready-for-review path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next) <br>
- [Publisher profile](https://clawhub.ai/user/drumrobot) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Stall detection topic](artifact/stall-detect.md) <br>
- [Ask gates topic](artifact/ask-gates.md) <br>
- [Suggestion patterns topic](artifact/suggestion-patterns.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with structured next-action options and optional JSON hook outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May invoke follow-up skills, ask the user to choose next actions, or emit hook decision/context JSON when installed as a local automation hook.] <br>

## Skill Version(s): <br>
0.7.0 (source: server release metadata and CHANGELOG.md, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
