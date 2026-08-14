## Description:

Routes complex software work to the smallest defensible workflow, keeps one semantic lead across eight specialists, asks for intent confirmation when needed, and closes with verifiable evidence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fxbin](https://clawhub.ai/user/fxbin)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering teams use this skill to route complex software work into bounded delivery, planning, iteration, release, and governance workflows with explicit evidence and recovery anchors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automation paths can run shell commands and mutate repository files.

Mitigation: Review generated commands and command-bearing JSON before execution; prefer disposable worktrees for automation.

Risk: The skill can create .vidt workflow state, resume plans, and remediation artifacts in a candidate repository.

Mitigation: Install it only where workflow orchestration is desired, and check scope, residual risk, and completion evidence before accepting changes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/fxbin/skills/virtual-intelligent-dev-team)
- [Server-Resolved GitHub Repository](https://github.com/fxbin/virtual-intelligent-dev-team)
- [Public Documentation Site](https://fxbin.github.io/virtual-intelligent-dev-team)
- [Architecture Documentation](https://fxbin.github.io/virtual-intelligent-dev-team/architecture.html)
- [Playbook Index](references/playbook-index.md)
- [Tooling Command Index](references/tooling-command-index.md)
- [Agent Catalog](references/agent-catalog.md)
- [Team Engine Lite Protocol](references/team-engine-lite-protocol.md)

## Skill Output:

**Output Type(s):** [text, guidance, markdown, code, shell commands, configuration, JSON files]

**Output Format:** [Markdown guidance with code blocks, shell commands, configuration snippets, and optional structured JSON artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local workflow state, evidence files, resume anchors, and command-bearing plans when automation paths are used.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
