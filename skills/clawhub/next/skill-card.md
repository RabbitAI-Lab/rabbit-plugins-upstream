## Description:

Suggests next actions after task completion, with stall detection, ask gates, and context-specific follow-up patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[drumrobot](https://clawhub.ai/user/drumrobot)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to decide what to do after a task completes, such as verifying work, continuing pending items, creating follow-up tasks, or addressing stalls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad reactive triggers can initiate follow-up workflow actions after ordinary completion signals.

Mitigation: Install only in environments where follow-up prompts and actions are expected, and review suggested actions before execution.

Risk: Ambiguous stall detection can route work into repair flows when the intended next step is unclear.

Mitigation: Use the documented ask gates and task-list checks to confirm current work before invoking repair actions.

Risk: The skill may affect workflows that can push code, update pull requests, write trackers, or trigger review bots.

Mitigation: Require operator review before deployment in those environments and limit agent permissions where possible.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/drumrobot/skills/next)
- [Stall Detection](artifact/stall-detect.md)
- [Ask Gates](artifact/ask-gates.md)
- [Suggestion Patterns](artifact/suggestion-patterns.md)

## Skill Output:

**Output Type(s):** [text, guidance, shell commands]

**Output Format:** [Markdown text with next-action options and occasional inline command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May recommend or trigger follow-up workflow actions when a stall is detected.]

## Skill Version(s):

0.7.3 (source: server release metadata and changelog, released 2026-08-12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
