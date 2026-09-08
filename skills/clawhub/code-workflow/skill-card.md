## Description:

Guides agents through a four-stage code-change workflow covering research, planning, user review, TDD implementation, and optional PR capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineering agents use this skill to plan, review, implement, test, commit, and optionally prepare PR evidence for code changes. It is aimed at issue implementation, tracked tasks, new features, and changes that benefit from explicit research, plan, and user-approval gates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may search RAG, memory, and peer-workspace documentation stores, which can expose broad planning context.

Mitigation: Disable or tightly configure RAG and memory dispatch, and require explicit approval before peer-workspace searches.

Risk: The skill writes persistent research, plan, and walkthrough artifacts.

Mitigation: Set the output directory deliberately and review generated artifacts before sharing or indexing them.

Risk: PR publishing, push, and issue updates can affect external project state.

Mitigation: Require explicit user instruction before publishing actions and review PR bodies before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/code-workflow)
- [Skill definition](artifact/SKILL.md)
- [Steps guide](artifact/steps.md)
- [Implementation guide](artifact/implement.md)
- [PR workflow guide](artifact/pr.md)
- [Plan and research pre-search guide](artifact/plan-research-search.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline code blocks, shell commands, and file artifact templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write research, plan, and walkthrough artifacts to a configured output directory, and may generate PR body or visual-evidence guidance when explicitly requested.]

## Skill Version(s):

0.9.0 (source: server release metadata and CHANGELOG, released 2026-09-06)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
