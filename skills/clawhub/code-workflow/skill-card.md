## Description:

Code Workflow guides agents through a research, plan, user review, and TDD implementation workflow for code changes, with optional PR capture support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to handle moderate or complex code changes through researched planning, explicit user review, TDD implementation, and optional PR evidence capture.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may search local, peer, or memory-backed project documentation and expose sensitive repository context in private workspaces.

Mitigation: Review and limit RAG receiver configuration, peer repository search paths, and artifact dispatch behavior before use.

Risk: The workflow can lead agents toward durable git and GitHub actions such as commits, pushes, issue updates, and PR creation.

Mitigation: Require explicit user approval for publishing actions and review branch, issue, and PR targets before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [Workflow steps](artifact/steps.md)
- [Implementation workflow](artifact/implement.md)
- [PR workflow](artifact/pr.md)
- [Plan and research pre-search obligation](artifact/plan-research-search.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update research, plan, checklist, commit, and PR text artifacts when the host agent follows the workflow.]

## Skill Version(s):

0.8.0 (source: server release metadata and CHANGELOG, released 2026-08-29; SKILL.md metadata reports 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
