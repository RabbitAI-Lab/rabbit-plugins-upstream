## Description:

Suggests next actions after task completion, including explicit next-action requests, supported auto-invocation flows, stall detection, ask gates, and context-specific follow-up option patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide what to do after task completion: continue pending work, verify or commit changes, push or monitor CI, route stalled work to a fix flow, or ask the user for a decision using context-specific options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can automatically inspect broad workflow state, including task lists, project checklists, GitHub or CI state, context logs, hook configuration, and some organization metadata.

Mitigation: Review the hook setup before deployment, restrict connected tools to the intended workspace, and disable or narrow auto-invocation if only explicit /next behavior is desired.

Risk: The skill may invoke follow-up or fix flows after task completion when it detects stalled work or missing next steps.

Mitigation: Keep user confirmation gates active, review suggested actions before execution, and verify that dependent skills such as fix are available and appropriate for the environment.

Risk: Follow-up suggestions can be incorrect or stale if the agent reads outdated task, checklist, PR, or CI state.

Mitigation: Require current-state checks before presenting options, especially for stale prior-session candidates, active task lists, and PR or issue references.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Ask Gates](ask-gates.md)
- [Stall Detection](stall-detect.md)
- [Suggestion Patterns](suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown prose with structured next-action options and occasional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask the user to choose among follow-up options and may route stalled work to a fix flow when available.]

## Skill Version(s):

0.9.0 (source: server release metadata and CHANGELOG, released 2026-08-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
