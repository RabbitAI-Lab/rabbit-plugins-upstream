## Description: <br>
Self-orchestrating multi-agent development workflows that help a developer describe the desired outcome while the agent coordinates research, architecture, implementation, validation, testing, documentation, and release steps. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gasgangrene](https://clawhub.ai/user/gasgangrene) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to coordinate multi-agent software development workflows for new features, bug fixes, API changes, refactoring, research, issue processing, and release preparation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can direct agents into high-impact GitHub and release actions. <br>
Mitigation: Require manual confirmation for PR merges, branch deletion, issue closure, release creation, and unattended cron-triggered runs. <br>
Risk: Full workflow use may involve local file changes, shell commands, tests, web research, browser automation, network access, and credentials. <br>
Mitigation: Install only for real development coordination, run in a controlled workspace, and keep GitHub tokens narrowly scoped. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gasgangrene/skills/cc-godmode) <br>
- [Publisher profile](https://clawhub.ai/user/gasgangrene) <br>
- [Declared repository](https://github.com/cubetribe/openclaw-godmode-skill) <br>
- [OpenClaw](https://openclaw.ai) <br>
- [Claude Code](https://claude.ai/code) <br>
- [Workflow documentation](artifact/docs/WORKFLOWS.md) <br>
- [Agent specifications](artifact/docs/AGENTS.md) <br>
- [Troubleshooting guide](artifact/docs/TROUBLESHOOTING.md) <br>
- [Migration guide](artifact/docs/MIGRATION.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline command and code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce workflow reports, implementation plans, code changes, validation results, test artifacts, documentation updates, and release checklists when agents follow the workflow.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata; artifact metadata declares 5.11.3) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
