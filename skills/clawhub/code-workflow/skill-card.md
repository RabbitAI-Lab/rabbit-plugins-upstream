## Description:

Guides agents through a four-stage code-change workflow: research, planning, user review, and TDD-based implementation, with optional PR capture support.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to structure non-trivial code changes, issue work, feature implementation, plan authoring, and pull-request preparation with explicit research, planning, approval, testing, and commit gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can write local research and plan files and expects local commits during implementation.

Mitigation: Use it only in repositories where generated planning files and local commits are acceptable, and review changes before pushing or publishing.

Risk: The workflow can post plans to linked GitHub issues and prepare PR content when the task context calls for those actions.

Mitigation: Confirm that repository issue comments, PR bodies, and any linked task details are appropriate for the target public or private repository before allowing publication.

Risk: Optional RAG dispatch can send research or plan artifacts to a configured receiver.

Mitigation: Enable RAG dispatch only for approved receivers and avoid dispatching sensitive repository details to untrusted stores.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [Skill overview and topics](artifact/SKILL.md)
- [Research, plan, review, and branch workflow](artifact/steps.md)
- [TDD implementation workflow](artifact/implement.md)
- [PR workflow with visual evidence](artifact/pr.md)
- [Plan and research pre-search obligation](artifact/plan-research-search.md)
- [Release changelog](artifact/CHANGELOG.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown guidance with file paths, checklists, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce or update local research and plan files, commit guidance, GitHub issue or PR text, and visual capture instructions when explicitly requested.]

## Skill Version(s):

0.6.3 (source: release evidence and CHANGELOG, released 2026-08-17; SKILL.md metadata version is 0.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
