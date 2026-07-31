## Description: <br>
Claudify helps Claude Code users create, improve, persist, and monitor agent automation such as skills, agents, rules, commands, hooks, and plugins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[drumrobot](https://clawhub.ai/user/drumrobot) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use Claudify to turn repeated workflows into Claude Code automation and to review, persist, or monitor automation behavior across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can introduce persistent Claude Code behavior changes through automation files, settings, hooks, memory, failed-attempt records, or Ralph-mode files. <br>
Mitigation: Require previews before writes to ~/.claude, .claude, settings.json, memory, failed-attempts.md, or .ralph files, and prefer project-local scope unless a global change is explicitly intended. <br>
Risk: Hook examples and automation templates may include shell commands or configuration that change future agent behavior. <br>
Mitigation: Review hook commands and generated configuration before copying or installing them, then scan the resulting automation before deployment. <br>
Risk: The security summary flags insufficient user-facing confirmation and scoping for persistent changes. <br>
Mitigation: Confirm the target automation type, target scope, and persistence location before applying generated changes. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/claudify) <br>
- [CHANGELOG.md](CHANGELOG.md) <br>
- [Background Polling](background-polling.md) <br>
- [Improve](improve.md) <br>
- [Persist](persist.md) <br>
- [Automation Decision Guide](resources/automation-decision-guide.md) <br>
- [Hook Examples](resources/hook-examples.md) <br>
- [Plugin Creation Guide](resources/plugin-creation.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with file templates and inline shell or JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose or create persistent Claude Code automation files, hook configuration, and memory records when used for those workflows.] <br>

## Skill Version(s): <br>
0.5.1 (source: ClawHub release metadata and CHANGELOG.md, released 2026-07-28) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
