## Description:

Scaffold MVP helps agents bootstrap a new empty repository into an agile .NET, Blazor, or Angular MVP with clean engineering boundaries, atomic configuration, stability checks, and Portuguese (pt-BR) user-facing prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[afonsoft](https://clawhub.ai/user/afonsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to bootstrap a new MVP repository with an opinionated .NET, Blazor, or Angular stack, project structure, documentation trail, build checks, and local service stubs. It is intended for empty repositories after initial product context has been established, or when a user explicitly requests a quick MVP bootstrap.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can install persistent repo-local agent harness files and hooks.

Mitigation: Use it only in a new repository where this harness is intended, then review generated .claude hooks, skills, rules, CLAUDE.md or AGENTS.md, and memory files before continuing.

Risk: The skill proposes stack and dependency choices that may not match local policy or support requirements.

Mitigation: Confirm the proposed stack and exact dependency versions before allowing project setup to proceed.

Risk: Approval prompts are mandated in Portuguese, which may reduce clarity for non-Portuguese users.

Mitigation: Have a Portuguese-capable reviewer confirm the prompts and approvals, or adapt the workflow language before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/afonsoft/skills/scaffold-mvp)
- [Publisher metadata URL](https://github.com/afonsoft/skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces repo scaffolding guidance and file-oriented implementation steps for an agent; no structured API response is specified.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
