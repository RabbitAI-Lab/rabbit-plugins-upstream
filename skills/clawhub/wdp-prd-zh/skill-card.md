## Description:

需求调度官 helps Chinese-speaking developers capture software requirements as backlog cards, compute dependency and conflict scheduling, and dispatch confirmed work to background agents for implementation and acceptance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[luckystar513](https://clawhub.ai/user/luckystar513)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to discuss, record, prioritize, confirm, dispatch, and accept software requirements without blocking the main agent session. It supports backlog review, dependency and conflict checks, background implementation through subagents, test/review gates, and markdown-based project planning records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dispatch and acceptance workflows may launch implementation agents, run the project test suite, and execute repository build or test scripts.

Mitigation: Install and use the skill only in repositories where those commands are trusted, and review dispatch choices before allowing background implementation.

Risk: Acceptance can merge worktree branch changes into the current branch after implementation.

Mitigation: Require the documented full test run, code review, change summary, and user confirmation before marking a requirement done or merging work.

Risk: The skill creates and updates planning files in the project and under the configured PRD root.

Mitigation: Check the .wdp-prd pointer and PRD_ROOT location during initialization, and review generated backlog cards and execution plans before dispatch.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/luckystar513/skills/wdp-prd-zh)
- [Requirement card template](artifact/references/card-template.md)
- [Dry-run test scenarios](artifact/references/test-scenarios.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown requirement cards, markdown execution plans, status reports, implementation summaries, test results, and review guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and updates backlog cards, execution-plan.md, implementation plan archives, and the .wdp-prd project pointer; dispatch and acceptance flows may run tests and merge reviewed worktree branches.]

## Skill Version(s):

1.0.0 (source: evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
